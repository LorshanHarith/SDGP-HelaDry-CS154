#!/usr/bin/env python3
"""
Firebase Authentication Setup for HelaDry Postman automation.
This script helps set up Firebase JWT tokens for testing.
"""

import json
import os
import sys
from datetime import datetime

def create_firebase_config_template():
    """Create a template Firebase configuration file."""
    config_template = {
        "firebase": {
            "projectId": "your-project-id",
            "apiKey": "your-api-key",
            "appId": "your-app-id",
            "authDomain": "your-project-id.firebaseapp.com",
            "databaseURL": "https://your-project-id-default-rtdb.firebaseio.com",
            "storageBucket": "your-project-id.appspot.com",
            "messagingSenderId": "your-sender-id",
            "serviceAccount": {
                "type": "service_account",
                "project_id": "your-project-id",
                "private_key_id": "your-private-key-id",
                "private_key": "-----BEGIN PRIVATE KEY-----\nyour-private-key-here\n-----END PRIVATE KEY-----",
                "client_email": "your-service-account@your-project-id.iam.gserviceaccount.com",
                "client_id": "your-client-id",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account%40your-project-id.iam.gserviceaccount.com"
            }
        }
    }
    
    return config_template

def create_postman_environment_with_token(firebase_token=None):
    """Create or update Postman environment with Firebase token."""
    
    # Load existing environment or create new one
    env_file = "postman_environment.json"
    if os.path.exists(env_file):
        try:
            with open(env_file, 'r') as f:
                env_data = json.load(f)
        except:
            env_data = {
                "id": "hela-dry-environment",
                "name": "HelaDry IoT Environment",
                "values": []
            }
    else:
        env_data = {
            "id": "hela-dry-environment",
            "name": "HelaDry IoT Environment",
            "values": []
        }
    
    # Update or add Firebase token
    firebase_token_set = False
    for value in env_data.get("values", []):
        if value["key"] == "firebaseToken":
            if firebase_token:
                value["value"] = firebase_token
                value["description"] = f"Firebase JWT token (set {datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"
            firebase_token_set = True
            break
    
    if not firebase_token_set and firebase_token:
        env_data["values"].append({
            "key": "firebaseToken",
            "value": firebase_token,
            "description": f"Firebase JWT token (set {datetime.now().strftime('%Y-%m-%d %H:%M:%S')})",
            "enabled": True,
            "type": "secret"
        })
    
    # Ensure other required variables exist
    required_vars = [
        {"key": "baseUrl", "value": "http://localhost:5000", "description": "Base URL for the HelaDry backend API", "type": "default"},
        {"key": "testDeviceId", "value": "test-device-{{randomUUID}}", "description": "Test device ID (auto-generated)", "type": "default"},
        {"key": "testSessionId", "value": "", "description": "Test session ID (auto-populated during tests)", "type": "default"},
        {"key": "apiTimeout", "value": "30000", "description": "API timeout in milliseconds", "type": "default"}
    ]
    
    for var in required_vars:
        var_exists = False
        for value in env_data.get("values", []):
            if value["key"] == var["key"]:
                var_exists = True
                break
        if not var_exists:
            env_data["values"].append({**var, "enabled": True})
    
    # Save updated environment
    try:
        with open(env_file, 'w') as f:
            json.dump(env_data, f, indent=2)
        print(f"✅ Updated Postman environment: {env_file}")
        return True
    except Exception as e:
        print(f"❌ Failed to update environment file: {e}")
        return False

def generate_mock_token():
    """Generate a mock Firebase token for testing (if no real Firebase setup)."""
    import base64
    import time
    import hashlib
    
    # Create a mock JWT token structure
    header = {
        "alg": "none",
        "typ": "JWT"
    }
    
    payload = {
        "iss": "https://securetoken.google.com/your-project-id",
        "aud": "your-project-id",
        "auth_time": int(time.time()),
        "user_id": "test-user-123",
        "sub": "test-user-123",
        "iat": int(time.time()),
        "exp": int(time.time()) + 3600,  # 1 hour expiry
        "email": "test@example.com",
        "email_verified": False,
        "firebase": {
            "identities": {
                "email": ["test@example.com"]
            },
            "sign_in_provider": "password"
        }
    }
    
    # For testing purposes, create a mock token
    # In a real scenario, you'd use Firebase Admin SDK to generate this
    mock_token = "mock_firebase_token_for_testing_purposes_only_replace_with_real_token"
    
    return mock_token

def setup_firebase_instructions():
    """Print instructions for setting up Firebase authentication."""
    
    instructions = """
🔧 FIREBASE AUTHENTICATION SETUP GUIDE
==========================================

To run the automated Postman tests, you need a valid Firebase JWT token.

OPTION 1: Quick Setup (For Testing)
------------------------------------
1. Use the mock token provided below (limited functionality):
   Token: mock_firebase_token_for_testing_purposes_only_replace_with_real_token

2. Run: python setup_firebase_auth.py --token "your-mock-token"

OPTION 2: Real Firebase Setup
-----------------------------
1. Go to Firebase Console: https://console.firebase.google.com/
2. Create a new project or select existing one
3. Enable Authentication (Authentication > Sign-in method)
4. Set up service account:
   - Go to Project Settings > Service Accounts
   - Click "Generate new private key"
   - Save the JSON file securely
5. Install Firebase Admin SDK:
   pip install firebase-admin
6. Use the provided script to generate real tokens

OPTION 3: Manual Token Setup
---------------------------
1. Generate a custom token using Firebase Admin SDK
2. Exchange it for an ID token
3. Use that token in the Postman environment

FILES CREATED:
- firebase_config_template.json: Template for Firebase configuration
- Updated postman_environment.json: With your token

NEXT STEPS:
1. Set your Firebase token using: python setup_firebase_auth.py --token "your-token"
2. Run the automated tests: automate_postman_tests.bat
3. Check the generated reports in test_reports/ folder

For more help, see the Firebase documentation:
https://firebase.google.com/docs/auth/admin/create-custom-tokens
"""
    
    print(instructions)

def main():
    """Main function for Firebase setup."""
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        setup_firebase_instructions()
        return
    
    if len(sys.argv) > 2 and sys.argv[1] == "--token":
        token = sys.argv[2]
        print(f"🔑 Setting Firebase token: {token[:20]}...")
        success = create_postman_environment_with_token(token)
        if success:
            print("✅ Firebase token configured successfully!")
            print("🚀 You can now run: automate_postman_tests.bat")
        return
    
    print("🔧 Setting up Firebase authentication for HelaDry tests...")
    
    # Create Firebase config template
    config_template = create_firebase_config_template()
    try:
        with open("firebase_config_template.json", 'w') as f:
            json.dump(config_template, f, indent=2)
        print("✅ Created firebase_config_template.json")
    except Exception as e:
        print(f"❌ Failed to create Firebase config template: {e}")
    
    # Create/update Postman environment
    mock_token = generate_mock_token()
    success = create_postman_environment_with_token(mock_token)
    
    if success:
        print("✅ Firebase authentication setup complete!")
        print(f"🔑 Mock token added: {mock_token[:20]}...")
        print("📝 To use a real Firebase token, run:")
        print("   python setup_firebase_auth.py --token \"your-real-firebase-token\"")
        print("🚀 Then run: automate_postman_tests.bat")
    else:
        print("❌ Firebase setup failed!")
    
    # Show instructions
    setup_firebase_instructions()

if __name__ == "__main__":
    main()