import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_application_1/app/app.dart';
import 'package:flutter_application_1/theme/theme_controller.dart';
import 'package:flutter_application_1/services/session_store.dart';
import 'package:flutter_application_1/services/auth_service.dart';

void main() {
  testWidgets('TC003: Login form validation shows errors for empty submit', (WidgetTester tester) async {
    await tester.pumpWidget(
      MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => ThemeController()),
          ChangeNotifierProvider(create: (_) => SessionStore()),
          ChangeNotifierProvider(create: (_) => AuthService()),
        ],
        child: const HelaDryApp(),
      ),
    );

    await tester.pumpAndSettle();
    
    // Try to submit empty form
    await tester.tap(find.text('Login'));
    await tester.pumpAndSettle();

    // Verify validation errors are shown
    expect(find.text('Please enter your email'), findsOneWidget);
    expect(find.text('Please enter your password'), findsOneWidget);
  });
}