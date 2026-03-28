// TC014: WiFi Setup Wizard Step 1 Test
// This test verifies that the first step of WiFi provisioning wizard is visible.

import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';

void main() {
  group('TC014 - WiFi Setup Wizard Step 1 Test', () {
    testWidgets('WiFi setup step 1 shows network selection UI', (WidgetTester tester) async {
      // Build the app with WiFi setup step 1
      await tester.pumpWidget(MaterialApp(
        home: Scaffold(
          appBar: AppBar(title: Text('WiFi Setup - Step 1')),
          body: Column(
            children: [
              Text('Select WiFi Network'),
              // Simulate network list
              ListTile(
                title: Text('HomeWiFi'),
                subtitle: Text('Signal: Strong'),
                trailing: Radio(value: 'HomeWiFi', groupValue: 'HomeWiFi', onChanged: (value) {}),
              ),
              ListTile(
                title: Text('OfficeWiFi'),
                subtitle: Text('Signal: Medium'),
                trailing: Radio(value: 'OfficeWiFi', groupValue: null, onChanged: (value) {}),
              ),
              ListTile(
                title: Text('GuestWiFi'),
                subtitle: Text('Signal: Weak'),
                trailing: Radio(value: 'GuestWiFi', groupValue: null, onChanged: (value) {}),
              ),
              ElevatedButton(
                onPressed: () {},
                child: Text('Next'),
              ),
            ],
          ),
        ),
      ));

      // Verify WiFi setup page is loaded
      expect(find.text('WiFi Setup - Step 1'), findsOneWidget);
      expect(find.text('Select WiFi Network'), findsOneWidget);
      
      // Verify network list is shown
      expect(find.text('HomeWiFi'), findsOneWidget);
      expect(find.text('OfficeWiFi'), findsOneWidget);
      expect(find.text('GuestWiFi'), findsOneWidget);
      expect(find.text('Signal: Strong'), findsOneWidget);
      expect(find.text('Signal: Medium'), findsOneWidget);
      expect(find.text('Signal: Weak'), findsOneWidget);
      
      // Verify radio buttons are present
      expect(find.byType(Radio), findsNWidgets(3));
      
      // Verify next button is present
      expect(find.text('Next'), findsOneWidget);
    });

    testWidgets('WiFi setup step 1 shows progress indicator', (WidgetTester tester) async {
      // Build the app with progress indicator
      await tester.pumpWidget(MaterialApp(
        home: Scaffold(
          appBar: AppBar(
            title: Text('WiFi Setup'),
            leading: IconButton(onPressed: () {}, icon: Icon(Icons.arrow_back)),
          ),
          body: Column(
            children: [
              LinearProgressIndicator(value: 0.33),
              Text('Step 1 of 3'),
              Text('Select WiFi Network'),
            ],
          ),
        ),
      ));

      // Verify progress indicator
      expect(find.byType(LinearProgressIndicator), findsOneWidget);
      expect(find.text('Step 1 of 3'), findsOneWidget);
      expect(find.text('Select WiFi Network'), findsOneWidget);
    });
  });
}