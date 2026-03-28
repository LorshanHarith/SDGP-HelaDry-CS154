import requests
import json

def test_batch_management_api():
    """Test batch creation and management API endpoints"""
    base_url = "http://localhost:5000"
    timeout = 30
    
    # Mock authentication token (would normally come from login)
    auth_token = "mock_token_123"
    headers = {"Authorization": f"Bearer {auth_token}"}
    
    # Test batch creation
    batch_data = {
        "device_id": "HELADRY-001",
        "crop_type": "mango",
        "tray_count": 3,
        "batch_weight": 5.5
    }
    
    try:
        # Test create batch endpoint
        response = requests.post(f"{base_url}/batch/create", 
                               json=batch_data, 
                               headers=headers,
                               timeout=timeout)
        assert response.status_code == 201, f"Expected 201 for batch creation, got {response.status_code}"
        
        json_data = response.json()
        assert "batch_id" in json_data, "Batch creation response missing batch_id"
        assert "device_id" in json_data, "Batch creation response missing device_id"
        assert "status" in json_data, "Batch creation response missing status"
        assert json_data["status"] == "active", "Expected batch status to be 'active'"
        
        # Test get batch status
        batch_id = json_data["batch_id"]
        response = requests.get(f"{base_url}/batch/{batch_id}/status", 
                              headers=headers,
                              timeout=timeout)
        assert response.status_code == 200, f"Expected 200 for batch status, got {response.status_code}"
        
        json_data = response.json()
        assert "batch_id" in json_data, "Batch status response missing batch_id"
        assert "status" in json_data, "Batch status response missing status"
        assert "start_time" in json_data, "Batch status response missing start_time"
        
        # Test batch metrics
        response = requests.get(f"{base_url}/batch/{batch_id}/metrics", 
                              headers=headers,
                              timeout=timeout)
        assert response.status_code == 200, f"Expected 200 for batch metrics, got {response.status_code}"
        
        json_data = response.json()
        assert "temperature" in json_data, "Batch metrics missing temperature"
        assert "humidity" in json_data, "Batch metrics missing humidity"
        assert "fan_speed" in json_data, "Batch metrics missing fan_speed"
        
        # Test batch completion
        response = requests.post(f"{base_url}/batch/{batch_id}/complete", 
                               headers=headers,
                               timeout=timeout)
        assert response.status_code == 200, f"Expected 200 for batch completion, got {response.status_code}"
        
        json_data = response.json()
        assert "batch_id" in json_data, "Batch completion response missing batch_id"
        assert json_data["status"] == "completed", "Expected batch status to be 'completed'"
        
    except requests.RequestException as e:
        assert False, f"Request failed: {e}"
    except ValueError:
        assert False, "Response is not valid JSON"

test_batch_management_api()