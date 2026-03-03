from firebase_admin import db
from datetime import datetime, timezone


def start_device(user_id, device_id, temperature):
    try:
        # Basic validation
        if temperature is None:
            return {"error": "Temperature is required"}

        if not isinstance(temperature, (int, float)):
            return {"error": "Temperature must be a number"}

        ref = db.reference(f"devices/{device_id}")
        device = ref.get()

        if not device:
            return {"error": "Device not found"}

        if device.get("owner") != user_id:
            return {"error": "Unauthorized access to device"}

        ref.update({
            "status": "running",
            "temperature": temperature,
            "last_command": {
                "type": "start",
                "value": temperature,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "source": "cloud"
            },
            "updated_at": datetime.now(timezone.utc).isoformat()
        })

        return {
            "message": "Device started",
            "device_id": device_id,
            "temperature": temperature
        }

    except Exception as e:
        raise Exception(f"Failed to start device: {str(e)}")


def stop_device(user_id, device_id):
    try:
        ref = db.reference(f"devices/{device_id}")
        device = ref.get()

        if not device:
            return {"error": "Device not found"}

        if device.get("owner") != user_id:
            return {"error": "Unauthorized access to device"}

        ref.update({
            "status": "stopped",
            "last_command": {
                "type": "stop",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "source": "cloud"
            },
            "updated_at": datetime.now(timezone.utc).isoformat()
        })

        return {
            "message": "Device stopped",
            "device_id": device_id
        }

    except Exception as e:
        raise Exception(f"Failed to stop device: {str(e)}")