import requests

def test_device_register_without_authorization():
    base_url = "http://localhost:5000"
    url = f"{base_url}/device/register"
    payload = {
        "device_id": "test_device_123",
        "model": "ModelX",
        "pairing_code": "PAIR1234"
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        assert response.status_code == 401, f"Expected 401 Unauthorized, got {response.status_code}"
    except requests.RequestException as e:
        assert False, f"Request failed: {e}"

test_device_register_without_authorization()