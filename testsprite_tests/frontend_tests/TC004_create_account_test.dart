import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_application_1/app/app.dart';
import 'package:flutter_application_1/theme/theme_controller.dart';
import 'package:flutter_application_1/services/session_store.dart';
import 'package:flutter_application_1/services/auth_service.dart';

void main() {
  testWidgets('TC004: Create account screen reachable', (WidgetTester tester) async {
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
    
    // Navigate to create account
    await tester.tap(find.text('Create Account'));
    await tester.pumpAndSettle();

    // Verify registration form fields
    expect(find.text('Create Account'), findsOneWidget);
    expect(find.text('Email'), findsOneWidget);
    expect(find.text('Password'), findsOneWidget);
    expect(find.text('Confirm Password'), findsOneWidget);
    expect(find.byType(TextFormField), findsNWidgets(3));
  });
}