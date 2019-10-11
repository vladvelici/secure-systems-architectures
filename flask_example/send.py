#!/usr/bin/env python3

import argparse

# library to send HTTP requests easily
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--login-as", required=True, help="login username")
parser.add_argument("--to", required=True, help="recipient username")
parser.add_argument("--message", required=True, help="message")
args = parser.parse_args()


# This must be configured properly, perhaps via command line flags like in the server.py script.
server_url = "http://localhost:8000/"

# we send the request to "/send-message" URL
request_uri = server_url + "send-message"

# printing some debug info
print("request URI:", request_uri)
print()


params = {
    "auth_data": args.login_as,
    "recipient": args.to,
    "message": args.message
}


response = requests.post(request_uri, json=params)

print("status response:", response.status_code) # 200 means OK
print()
response_data = response.json()
print(response_data)
