# Implementation Summary: HelaDry Integration

## Overview
This document summarizes the end-to-end integration between the Flutter mobile UI and the ESP32 firmware for the HelaDry project, supporting both offline (BLE) and online (Firebase) modes.

## What Was Changed

### Firmware Changes (`src/main.cpp`)
- **Device Identity**: Transformed the hardcoded `DEVICE_ID` into a dynamic device identity (`bleDeviceName`) based on the base MAC address.
- **BLE Service/Characteristics**: 
  - Exposed live `telemetry` JSON stream on `STATE_CHAR_UUID`.
  - Added ACK characteristics (`ACK_CHAR_UUID`) for sending Wi-Fi scan results and command acknowledgments.
  - Implemented command parsing on `COMMAND_CHAR_UUID` for `SCAN_WIFI`, `SET_MANUAL_OUTPUTS` (with offsets), and more.
- **Firebase/Wi-Fi Provisioning**: 
  - When provisioned dynamically, Firebase connects after a successful Wi-Fi link. 
  - `temp_offset` and `humidity_offset` polling mechanisms were added from `/config`.

### Flutter UI/Services (`lib/`)
- Added `flutter_reactive_ble`, `firebase_core`, `firebase_database`, and `permission_handler`.
- Configured Android/iOS manifests for BLE and Location. 
- Refactored away mock services into real data handling layers:
  - **`BleDeviceService`**: Handles scanning, connection, and data subscriptions via BLE.
  - **`FirebaseDeviceService`**: Handles Firebase listeners and online telemetry maps.
  - **`DeviceTransport`**: Singleton repository that acts as an abstraction over BLE and Firebase, exposing `stateStream` and `ackStream`. It parses varying payload formats into a unified `DeviceState` object.
- **Screen Wiring**:
  - `PairDevicePage`: Scans for the `HELADRY-*` device and connects locally via BLE.
  - `WifiSetupBleStepXPage`: Uses BLE transport to request Wi-Fi scanning (`SCAN_WIFI`) and send chosen network credentials (`SET_WIFI_CREDS`).
  - `DashboardPage`: Replaced mock metrics with Stream-based subscription to `DeviceTransport`.
  - `ManualControlsPage`: Sends real commands (`SET_MANUAL_OUTPUTS` and `EMERGENCY_STOP`) through the active transport.
  - `StartNewBatchPage`: Configured to send `START_SESSION` commands containing crop types and target parameters.

## Architecture Decisions
- **Unified Transport Layer**: Developed a `DeviceTransport` singleton. This abstracts the differences between offline payload structures and online schema structures to prevent `Dashboard` or UI models from tightly coupling to BLE or RTDB specifics.
- **Async Firmware Comm (BLE)**: Wi-Fi scanning is async on the firmware; rather than holding a BLE write hostage, we return results via a separate ACK characteristic notification which `DeviceTransport` streams via `ackStream`.

## Known Limitations
- The firmware still requires some dependencies to build completely through standard PIO (e.g. `Firebase_ESP_Client` local resolution). 
- Disconnection / Reconnection resilience inside Flutter could be enhanced with exponential backoffs.

## Setup & Run Steps
1. Make sure Flutter SDK is installed and configured correctly running `flutter doctor`.
2. Update the Firebase credentials if appropriate (none provided natively here).
3. Connect ESP32, build the firmware with `pio run -t upload`.
4. Deploy flutter app using `flutter run` on a real physical mobile device. Emulator BLE will not function reliably.
