import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_database/firebase_database.dart';

class DeviceLinkService {
  final FirebaseAuth _auth = FirebaseAuth.instance;
  final FirebaseDatabase _db = FirebaseDatabase.instance;

  /// Links a device to the currently logged-in user.
  /// Writes:
  /// users/{uid}/devices/{deviceId} = true
  /// devices/{deviceId}/owner = uid
  Future<void> linkDeviceToCurrentUser(String deviceId) async {
    final user = _auth.currentUser;
    if (user == null) {
      throw Exception("No logged-in user found.");
    }

    final firebaseUid = user.uid;

    final Map<String, Object?> updates = {
      'users/$uid/devices/$deviceId': true,
      'devices/$deviceId/owner': uid,
    };

    await _db.ref().update(updates);
  }

  /// Optional helper: check device owner
  Future<String?> getDeviceOwner(String deviceId) async {
    final snap = await _db.ref('devices/$deviceId/owner').get();
    if (!snap.exists) return null;
    return snap.value?.toString();
  }
}