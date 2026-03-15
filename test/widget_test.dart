// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:heladry/dashboard_screen.dart';

void main() {
  testWidgets('Dashboard screen displays welcome message', (WidgetTester tester) async {
    // Build the dashboard screen directly for testing
    await tester.pumpWidget(
      const MaterialApp(
        home: DashboardScreen(),
      ),
    );

    // Verify welcome text is displayed
    expect(find.text('Welcome,'), findsOneWidget);
    expect(find.text('Farmer!'), findsOneWidget);
    expect(find.text('Solar Dehydrator Dashboard'), findsOneWidget);
    expect(find.byIcon(Icons.wb_sunny), findsOneWidget);
  });
}
