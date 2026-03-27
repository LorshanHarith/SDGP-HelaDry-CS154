import requests
import uuid
from unittest.mock import patch

BASE_URL = "http://localhost:5000"
AUTH_HEADER = {"Authorization": "Bearer dummy_token"}
TIMEOUT = 30

def test_device_update_temperature_with_valid_target():
    # Mock firebase_admin.auth.verify_id_token to bypass real token verification
    with patch("firebase_admin.auth.verify_id_token") as mock_verify:
        mock_verify.return_value = {"uid": "test_user_123"}

        device_id = str(uuid.uuid4())
        register_payload = {
            "device_id": device_id,
            "model": "Model-X",
            "pairing_code": "PAIR1234"
        }

        # Register a device first
        try:
            register_resp = requests.post(
                f"{BASE_URL}/device/register",
                headers=AUTH_HEADER,
                json=register_payload,
                timeout=TIMEOUT
            )
            assert register_resp.status_code == 201, f"Device registration failed: {register_resp.text}"
            register_data = register_resp.json()
            assert register_data.get("device_id") == device_id
            assert "assigned_to_user" in register_data

            # Now update temperature with valid target_temperature within allowed range
            update_temp_payload = {
                "device_id": device_id,
                "target_temperature": 45.0
            }
            update_resp = requests.post(
                f"{BASE_URL}/device/update-temperature",
                headers=AUTH_HEADER,
                json=update_temp_payload,
                timeout=TIMEOUT
            )
            assert update_resp.status_code == 200, f"Update temperature failed: {update_resp.text}"
            update_data = update_resp.json()
            assert update_data.get("device_id") == device_id
            assert update_data.get("target_temperature") == 45.0

        finally:
            # Cleanup: delete the device if deletion endpoint exists (not described in PRD, so ignored)
            pass


test_device_update_temperature_with_valid_target()