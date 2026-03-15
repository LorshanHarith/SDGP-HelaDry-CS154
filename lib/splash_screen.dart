import 'dart:async';
import 'package:flutter/material.dart';
import 'sign_in_screen.dart';

class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  static const Duration _splashDuration = Duration(seconds: 3);
  static const Color _backgroundColor = Color(0xFFF7FFF9);
  static const Color _iconColor = Color(0xFFFFC107);
  static const String _appTitle = 'Smart Solar Drying for Farmers';

  Timer? _timer;

  @override
  void initState() {
    super.initState();
    _timer = Timer(_splashDuration, _navigateToSignIn);
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  void _navigateToSignIn() {
    if (mounted) {
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(builder: (context) => const SignInScreen()),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: _backgroundColor,
      body: const Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              _appTitle,
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.w500),
            ),
            SizedBox(height: 20),
            Icon(Icons.wb_sunny_rounded, size: 120, color: _iconColor),
          ],
        ),
      ),
    );
  }
}