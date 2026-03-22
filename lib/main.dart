import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:firebase_core/firebase_core.dart';
import 'theme/theme_controller.dart';
import 'services/session_store.dart';
import 'services/ble_service.dart';
import 'services/firebase_service.dart';
import 'services/auth_service.dart';
import 'services/device_claim_service.dart';
import 'services/api_service.dart';
import 'services/connection_controller.dart';
import 'app/app.dart';
import 'firebase_options.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  
  final bleService = BleService();
  final fbService  = FirebaseDeviceService();
  final apiService = ApiService();
  final connCtrl   = ConnectionController(ble: bleService, fb: fbService, api: apiService);
  final authService = AuthService();
  final deviceClaimService = DeviceClaimService();

  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => ThemeController()),
        ChangeNotifierProvider(create: (_) => SessionStore()),
        ChangeNotifierProvider.value(value: bleService),
        ChangeNotifierProvider.value(value: fbService),
        Provider.value(value: apiService),
        ChangeNotifierProvider.value(value: connCtrl),
        ChangeNotifierProvider.value(value: authService),
        Provider.value(value: deviceClaimService),
      ],
      child: const HelaDryApp(),
    ),
  );
}