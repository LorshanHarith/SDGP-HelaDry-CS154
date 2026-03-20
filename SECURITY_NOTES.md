# Security Notes

## Exposed Secrets Found
- During the inspection, hardcoded configuration files inside the firmware (`src/main.cpp` or older headers if any existed) often contained generic placeholders or specific Firebase RTDB URLs and secrets `WIFI_SSID`, `WIFI_PASSWORD`, `FIREBASE_HOST`, and `FIREBASE_AUTH`. 
- The Flutter application might contain hardcoded `firebase_options.dart` data.

## Mitigations Applied (or Recommended)
- **Dynamic Device Identity**: The device ID is no longer a static hardcoded `heladry_001` string which could cause telemetry collisions or injection vulnerabilities. It dynamically binds to the hardware's MAC address `HELADRY-MAC`.
- **Wi-Fi Provisioning**: Real SSIDs and Passwords are no longer flashed into the firmware source code. They are transmitted dynamically over the encrypted BLE channel.

## Actions Required (Manual Rotation & Checks)
- **Rotate Firebase Tokens**: If you ever uploaded any `FIREBASE_AUTH` secret or API key in your previous commits to GitHub, you MUST rotate that Firebase database secret immediately in the Firebase Console.
- **GitIgnore Rules**: Ensure `.env` files or secret headers (`secrets.h`) are added to `.gitignore`.
- **Firebase Options**: Do not expose your `firebase_options.dart` if the rules on your Realtime Database are set to completely public read/write. Implement Firebase Authentication or restrict RTDB rules to only allow writes to `/devices/$deviceId/` if the user is authenticated and linked.

## Local Configuration Example
Create a `secrets.example.h` for your firmware teammates:

```cpp
// secrets.example.h
#pragma once

#define FIREBASE_HOST "your-project.firebaseio.com"
#define FIREBASE_AUTH "your_database_secret_here"
```

*Note: Make sure to copy this to `secrets.h` locally and never track `secrets.h` in git.*
