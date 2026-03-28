import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_application_1/app/app.dart';
import 'package:flutter_application_1/theme/theme_controller.dart';
import 'package:flutter_application_1/services/session_store.dart';
import 'package:flutter_application_1/services/auth_service.dart';

void main() {
  testWidgets('TC006: Dashboard route shows main metrics UI', (WidgetTester tester) async {
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
    
    // Navigate to dashboard
    expect(find.text('Dashboard'), findsOneWidget);
    expect(find.text('Temperature'), findsOneWidget);
    expect(find.text('Humidity'), findsOneWidget);
    expect(find.text('Status'), findsOneWidget);
  });
}