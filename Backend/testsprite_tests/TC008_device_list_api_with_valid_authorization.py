import requests

BASE_URL = "http://localhost:5000"
DEVICE_LIST_PATH = "/device/list"
AUTH_HEADER_KEY = "Authorization"
DUMMY_TOKEN = "Bearer dummy_token_123"

def test_device_list_api_with_valid_authorization():
    url = f"{BASE_URL}{DEVICE_LIST_PATH}"
    headers = {AUTH_HEADER_KEY: DUMMY_TOKEN}
    response = requests.get(url, headers=headers, timeout=30)

    # Assert HTTP status code is 200
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    # Assert response content is a JSON array (list) of devices
    try:
        data = response.json()
    except ValueError:
        assert False, "Response is not valid JSON"

    assert isinstance(data, list), f"Expected response to be a list but got {type(data)}"
    # Optionally: Validate that each device item contains expected keys (like device_id)
    for device in data:
        assert isinstance(device, dict), "Device item is not a dictionary"
        assert "device_id" in device, "Device item does not contain 'device_id' key"
        # user association key is optional; no assertion needed

test_device_list_api_with_valid_authorization()