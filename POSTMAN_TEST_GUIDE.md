# HelaDry Postman Test Execution Guide

This guide will help you run comprehensive Postman tests for your HelaDry IoT backend API and frontend integration.

## Files Created

1. **`postman_collection.json`** - Complete backend API test collection
2. **`postman_environment.json`** - Environment configuration
3. **`frontend_integration_tests.json`** - Flutter app integration tests
4. **`POSTMAN_TEST_GUIDE.md`** - This guide

## Prerequisites

### 1. Backend Server Setup
Ensure your Flask backend is running:

```bash
cd Backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

The server should be running on `http://localhost:5000`

### 2. Firebase Authentication
You'll need a valid Firebase JWT token for testing authenticated endpoints:

1. Set up Firebase project with Authentication
2. Generate a test user token
3. Use the token in the Postman environment

## Importing Collections to Postman

### Method 1: Direct Import
1. Open Postman
2. Click **Import** in the top left
3. Select the JSON files:
   - `postman_collection.json`
   - `postman_environment.json`
   - `frontend_integration_tests.json`
4. Click **Import**

### Method 2: Using Postman CLI (Newman)
```bash
# Install Newman globally
npm install -g newman

# Run tests
newman run postman_collection.json -e postman_environment.json
newman run frontend_integration_tests.json -e postman_environment.json
```

## Environment Setup

### Setting Firebase Token
1. In Postman, go to **Environments**
2. Select **HelaDry IoT Environment**
3. Set the `firebaseToken` variable with your Firebase JWT token
4. Save the environment

### Alternative: Using Environment Variables
You can also set the token via environment variables:
```bash
export FIREBASE_TOKEN="your_firebase_jwt_token_here"
```

## Running Tests

### Option 1: Manual Testing in Postman UI

#### Backend API Tests
1. Open the **HelaDry IoT API Collection**
2. Select the **HelaDry IoT Environment**
3. Run individual requests or use **Collection Runner**

#### Frontend Integration Tests
1. Open the **HelaDry Frontend Integration Tests** collection
2. Select the **HelaDry IoT Environment**
3. Run tests to simulate Flutter app behavior

### Option 2: Automated Testing with Collection Runner

1. In Postman, click **Runner** (bottom left)
2. Select your collection
3. Choose the environment
4. Configure test settings:
   - Iterations: 1
   - Delay: 1000ms between requests
   - Stop on failure: Enabled
5. Click **Run**

### Option 3: Command Line with Newman

```bash
# Run backend API tests
newman run postman_collection.json \
  -e postman_environment.json \
  --reporters cli,html \
  --reporter-html-export backend-test-report.html

# Run frontend integration tests
newman run frontend_integration_tests.json \
  -e postman_environment.json \
  --reporters cli,html \
  --reporter-html-export frontend-test-report.html

# Run all tests
newman run postman_collection.json frontend_integration_tests.json \
  -e postman_environment.json \
  --reporters cli,html \
  --reporter-html-export full-test-report.html
```

## Test Scenarios

### Backend API Tests
- **Health Check**: Verify API is running
- **Device Management**:
  - Register new devices
  - Start/stop drying sessions
  - Update temperature and fan speed
  - List user devices
- **Session Management**:
  - Get user sessions
  - Monitor session metrics
- **Error Handling**:
  - Invalid temperature ranges
  - Missing authentication
  - Invalid fan speeds

### Frontend Integration Tests
- **Flutter App Compatibility**:
  - Test with proper User-Agent headers
  - Verify response formats for Flutter widgets
  - Check response times for mobile UX
- **Real-time Control**:
  - Temperature adjustments
  - Fan speed control
  - Session management
- **Error Handling**:
  - Network errors
  - Authentication failures
  - Server errors

## Expected Test Results

### Success Criteria
- All health checks return 200 status
- Device registration returns 201 with proper response format
- Session operations return 200 with session details
- Error cases return appropriate 4xx status codes
- Response times are acceptable for mobile apps (< 3 seconds)

### Common Issues and Solutions

#### 1. Authentication Errors (401/403)
**Problem**: Tests fail with authentication errors
**Solution**: 
- Verify Firebase token is valid
- Check token hasn't expired
- Ensure Firebase project is properly configured

#### 2. Device Not Found Errors
**Problem**: Tests fail when trying to control non-existent devices
**Solution**:
- Run device registration test first
- Ensure device IDs are consistent across tests
- Check database connectivity

#### 3. Server Not Running
**Problem**: Connection refused errors
**Solution**:
- Start the Flask backend server
- Verify correct port (default: 5000)
- Check firewall settings

#### 4. Response Time Issues
**Problem**: Tests fail due to slow responses
**Solution**:
- Check server performance
- Verify database queries are optimized
- Consider increasing timeout values

## Continuous Integration

### GitHub Actions Example
Create `.github/workflows/postman-tests.yml`:

```yaml
name: Postman Tests
on: [push, pull_request]

jobs:
  postman-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '16'
      - name: Install Newman
        run: npm install -g newman
      - name: Run Postman Tests
        run: |
          newman run postman_collection.json \
            -e postman_environment.json \
            --reporters cli,html \
            --reporter-html-export test-report.html
      - name: Upload Test Results
        uses: actions/upload-artifact@v2
        with:
          name: test-results
          path: test-report.html
```

### Docker Testing
Create a test script for containerized testing:

```bash
#!/bin/bash
# test-with-docker.sh

# Start backend in Docker
docker-compose up -d backend

# Wait for backend to be ready
sleep 10

# Run tests
newman run postman_collection.json -e postman_environment.json

# Stop containers
docker-compose down
```

## Test Data Management

### Test Cleanup
The tests are designed to be idempotent and use unique device IDs. However, you may want to clean up test data:

```python
# cleanup_test_data.py
import requests

BASE_URL = "http://localhost:5000"
FIREBASE_TOKEN = "your_token_here"

def cleanup_test_devices():
    headers = {"Authorization": f"Bearer {FIREBASE_TOKEN}"}
    
    # Get all devices
    response = requests.get(f"{BASE_URL}/device/list", headers=headers)
    devices = response.json()
    
    # Delete test devices (those with 'test' in the name)
    for device in devices:
        if 'test' in device['device_name'].lower():
            print(f"Deleting test device: {device['device_name']}")
            # Add deletion logic if you have a delete endpoint

if __name__ == "__main__":
    cleanup_test_devices()
```

## Monitoring and Reporting

### Test Reports
Newman generates HTML reports that include:
- Test execution summary
- Individual test results
- Response times
- Error details

### Performance Monitoring
The tests include performance assertions:
- API response times < 3 seconds
- Real-time control response times < 1 second
- Health check response times < 2 seconds

## Troubleshooting

### Debug Mode
Enable debug logging in Newman:
```bash
newman run postman_collection.json -e postman_environment.json --verbose
```

### Individual Test Debugging
1. Run tests in Postman UI
2. Check the **Console** tab for detailed logs
3. Use **Pre-request Scripts** to log variables
4. Check **Tests** tab for assertion results

### Common Debug Scripts
Add to Pre-request Scripts:
```javascript
console.log('Firebase Token:', pm.environment.get('firebaseToken'));
console.log('Base URL:', pm.environment.get('baseUrl'));
console.log('Test Device ID:', pm.environment.get('testDeviceId'));
```

## Next Steps

1. **Run the tests** using the instructions above
2. **Review test results** and fix any failures
3. **Integrate with CI/CD** for automated testing
4. **Add more test scenarios** as your API evolves
5. **Monitor performance** and optimize slow endpoints

## Support

If you encounter issues:
1. Check the backend logs for errors
2. Verify Firebase authentication setup
3. Review test assertions for correctness
4. Check network connectivity
5. Consult Postman documentation for tool-specific issues

Happy testing! 🧪