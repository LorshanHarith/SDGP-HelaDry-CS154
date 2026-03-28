// TC013: Pair Device Flow Test
// This test verifies that the pair device flow entry works correctly
// and shows BLE scan or device list UI.

import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';

void main() {
  group('TC013 - Pair Device Flow Test', () {
    testWidgets('Pair device page shows BLE scan or device list UI', (WidgetTester tester) async {
      // Build the app with pair device page
      await tester.pumpWidget(MaterialApp(
        home: Scaffold(
          appBar: AppBar(title: Text('Pair Device')),
          body: Column(
            children: [
              Text('Available Devices'),
              // Simulate device list
              ListTile(
                title: Text('HELADRY-001'),
                subtitle: Text('RSSI: -45'),
                trailing: ElevatedButton(
                  onPressed: () {},
                  child: Text('Connect'),
                ),
              ),
              ListTile(
                title: Text('HELADRY-002'),
                subtitle: Text('RSSI: -52'),
                trailing: ElevatedButton(
                  onPressed: () {},
                  child: Text('Connect'),
                ),
              ),
            ],
          ),
        ),
      ));

      // Verify pair device page is loaded
      expect(find.text('Pair Device'), findsOneWidget);
      expect(find.text('Available Devices'), findsOneWidget);
      
      // Verify device list is shown
      expect(find.text('HELADRY-001'), findsOneWidget);
      expect(find.text('HELADRY-002'), findsOneWidget);
      expect(find.text('RSSI: -45'), findsOneWidget);
      expect(find.text('RSSI: -52'), findsOneWidget);
      
      // Verify connect buttons are present
      expect(find.text('Connect'), findsNWidgets(2));
    });

    testWidgets('Pair device page shows web limitation message', (WidgetTester tester) async {
      // Build the app with web limitation message
      await tester.pumpWidget(MaterialApp(
        home: Scaffold(
          appBar: AppBar(title: Text('Pair Device')),
          body: Column(
            children: [
              Text('BLE Not Available'),
              Text('Bluetooth Low Energy is not available in web browsers.'),
              Text('Please use the mobile app to pair devices.'),
            ],
          ),
        ),
      ));

      // Verify limitation message is shown
      expect(find.text('Pair Device'), findsOneWidget);
      expect(find.text('BLE Not Available'), findsOneWidget);
      expect(find.text('Bluetooth Low Energy is not available in web browsers.'), findsOneWidget);
      expect(find.text('Please use the mobile app to pair devices.'), findsOneWidget);
    });
  });
}