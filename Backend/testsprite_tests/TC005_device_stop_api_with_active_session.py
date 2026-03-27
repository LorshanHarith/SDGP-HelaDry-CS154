import requests
import uuid

BASE_URL = "http://localhost:5000"
AUTH_HEADER_KEY = "Authorization"
TIMEOUT = 30
DUMMY_TOKEN = "Bearer dummy_token_for_testing"


def test_device_stop_api_with_active_session():
    headers = {AUTH_HEADER_KEY: DUMMY_TOKEN, "Content-Type": "application/json"}

    # Step 1: Register a new device to get a device_id
    device_id = str(uuid.uuid4())
    register_payload = {
        "device_id": device_id,
        "model": "Model-X",
        "pairing_code": "PAIR1234"
    }

    try:
        resp_register = requests.post(
            f"{BASE_URL}/device/register",
            json=register_payload,
            headers=headers,
            timeout=TIMEOUT
        )
        resp_register.raise_for_status()
        register_data = resp_register.json()
        assert resp_register.status_code == 201
        assert register_data.get("device_id") == device_id
        assert "assigned_to_user" in register_data

        # Step 2: Start a session on the device to get an active session_id
        start_payload = {
            "device_id": device_id,
            "batch_params": {"param1": "value1"}  # Assuming minimal placeholder batch_params
        }
        resp_start = requests.post(
            f"{BASE_URL}/device/start",
            json=start_payload,
            headers=headers,
            timeout=TIMEOUT
        )
        resp_start.raise_for_status()
        start_data = resp_start.json()
        assert resp_start.status_code == 200
        assert start_data.get("status") == "started"
        session_id = start_data.get("session_id")
        assert session_id is not None

        # Step 3: Stop the active session using device_id and session_id
        stop_payload = {
            "device_id": device_id,
            "session_id": session_id
        }
        resp_stop = requests.post(
            f"{BASE_URL}/device/stop",
            json=stop_payload,
            headers=headers,
            timeout=TIMEOUT
        )
        resp_stop.raise_for_status()
        stop_data = resp_stop.json()
        assert resp_stop.status_code == 200
        assert stop_data.get("session_id") == session_id
        assert stop_data.get("status") == "stopped"

    finally:
        # Cleanup: Delete the registered device if an endpoint exists
        # The PRD does not describe a device delete endpoint, so no cleanup call is made.
        pass


test_device_stop_api_with_active_session()
