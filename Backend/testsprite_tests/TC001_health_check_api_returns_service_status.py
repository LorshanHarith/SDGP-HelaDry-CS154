import requests

def test_health_check_api_returns_service_status():
    base_url = "http://localhost:5000"
    timeout = 30
    try:
        response = requests.get(f"{base_url}/", timeout=timeout)
    except requests.RequestException as e:
        assert False, f"Request failed: {e}"
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    try:
        json_data = response.json()
    except ValueError:
        assert False, "Response is not valid JSON"
    assert "status" in json_data, "Response JSON missing 'status' key"
    assert json_data["status"] == "ok", f"Expected status 'ok' but got '{json_data['status']}'"
    assert "uptime" in json_data, "Response JSON missing 'uptime' key"
    assert "version" in json_data, "Response JSON missing 'version' key"

test_health_check_api_returns_service_status()