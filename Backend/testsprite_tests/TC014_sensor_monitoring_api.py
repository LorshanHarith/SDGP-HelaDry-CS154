import requests
import json

def test_sensor_monitoring_api():
    """Test sensor data monitoring and real-time metrics API endpoints"""
    base_url = "http://localhost:5000"
    timeout = 30
    
    # Mock authentication token
    auth_token = "mock_token_123"
    headers = {"Authorization": f"Bearer {auth_token}"}
    
    # Test real-time sensor data
    device_id = "HELADRY-001"
    
    try:
        # Test get current sensor data
        response = requests.get(f"{base_url}/device/{device_id}/sensors", 
                              headers=headers,
                              timeout=timeout)
        assert response.status_code == 200, f"Expected 200 for sensor data, got {response.status_code}"
        
        json_data = response.json()
        assert "temperature" in json_data, "Sensor data missing temperature"
        assert "humidity" in json_data, "Sensor data missing humidity"
        assert "fan_speed" in json_data, "Sensor data missing fan_speed"
        assert "heater_status" in json_data, "Sensor data missing heater_status"
        assert "battery_level" in json_data, "Sensor data missing battery_level"
        assert "solar_voltage" in json_data, "Sensor data missing solar_voltage"
        
        # Validate data ranges
        assert isinstance(json_data["temperature"], (int, float)), "Temperature should be numeric"
        assert isinstance(json_data["humidity"], (int, float)), "Humidity should be numeric"
        assert 0 <= json_data["fan_speed"] <= 100, "Fan speed should be 0-100%"
        assert json_data["heater_status"] in ["ON", "OFF"], "Heater status should be ON or OFF"
        assert 0 <= json_data["battery_level"] <= 100, "Battery level should be 0-100%"
        
        # Test historical sensor data
        response = requests.get(f"{base_url}/device/{device_id}/sensors/history?limit=10", 
                              headers=headers,
                              timeout=timeout)
        assert response.status_code == 200, f"Expected 200 for historical data, got {response.status_code}"
        
        json_data = response.json()
        assert isinstance(json_data, list), "Historical data should be an array"
        if len(json_data) > 0:
            assert "timestamp" in json_data[0], "Historical data missing timestamp"
            assert "temperature" in json_data[0], "Historical data missing temperature"
            assert "humidity" in json_data[0], "Historical data missing humidity"
        
        # Test device status
        response = requests.get(f"{base_url}/device/{device_id}/status", 
                              headers=headers,
                              timeout=timeout)
        assert response.status_code == 200, f"Expected 200 for device status, got {response.status_code}"
        
        json_data = response.json()
        assert "device_id" in json_data, "Device status missing device_id"
        assert "connection_status" in json_data, "Device status missing connection_status"
        assert "last_seen" in json_data, "Device status missing last_seen"
        assert "firmware_version" in json_data, "Device status missing firmware_version"
        
        # Test alerts/notifications
        response = requests.get(f"{base_url}/device/{device_id}/alerts", 
                              headers=headers,
                              timeout=timeout)
        assert response.status_code == 200, f"Expected 200 for alerts, got {response.status_code}"
        
        json_data = response.json()
        assert isinstance(json_data, list), "Alerts should be an array"
        
    except requests.RequestException as e:
        assert False, f"Request failed: {e}"
    except ValueError:
        assert False, "Response is not valid JSON"

test_sensor_monitoring_api()