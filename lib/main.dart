import 'package:flutter/material.dart';
<<<<<<< Updated upstream
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';
import 'splash_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);

=======
import 'package:firebase_core/firebase_core.dart'; // Add this
import 'firebase_options.dart'; // Add this
import 'package:heladry/login_screen.dart';

void main() async {
  // 1. Mandatory for Firebase
  WidgetsFlutterBinding.ensureInitialized();

  // 2. Start the "Engine"
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);

>>>>>>> Stashed changes
  runApp(const SolarDryingApp());
}

class SolarDryingApp extends StatelessWidget {
  const SolarDryingApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'HelaDry', // Use your project name
      theme: ThemeData(
        useMaterial3: true,
        colorSchemeSeed: const Color(0xFF13B546), // Your HelaDry Green
      ),
      home: const LoginScreen(), // Directly points to Login now
    );
  }
}
