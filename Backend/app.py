from flask import Flask, request, jsonify
from functools import wraps
import firebase_admin
from firebase_admin import credentials, auth

app = Flask(__name__)

cred = credentials.Certificate("")
firebase_admin.initialize_app(cred)

def firebase_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "Token missing"}), 403

        try:
            token = auth_header.split(" ")[1]
            decoded_token = auth.verify_id_token(token)
            request.user = decoded_token
        except:
            return jsonify({"error": "Invalid Firebase token"}), 403

        return f(*args, **kwargs)

    return wrapper

