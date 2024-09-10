#!/usr/bin/env python3
"""The Flask app"""

from auth import Auth
from flask import Flask, jsonify, Response, request, abort


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def welcome() -> Response:
    """This method contsaisn the GET route for /.
    Returns:
        JSON: the payload."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def users():
    """Registers a new user"""
    # Get the email and password from form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Check for validity of provided email and password
    if not email or not password:
        abort(400, description="Missing email or password")

    try:
        # Attempt to register the new user
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        # If user exists, return error message
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
