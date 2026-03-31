from functools import wraps
from flask import request, jsonify

TOKEN = "123456"

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token or token != TOKEN:
            return jsonify({"error": "Unauthorized"}), 401

        return f(*args, **kwargs)
    
    return decorated