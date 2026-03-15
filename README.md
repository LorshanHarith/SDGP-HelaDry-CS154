# HelaDry - Smart Solar Drying System

A comprehensive IoT-based solar drying solution designed for Sri Lankan tea farmers, featuring a Flutter mobile application and ESP32 microcontroller integration for real-time monitoring and control of the drying process.

## 📋 Overview

HelaDry is a smart solar dehydrator system that helps tea farmers optimize their drying process through automated monitoring, data collection, and mobile app control. The system consists of:

- **Mobile App**: Flutter-based Android/iOS application for monitoring and controlling drying batches
- **IoT Device**: ESP32 microcontroller with sensors for weight measurement and environmental monitoring
- **Cloud Integration**: Firebase backend for data storage and real-time synchronization

## ✨ Features

### Mobile Application
- **Dashboard**: Real-time overview of drying batches and system status
- **Batch Management**: Start, monitor, and complete drying batches
- **Drying Reports**: Historical data and analytics for optimization
- **Drying Guide**: Educational content for best practices
- **User Authentication**: Secure sign-in system

### IoT Functionality
- **Weight Monitoring**: HX711 load cell sensor for precise weight measurements
- **Real-time Data**: Continuous monitoring and cloud synchronization
- **Automated Control**: Smart drying process management

## 🛠️ Technology Stack

### Mobile App
- **Framework**: Flutter (Dart)
- **UI**: Material Design 3
- **State Management**: Provider/Bloc (as implemented)

### IoT Device
- **Microcontroller**: ESP32 DevKit v1
- **Framework**: Arduino
- **Sensors**: HX711 Load Cell Amplifier
- **Communication**: WiFi + Firebase

### Backend
- **Database**: Firebase Firestore
- **Authentication**: Firebase Auth
- **Real-time Updates**: Firebase Realtime Database

## 🚀 Installation & Setup

### Prerequisites
- Flutter SDK (3.10.7 or later)
- Dart SDK
- Android Studio / VS Code with Flutter extensions
- PlatformIO IDE for ESP32 development
- ESP32 DevKit v1 board
- HX711 load cell and sensors

### Mobile App Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/asjath-admin/SDGP-HelaDry-CS154.git
   cd SDGP-HelaDry-CS154
   ```

2. Install Flutter dependencies:
   ```bash
   flutter pub get
   ```

3. Configure Firebase:
   - Add your `google-services.json` (Android) and `GoogleService-Info.plist` (iOS) to respective directories
   - Update Firebase configuration in the app

4. Run the app:
   ```bash
   flutter run
   ```

### IoT Device Setup
1. Install PlatformIO:
   ```bash
   pip install platformio
   ```

2. Open the project in PlatformIO IDE

3. Configure WiFi credentials in `src/main.cpp`:
   ```cpp
   const char* ssid = "YOUR_WIFI_SSID";
   const char* password = "YOUR_WIFI_PASSWORD";
   ```

4. Configure Firebase credentials:
   - Update API key and project details in the ESP32 code

5. Upload to ESP32:
   ```bash
   pio run -t upload
   ```

## 📱 Usage

1. **Launch the App**: Open the HelaDry app on your mobile device
2. **Sign In**: Authenticate with your farmer account
3. **Start Batch**: Begin a new drying batch with initial parameters
4. **Monitor Progress**: View real-time weight changes and environmental data
5. **Access Reports**: Review historical drying data and performance metrics
6. **Follow Guides**: Learn optimal drying techniques through the built-in guide

## 🔧 Development

### Project Structure
```
lib/
├── main.dart                 # App entry point
├── splash_screen.dart        # Splash screen
├── signin_screen.dart        # Authentication
├── dashboard_screen.dart     # Main dashboard
├── start_batch_screen.dart   # Batch initiation
├── drying_guide_screen.dart  # Educational content
└── drying_report_screen.dart # Reports and analytics

src/
└── main.cpp                 # ESP32 firmware

platformio.ini               # PlatformIO configuration
pubspec.yaml                 # Flutter dependencies
```

### Building for Production
- **Android**: `flutter build apk --release`
- **iOS**: `flutter build ios --release`
- **ESP32**: `pio run -t upload --environment esp32doit-devkit-v1`

## 🤝 Contributing

This project is part of CS154 Software Development Group Project. Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

- **Project**: SDGP-CS154
- **Institution**: IIT
- **Developers**: Frontend - Asjath and Kabi

## 📞 Support

For support and questions:
- Create an issue in this repository
- Contact the development team

---

**Note**: This is an academic project developed as part of the Software Development Group Project (SDGP) curriculum.
