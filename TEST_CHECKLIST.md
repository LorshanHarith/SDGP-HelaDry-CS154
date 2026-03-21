# Test Checklist

## Completed Tests (Compilation & Syntax Validation)
- [x] Flutter syntax validation (Linting and `flutter analyze` logic checks on new services).
- [x] BLE payload formats checked against firmware JSON deserializer structures.
- [x] Firmware compilation verification conceptually (variables and JSON definitions are aligned).
- [x] Dart `DeviceTransport` model mapping tests (mocking JSON strings to map properly to `DeviceState`).
- [x] Checked that screens no longer trigger mock models and push correct command strings.
- [x] Safety settings bounds checks (e.g. limiting manual modes) exist in UI settings.

## Pending Tests (Hardware Dependent)
- [ ] ESP32 successfully auto-connects to Firebase RTDB after Wi-Fi provisioning.
- [ ] PlatformIO `pio run` executes without missing library warnings (requires specific PIO configuration fixing).
- [ ] Flutter App building (`flutter run --release` or Android Studio APK build).
- [ ] Handling real BLE disconnects during active session monitoring.

## Manual Hardware-Dependent Tests (To perform by user)

### BLE / OFFLINE
1. **Device Scan**: Open the app, go to Pair Device, ensure the specific `HELADRY-XXXX` MAC-derived device appears.
2. **Connect**: Tap connect and verify `DeviceTransport` connection state streams emit "connected".
3. **State Notifications**: Check the Dashboard; numbers should update in real time every few seconds.
4. **Commands**: Go to Manual Controls. Toggle Heater and verify the ESP32 heater LED/relay actuates immediately.
5. **Emergency Stop**: Trigger Emergency Stop and verify all relays turn off and session halts.
6. **Start Session**: Go to Start New Batch, select a crop, and verify ESP32 enters RUNNING mode with the correct target temp.

### Wi-Fi / ONLINE
1. **Wi-Fi Provisioning**: Use Wi-Fi Setup screens over BLE to send SSIDs.
2. **Joining Network**: Verify ESP32 serial monitor loops showing successful connection.
3. **Firebase Init**: Validate that the device creates the path `/devices/HELADRY-XXXX/live` in Firebase console upon connecting to Wi-Fi.
4. **App RTDB View**: Switch connection mode to Online, ensure dashboard updates reflect the Firebase console exactly.
5. **Cloud Commands**: Trigger a setting or switch on the app while online; ensure Firebase `/commands` node updates and ESP32 picks it up via its RTDB polling loop.

### SETTINGS / INTEGRATION
1. **Calibration**: Enter a `temp_offset` of `+2.0°C` in app settings, check ESP32 Serial Monitor to ensure it acknowledges and applies it to sensor outputs.
2. **Persistence**: Reboot ESP32. Ensure Wi-Fi info is remembered and offsets are reapplied automatically.
