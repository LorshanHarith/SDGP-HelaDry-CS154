import requests

BASE_URL = "http://localhost:5000"
TIMEOUT = 30
AUTH_HEADER = {"Authorization": "Bearer dummy_token_for_test"}


def test_session_my_sessions_api_with_valid_authorization():
    url = f"{BASE_URL}/session/my-sessions"
    try:
        response = requests.get(url, headers=AUTH_HEADER, timeout=TIMEOUT)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        json_data = response.json()
        assert isinstance(json_data, list), "Response is not a list of sessions"

        # Validate each session object contains required keys with appropriate types
        for session in json_data:
            assert isinstance(session, dict), "Session item is not a dict"
            assert "session_id" in session, "Missing session_id in session"
            assert isinstance(session["session_id"], (str, int)), "session_id should be str or int"

            assert "device_id" in session, "Missing device_id in session"
            assert isinstance(session["device_id"], (str, int)), "device_id should be str or int"

            assert "start_time" in session, "Missing start_time in session"
            assert isinstance(session["start_time"], str), "start_time should be str"

            assert "end_time" in session, "Missing end_time in session"
            # end_time can be None if session active or string if ended
            assert session["end_time"] is None or isinstance(session["end_time"], str), "end_time should be str or None"

            assert "status" in session, "Missing status in session"
            assert isinstance(session["status"], str), "status should be str"

            assert "metrics" in session, "Missing metrics in session"
            # metrics can be dict or possibly empty dict
            assert isinstance(session["metrics"], dict), "metrics should be dict"

    except requests.RequestException as e:
        assert False, f"Request failed: {e}"


test_session_my_sessions_api_with_valid_authorization()