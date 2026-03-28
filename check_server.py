#!/usr/bin/env python3
"""
Server health check script for HelaDry Postman automation.
This script checks if the backend server is running and responding.
"""

import requests
import sys
import time
import json

def check_server_health():
    """Check if the HelaDry backend server is running and healthy."""
    base_url = "http://localhost:5000"
    max_retries = 5
    retry_delay = 2
    
    print(f"🔍 Checking server health at {base_url}/")
    
    for attempt in range(max_retries):
        try:
            response = requests.get(f"{base_url}/", timeout=10)
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    if data.get('status') == 'running' and data.get('service') == 'HelaDry Backend':
                        print("✅ Server is healthy and ready!")
                        return True
                    else:
                        print(f"⚠️  Server responded but with unexpected data: {data}")
                except json.JSONDecodeError:
                    print(f"⚠️  Server responded but invalid JSON: {response.text}")
            else:
                print(f"⚠️  Server responded with status {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print(f"❌ Connection failed (attempt {attempt + 1}/{max_retries})")
        except requests.exceptions.Timeout:
            print(f"⏰ Request timed out (attempt {attempt + 1}/{max_retries})")
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
        
        if attempt < max_retries - 1:
            print(f"⏳ Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
    
    print("❌ Server is not responding. Please check:")
    print("  1. Backend server is running on port 5000")
    print("  2. No firewall blocking the connection")
    print("  3. Python dependencies are installed")
    return False

if __name__ == "__main__":
    success = check_server_health()
    sys.exit(0 if success else 1)