from flask import Blueprint, request, jsonify
from app.services.auth_service import register_user, login_user
from app import limiter

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
@limiter.limit("10 per minute")
def register():
    data = request.get_json()
    if not data or not all(k in data for k in ("username", "email", "password")):
        return jsonify({"error": "username, email, and password are required"}), 400

    user, error = register_user(data["username"], data["email"], data["password"])
    if error:
        return jsonify({"error": error}), 409

    return jsonify({"message": "User registered successfully", "user": user.to_dict()}), 201

@auth_bp.route("/login", methods=["POST"])
@limiter.limit("20 per minute")
def login():
    data = request.get_json()
    if not data or not all(k in data for k in ("email", "password")):
        return jsonify({"error": "email and password are required"}), 400

    user, token, error = login_user(data["email"], data["password"])
    if error:
        return jsonify({"error": error}), 401

    return jsonify({
        "message": "Login successful",
        "token": token,
        "user": user.to_dict()
    }), 200