import requests

BASE_URL = "http://localhost:5000"
AUTH_TOKEN = "Bearer dummy_token_for_test"

def test_device_update_temperature_with_invalid_string_target():
    # First register a device to get a valid device_id for the test
    register_payload = {
        "device_id": "test_device_update_temp_invalid_001",
        "model": "TestModelX",
        "pairing_code": "PAIR1234"
    }
    headers = {
        "Authorization": AUTH_TOKEN,
        "Content-Type": "application/json"
    }
    try:
        # Register device
        r_reg = requests.post(
            f"{BASE_URL}/device/register",
            json=register_payload,
            headers=headers,
            timeout=30
        )
        assert r_reg.status_code == 201, f"Device registration failed: {r_reg.text}"
        device_id = r_reg.json().get("device_id")
        assert device_id == register_payload["device_id"]

        # Attempt to update temperature with invalid string target_temperature
        update_payload = {
            "device_id": device_id,
            "target_temperature": "invalid_string"
        }
        r_update = requests.post(
            f"{BASE_URL}/device/update-temperature",
            json=update_payload,
            headers=headers,
            timeout=30
        )
        assert r_update.status_code == 400, f"Expected 400 Bad Request, got {r_update.status_code}"
        # Optionally verify error message or error structure in response JSON
        json_resp = r_update.json()
        assert "error" in json_resp or "message" in json_resp or r_update.text, "Expected error detail in response"

    finally:
        # Clean up - delete the registered test device if possible
        try:
            requests.delete(
                f"{BASE_URL}/device/delete",
                json={"device_id": register_payload["device_id"]},
                headers=headers,
                timeout=30
            )
        except Exception:
            pass

test_device_update_temperature_with_invalid_string_target()
