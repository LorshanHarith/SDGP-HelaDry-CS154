import requests
import json

def test_user_authentication_api():
    """Test user registration and login API endpoints"""
    base_url = "http://localhost:5000"
    timeout = 30
    
    # Test user registration
    registration_data = {
        "email": "test@example.com",
        "password": "testpassword123",
        "confirm_password": "testpassword123"
    }
    
    try:
        # Test registration endpoint
        response = requests.post(f"{base_url}/auth/register", 
                               json=registration_data, 
                               timeout=timeout)
        assert response.status_code == 201, f"Expected 201 for registration, got {response.status_code}"
        
        json_data = response.json()
        assert "user_id" in json_data, "Registration response missing user_id"
        assert "email" in json_data, "Registration response missing email"
        
        # Test login endpoint
        login_data = {
            "email": "test@example.com",
            "password": "testpassword123"
        }
        
        response = requests.post(f"{base_url}/auth/login", 
                               json=login_data, 
                               timeout=timeout)
        assert response.status_code == 200, f"Expected 200 for login, got {response.status_code}"
        
        json_data = response.json()
        assert "token" in json_data, "Login response missing authentication token"
        assert "user_id" in json_data, "Login response missing user_id"
        
        # Test invalid login
        invalid_login = {
            "email": "test@example.com",
            "password": "wrongpassword"
        }
        
        response = requests.post(f"{base_url}/auth/login", 
                               json=invalid_login, 
                               timeout=timeout)
        assert response.status_code == 401, f"Expected 401 for invalid login, got {response.status_code}"
        
    except requests.RequestException as e:
        assert False, f"Request failed: {e}"
    except ValueError:
        assert False, "Response is not valid JSON"

test_user_authentication_api()