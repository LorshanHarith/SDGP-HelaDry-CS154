import requests
import json

def test_manual_controls_api():
    """Test manual control API endpoints for fan, heater, and temperature"""
    base_url = "http://localhost:5000"
    timeout = 30
    
    # Mock authentication token
    auth_token = "mock_token_123"
    headers = {"Authorization": f"Bearer {auth_token}"}
    
    device_id = "HELADRY-001"
    
    try:
        # Test fan speed control
        fan_data = {
            "device_id": device_id,
            "fan_speed": 75
        }
        
        response = requests.post(f"{base_url}/device/{device_id}/control/fan", 
                               json=fan_data, 
                               headers=headers,
                               timeout=timeout)
        assert response.status_code == 200, f"Expected 200 for fan control, got {response.status_code}"
        
        json_data = response.json()
        assert "device_id" in json_data, "Fan control response missing device_id"
        assert "fan_speed" in json_data, "Fan control response missing fan_speed"
        assert json_data["fan_speed"] == 75, "Fan speed not set correctly"
        
        # Test heater control
        heater_data = {
            "device_id": device_id,
            "heater_status": "ON"
        }
        
        response = requests.post(f"{base_url}/device/{device_id}/control/heater", 
                               json=heater_data, 
                               headers=headers,
                               timeout=timeout)
        assert response.status_code == 200, f"Expected 200 for heater control, got {response.status_code}"
        
        json_data = response.json()
        assert "device_id" in json_data, "Heater control response missing device_id"
        assert "heater_status" in json_data, "Heater control response missing heater_status"
        assert json_data["heater_status"] == "ON", "Heater status not set correctly"
        
        # Test temperature control
        temp_data = {
            "device_id": device_id,
            "target_temperature": 65
        }
        
        response = requests.post(f"{base_url}/device/{device_id}/control/temperature", 
                               json=temp_data, 
                               headers=headers,
                               timeout=timeout)
        assert response.status_code == 200, f"Expected 200 for temperature control, got {response.status_code}"
        
        json_data = response.json()
        assert "device_id" in json_data, "Temperature control response missing device_id"
        assert "target_temperature" in json_data, "Temperature control response missing target_temperature"
        assert json_data["target_temperature"] == 65, "Target temperature not set correctly"
        
        # Test emergency stop
        response = requests.post(f"{base_url}/device/{device_id}/control/emergency-stop", 
                               headers=headers,
                               timeout=timeout)
        assert response.status_code == 200, f"Expected 200 for emergency stop, got {response.status_code}"
        
        json_data = response.json()
        assert "device_id" in json_data, "Emergency stop response missing device_id"
        assert "status" in json_data, "Emergency stop response missing status"
        assert json_data["status"] == "emergency_stopped", "Device not in emergency stop status"
        
        # Test invalid fan speed (out of range)
        invalid_fan_data = {
            "device_id": device_id,
            "fan_speed": 150  # Invalid: > 100
        }
        
        response = requests.post(f"{base_url}/device/{device_id}/control/fan", 
                               json=invalid_fan_data, 
                               headers=headers,
                               timeout=timeout)
        assert response.status_code == 400, f"Expected 400 for invalid fan speed, got {response.status_code}"
        
        # Test invalid temperature (out of range)
        invalid_temp_data = {
            "device_id": device_id,
            "target_temperature": 120  # Invalid: > 80
        }
        
        response = requests.post(f"{base_url}/device/{device_id}/control/temperature", 
                               json=invalid_temp_data, 
                               headers=headers,
                               timeout=timeout)
        assert response.status_code == 400, f"Expected 400 for invalid temperature, got {response.status_code}"
        
    except requests.RequestException as e:
        assert False, f"Request failed: {e}"
    except ValueError:
        assert False, "Response is not valid JSON"

test_manual_controls_api()