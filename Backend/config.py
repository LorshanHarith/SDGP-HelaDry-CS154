import os

class Config:
    DEBUG = True  # Change to False in production
    FIREBASE_CERT_PATH = os.getenv(
        "FIREBASE_CERT_PATH",
        "D:\\SDGP\\solar-dryer-iot-firebase-adminsdk-fbsvc-0e1fe49125.json"  # default for local dev
    )