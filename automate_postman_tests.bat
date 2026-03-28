@echo off
REM HelaDry Postman Test Automation Script
REM This script automates the entire testing process

echo 🚀 Starting HelaDry Postman Test Automation...
echo =================================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python and try again
    pause
    exit /b 1
)

REM Check if npm is installed (for Newman)
npm --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js/npm is not installed or not in PATH
    echo Please install Node.js and try again
    pause
    exit /b 1
)

REM Check if Newman is installed
newman --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 📦 Installing Newman globally...
    npm install -g newman
    if %errorlevel% neq 0 (
        echo ❌ Failed to install Newman
        pause
        exit /b 1
    )
)

echo ✅ Prerequisites check passed

REM Create reports directory
if not exist "test_reports" mkdir "test_reports"

REM Set timestamp for report files
set TIMESTAMP=%date:~-4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set TIMESTAMP=%TIMESTAMP: =0%

echo 📊 Test execution starting at %date% %time%
echo =================================================

REM Start backend server in background
echo 🔧 Starting backend server...
start "HelaDry Backend" cmd /c "cd Backend && python app.py"

REM Wait for server to start
echo ⏳ Waiting for backend server to start...
timeout /t 10 >nul

REM Check if server is running
echo 🔍 Checking server status...
python check_server.py
if %errorlevel% neq 0 (
    echo ❌ Backend server is not responding
    echo Please check the backend logs and try again
    pause
    exit /b 1
)

echo ✅ Backend server is running

REM Run backend API tests
echo 🧪 Running backend API tests...
newman run postman_collection.json -e postman_environment.json ^
    --reporters cli,html,json ^
    --reporter-html-export "test_reports\backend_tests_%TIMESTAMP%.html" ^
    --reporter-json-export "test_reports\backend_tests_%TIMESTAMP%.json"

if %errorlevel% neq 0 (
    echo ⚠️  Some backend tests failed - check the report
) else (
    echo ✅ Backend tests completed successfully
)

REM Run frontend integration tests
echo 📱 Running frontend integration tests...
newman run frontend_integration_tests.json -e postman_environment.json ^
    --reporters cli,html,json ^
    --reporter-html-export "test_reports\frontend_tests_%TIMESTAMP%.html" ^
    --reporter-json-export "test_reports\frontend_tests_%TIMESTAMP%.json"

if %errorlevel% neq 0 (
    echo ⚠️  Some frontend tests failed - check the report
) else (
    echo ✅ Frontend tests completed successfully
)

REM Generate summary report
echo 📋 Generating test summary...
python generate_test_summary.py "test_reports\backend_tests_%TIMESTAMP%.json" "test_reports\frontend_tests_%TIMESTAMP%.json" "test_reports\test_summary_%TIMESTAMP%.txt"

REM Cleanup: Stop backend server
echo 🛑 Stopping backend server...
taskkill /f /im python.exe >nul 2>&1

REM Open test reports
echo 📊 Opening test reports...
if exist "test_reports\backend_tests_%TIMESTAMP%.html" start "" "test_reports\backend_tests_%TIMESTAMP%.html"
if exist "test_reports\frontend_tests_%TIMESTAMP%.html" start "" "test_reports\frontend_tests_%TIMESTAMP%.html"

echo =================================================
echo 🎉 Test automation completed!
echo 📁 Reports saved to: test_reports/
echo 🕐 Completed at: %date% %time%
echo =================================================

pause