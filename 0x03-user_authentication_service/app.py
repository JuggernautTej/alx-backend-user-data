#!/usr/bin/env python3
"""The Flask app"""

from flask import Flask, jsonify, Response


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def welcome() -> Response:
    """This method contsaisn the GET route for /.
    Returns:
        JSON: the payload."""
    p_load = {"message": "Bienvenue"}
    return jsonify(p_load)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
