import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:firebase_auth/firebase_auth.dart';
import '../app/app_config.dart';

class DeviceSetupService {
  static Future<void> registerDeviceWithBackend(String receivedIdFromBluetooth) async {
    try {
      final user = FirebaseAuth.instance.currentUser;
      if (user == null) return;

      final token = await user.getIdToken(true);
      final baseUrl = AppConfig.baseUrl;

      final response = await http.post(
        Uri.parse('$baseUrl/device/register'),
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer $token",
        },
        body: jsonEncode({
          "device_id": receivedIdFromBluetooth,
          "device_name": "My HelaDry Device", 
        }),
      );

      if (response.statusCode == 201 || response.statusCode == 200) {
        print("Registration Successful: Device $receivedIdFromBluetooth is now linked.");
      } else {
        print("Registration Failed: ${response.body}");
      }
    } catch (e) {
      print("Error registering device: $e");
    }
  }
}