import requests
from unittest.mock import patch

BASE_URL = "http://localhost:5000"
DEVICE_REGISTER_PATH = "/device/register"
TIMEOUT = 30
AUTH_HEADER = "Authorization"
VALID_TOKEN = "Bearer dummy_token_12345"

@patch("firebase_admin.auth.verify_id_token", return_value={"uid": "test_user_123"})
def test_device_register_api_with_valid_authorization_and_payload(mock_verify):
    url = BASE_URL + DEVICE_REGISTER_PATH
    headers = {
        AUTH_HEADER: VALID_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "device_id": "device_123456",
        "model": "HDX-1000",
        "pairing_code": "PAIR1234"
    }
    response = None
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=TIMEOUT)
        assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
        resp_json = response.json()
        assert "device_id" in resp_json, "Response JSON missing 'device_id'"
        assert "assigned_to_user" in resp_json, "Response JSON missing 'assigned_to_user'"
        assert resp_json["device_id"] == payload["device_id"], "Response device_id mismatch"
        assert resp_json["assigned_to_user"] == "test_user_123", "Response assigned_to_user mismatch"
    finally:
        # Cleanup: delete the registered device
        if response is not None and response.status_code == 201:
            device_id = response.json().get("device_id")
            if device_id:
                del_url = BASE_URL + f"/device/{device_id}"
                # Attempt to delete with same auth header
                try:
                    requests.delete(del_url, headers=headers, timeout=TIMEOUT)
                except Exception:
                    pass

test_device_register_api_with_valid_authorization_and_payload()