#!/usr/bin/env python3

import argparse

from flask import Flask, request, jsonify

import mock_database_implementation as mockdb

app = Flask(__name__)

database = mockdb.MockDb()

@app.route('/send-message', methods=["POST"])
def send_message():
    incoming_data = request.json
    auth_data = incoming_data["auth_data"]
    sender_username = auth_data

    message = incoming_data["message"]
    recipient = incoming_data["recipient"]

    database.add_message_to_user(auth_data, recipient, message)
    return jsonify({"status": "ok", "msg": "Message sent"})

@app.route('/get-inbox', methods=["GET"])
def get_inbox():
    username = request.args["auth_data"]
    inbox = database.get_inbox_of(username)
    return jsonify(inbox)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1", help="IP for the HTTP server")
    parser.add_argument("--port", default="8000", help="port for the HTTP server")
    parser.add_argument("--production", action="store_true", default=False, help="disable debug mode")
    args = parser.parse_args()

    app.run(host=args.ip, port=args.port, debug=True)
