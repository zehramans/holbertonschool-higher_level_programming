#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "giizli"
jwt = JWTManager(app)

users = {
<<<<<<< HEAD
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"}
}


=======
        "user1": {
            "username": "user1",
            "password": generate_password_hash("password"),
            "role": "user"
            },
        "admin1": {
            "username": "admin1",
            "password": generate_password_hash("password"),
            "role":"admin"}
        }
>>>>>>> 5521354bcf476de22496cf8da0989e40a5d02525
@app.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return False
    return check_password_hash(user["password"], password)

<<<<<<< HEAD

=======
>>>>>>> 5521354bcf476de22496cf8da0989e40a5d02525
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200

<<<<<<< HEAD

=======
>>>>>>> 5521354bcf476de22496cf8da0989e40a5d02525
@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = {
<<<<<<< HEAD
        "username": username,
        "role": user["role"]}

    tokena = create_access_token(identity=token)

    return jsonify({"access_token": tokena}), 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Accesss Granted"}), 200


@app.route("/admin-only")
@jwt_required()
def admin_only():
    user_now = get_jwt_identity()

    if user_now["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200


@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
=======
            "username": username,
            "role": user["role"]}

>>>>>>> 5521354bcf476de22496cf8da0989e40a5d02525
