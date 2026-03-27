import requests
import uuid

BASE_URL = "http://localhost:5000"
AUTH_HEADER = {"Authorization": "Bearer dummy_token"}
TIMEOUT = 30

def test_device_update_fan_speed_with_valid_payload():
    # First register a device to get a valid device_id
    device_id = f"test-device-{uuid.uuid4()}"
    register_payload = {
        "device_id": device_id,
        "model": "test-model",
        "pairing_code": "test-pairing-code"
    }
    headers = {**AUTH_HEADER, "Content-Type": "application/json"}
    try:
        # Register device
        r_reg = requests.post(
            f"{BASE_URL}/device/register",
            json=register_payload,
            headers=headers,
            timeout=TIMEOUT,
        )
        assert r_reg.status_code == 201, f"Device registration failed: {r_reg.text}"
        json_reg = r_reg.json()
        assert json_reg["device_id"] == device_id
        assert "assigned_to_user" in json_reg

        # Now update fan speed with valid payload
        fan_speed_value = 5
        update_payload = {"device_id": device_id, "fan_speed": fan_speed_value}
        r_update = requests.post(
            f"{BASE_URL}/device/update-fan-speed",
            json=update_payload,
            headers=headers,
            timeout=TIMEOUT,
        )
        assert r_update.status_code == 200, f"Fan speed update failed: {r_update.text}"
        json_update = r_update.json()
        assert json_update["device_id"] == device_id
        assert json_update["fan_speed"] == fan_speed_value

    finally:
        # Cleanup: delete the created device if API supports deletion
        # The PRD doesn't specify delete endpoint, so skipping deletion here
        pass

test_device_update_fan_speed_with_valid_payload()
