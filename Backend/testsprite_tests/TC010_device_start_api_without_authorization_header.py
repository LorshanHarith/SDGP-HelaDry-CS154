import requests

def test_device_start_without_authorization():
    url = "http://localhost:5000/device/start"
    payload = {
        "device_id": "any_device_id",
        "batch_params": {}
    }
    try:
        response = requests.post(url, json=payload, timeout=30)
    except requests.RequestException as e:
        assert False, f"Request failed: {e}"

    assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"

test_device_start_without_authorization()