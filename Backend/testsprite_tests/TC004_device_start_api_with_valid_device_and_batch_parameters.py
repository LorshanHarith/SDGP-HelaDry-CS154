import requests
import uuid
from unittest.mock import patch

BASE_URL = "http://localhost:5000"
AUTH_HEADER = {"Authorization": "Bearer dummy_token_for_testing"}
TIMEOUT = 30

@patch("firebase_admin.auth.verify_id_token", return_value={"uid": "test_user_123"})
def test_device_start_api_with_valid_device_and_batch_params(mock_verify_token):
    device_id = f"test-device-{uuid.uuid4()}"
    session_id = None
    try:
        # First, register the device to have a valid device_id
        register_payload = {
            "device_id": device_id,
            "model": "Model-X",
            "pairing_code": "PAIR1234"
        }
        reg_resp = requests.post(
            f"{BASE_URL}/device/register",
            headers=AUTH_HEADER,
            json=register_payload,
            timeout=TIMEOUT,
        )
        assert reg_resp.status_code == 201
        reg_data = reg_resp.json()
        assert reg_data.get("device_id") == device_id
        assert "assigned_to_user" in reg_data

        # Now start the device session
        batch_params = {"batch_name": "Test Batch A", "duration": 120}
        start_payload = {
            "device_id": device_id,
            "batch_params": batch_params
        }
        start_resp = requests.post(
            f"{BASE_URL}/device/start",
            headers=AUTH_HEADER,
            json=start_payload,
            timeout=TIMEOUT,
        )
        assert start_resp.status_code == 200
        start_data = start_resp.json()
        assert "session_id" in start_data
        assert start_data.get("status") == "started"
        session_id = start_data.get("session_id")
    finally:
        # Cleanup: stop session if started and delete device if possible
        if session_id and device_id:
            try:
                stop_payload = {"device_id": device_id, "session_id": session_id}
                requests.post(
                    f"{BASE_URL}/device/stop",
                    headers=AUTH_HEADER,
                    json=stop_payload,
                    timeout=TIMEOUT,
                )
            except Exception:
                pass
        if device_id:
            try:
                # No endpoint provided to delete device in PRD so ignoring device deletion
                pass
            except Exception:
                pass

test_device_start_api_with_valid_device_and_batch_params()