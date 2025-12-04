#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}
"""in memory users here"""


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    return "OK"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """"demeli yoxluyuruq
    valid json olsun yoxsa 400
    username olsun yoxsa 400
    username artiq varsa 409
    successdise 201"""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    users[username] = user

    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    app.run()
