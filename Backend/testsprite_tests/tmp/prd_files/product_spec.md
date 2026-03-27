# Product Specification Document (PRD)
**Project Name:** HelaDry - Solar-Powered IoT Hybrid Dehydrator System
**Platforms:** Android, iOS, Web (Flutter)
**Firmware:** ESP32 DOIT DevKit V1

## 1. Overview
HelaDry is a mobile companion app for a solar-powered food dehydrator machine. It empowers farmers and users to monitor and control their dehydrator machine in real-time, track drying batches, and access crop-specific guidelines.

## 2. Target Audience
- Local farmers and home users seeking efficient food dehydration.
- Users who need both physical control (offline/Bluetooth) and remote monitoring (online/Wi-Fi).

## 3. Core Features

### 3.1 Authentication & User Management
* **Splash Screen:** Animated logo with automatic login check.
* **Account Creation/Login:** Email/Phone and Password authentication with form validations.
* **Profile Management:** Edit profile details (Name, Email) and logout functionality.

### 3.2 Connectivity Modes
* **Offline Mode (BLE):**
  * Direct Bluetooth control without internet dependency.
  * Scans and pairs with local devices (e.g., `HELADRY-XXXX`).
* **Online Mode (Wi-Fi/Cloud):**
  * Wi-Fi provisioning via BLE (3-step wizard: Scan networks, Enter password, Confirm).
  * Cloud sync via Firebase Realtime Database for remote remote monitoring.

### 3.3 Dashboard & Live Metrics
Central hub displaying:
* **Active Batch Card:** Status of the current drying batch with a shortcut to start a new one.
* **Live Telemetry:** 
  * Temperature (°C/°F)
  * Humidity (%)
  * Fan Speed (0-100%)
  * Heater Status (ON/OFF)
  * Battery Voltage
  * Solar Charging Status

### 3.4 Manual Controls
Direct hardware control interface:
* **Fan Speed:** Slider (0-100%).
* **Target Temperature:** Slider (30°C - 80°C).
* **Heater:** Manual ON/OFF toggle.
* **Emergency Stop:** Instantly halts operations (Fan 0%, Heater OFF) for safety.

### 3.5 Batch Management
* **Start New Batch:** Form to select crop type, tray count, and weight. Auto-fills target parameters based on the crop guide.
* **Drying Guide:** Database of 7 supported crops (Mango, Jackfruit, Tomato, Banana, Papaya, Chili, Grape) with recommended temps, durations, slice thickness, prep steps, and tips.
* **My Records:** Historical log of all active and completed drying batches.

### 3.6 Settings & Configuration
* **Sensor Calibration:** Adjust temperature and humidity offsets.
* **Preferences:** Toggle Temperature Units (Celsius/Fahrenheit), Light/Dark themes.
* **Alerts:** Over-temperature, low battery, and sensor fault notifications.
* **Device Info:** Unpair, restart, or check firmware versions.

## 4. Technical Architecture
* **Frontend:** Built with Flutter (Dart). State managed using `Provider` (`ChangeNotifier`). Features custom Light/Dark theme scaling.
* **Backend:** Python/Flask API interfacing with Firebase services.
* **Firmware:** Written in C++ (PlatformIO) for ESP32. Handles HX711 load cell sensors, BLE GATT services, and Firebase RTDB syncing.

## 5. Non-Functional Requirements
* **Performance:** Real-time metrics UI should update seamlessly via streams (BLE or Firebase).
* **Usability:** High-contrast Dark/Light modes for outdoor farm visibility.
* **Reliability:** Firmware must auto-reconnect to Wi-Fi/Firebase and gracefully handle network drops.

## 6. Testing Scenarios (Acceptance Criteria)
1. **Connectivity:** Ensure BLE provisioning successfully pushes Wi-Fi credentials to ESP32 and ESP32 connects to Firebase.
2. **Telemetry:** Verify UI metrics map accurately to Firebase `/current_weight` and BLE telemetry payloads.
3. **Controls:** Verify that triggering 'Emergency Stop' immediately alters ESP32 relay states.
4. **Offline Resilience:** App must function and control the dehydrator locally when internet drops.
