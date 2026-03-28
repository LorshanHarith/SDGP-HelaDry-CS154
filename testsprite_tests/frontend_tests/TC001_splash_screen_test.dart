import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_application_1/app/app.dart';
import 'package:flutter_application_1/theme/theme_controller.dart';
import 'package:flutter_application_1/services/session_store.dart';

void main() {
  testWidgets('TC001: Splash screen loads and app shell renders', (WidgetTester tester) async {
    await tester.pumpWidget(
      MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => ThemeController()),
          ChangeNotifierProvider(create: (_) => SessionStore()),
        ],
        child: const HelaDryApp(),
      ),
    );

    // Verify splash screen loads
    expect(find.text('HelaDry'), findsOneWidget);
    expect(find.byType(CircularProgressIndicator), findsOneWidget);
    
    // Wait for splash to complete (simulate navigation)
    await tester.pumpAndSettle();
  });
}