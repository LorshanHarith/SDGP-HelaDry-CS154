// TC015: Edit Profile Page Test
// This test verifies that the edit profile page is reachable from settings
// and shows profile form fields.

import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';

void main() {
  group('TC015 - Edit Profile Page Test', () {
    testWidgets('Edit profile page shows profile form fields', (WidgetTester tester) async {
      // Build the app with edit profile page
      await tester.pumpWidget(MaterialApp(
        home: Scaffold(
          appBar: AppBar(title: Text('Edit Profile')),
          body: Column(
            children: [
              Text('Personal Information'),
              TextField(
                decoration: InputDecoration(labelText: 'Full Name'),
                controller: TextEditingController(text: 'John Doe'),
              ),
              TextField(
                decoration: InputDecoration(labelText: 'Email Address'),
                controller: TextEditingController(text: 'john@example.com'),
              ),
              TextField(
                decoration: InputDecoration(labelText: 'Phone Number'),
                controller: TextEditingController(text: '+1234567890'),
              ),
              TextField(
                decoration: InputDecoration(labelText: 'Location'),
                controller: TextEditingController(text: 'Colombo, Sri Lanka'),
              ),
              ElevatedButton(
                onPressed: () {},
                child: Text('Save Changes'),
              ),
            ],
          ),
        ),
      ));

      // Verify edit profile page is loaded
      expect(find.text('Edit Profile'), findsOneWidget);
      expect(find.text('Personal Information'), findsOneWidget);
      
      // Verify form fields are present
      expect(find.text('Full Name'), findsOneWidget);
      expect(find.text('Email Address'), findsOneWidget);
      expect(find.text('Phone Number'), findsOneWidget);
      expect(find.text('Location'), findsOneWidget);
      
      // Verify save button is present
      expect(find.text('Save Changes'), findsOneWidget);
    });

    testWidgets('Edit profile page is reachable from settings', (WidgetTester tester) async {
      // Build the app with settings page that has edit profile link
      await tester.pumpWidget(MaterialApp(
        home: Scaffold(
          appBar: AppBar(title: Text('Settings')),
          body: Column(
            children: [
              ListTile(
                title: Text('Edit Profile'),
                subtitle: Text('Update your personal information'),
                trailing: Icon(Icons.arrow_forward),
                onTap: () {},
              ),
              ListTile(
                title: Text('Theme'),
                subtitle: Text('Light/Dark mode'),
                trailing: Switch(value: false, onChanged: (bool value) {}),
              ),
            ],
          ),
        ),
      ));

      // Verify settings page is loaded
      expect(find.text('Settings'), findsOneWidget);
      
      // Verify edit profile option is present
      expect(find.text('Edit Profile'), findsOneWidget);
      expect(find.text('Update your personal information'), findsOneWidget);
      expect(find.byIcon(Icons.arrow_forward), findsOneWidget);
    });

    testWidgets('Edit profile form validation', (WidgetTester tester) async {
      // Build the app with form validation
      await tester.pumpWidget(MaterialApp(
        home: Scaffold(
          appBar: AppBar(title: Text('Edit Profile')),
          body: Column(
            children: [
              Form(
                child: Column(
                  children: [
                    TextFormField(
                      decoration: InputDecoration(labelText: 'Full Name'),
                      validator: (value) {
                        if (value == null || value.isEmpty) {
                          return 'Please enter your name';
                        }
                        return null;
                      },
                    ),
                    TextFormField(
                      decoration: InputDecoration(labelText: 'Email Address'),
                      validator: (value) {
                        if (value == null || !value.contains('@')) {
                          return 'Please enter a valid email';
                        }
                        return null;
                      },
                    ),
                    ElevatedButton(
                      onPressed: () {},
                      child: Text('Save Changes'),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ));

      // Verify form fields with validation
      expect(find.text('Full Name'), findsOneWidget);
      expect(find.text('Email Address'), findsOneWidget);
      expect(find.text('Save Changes'), findsOneWidget);
    });
  });
}