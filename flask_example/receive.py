#!/usr/bin/env python3

import argparse

# library to send HTTP requests easily
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--login-as", required=True, help="login username")
args = parser.parse_args()

# This must be configured properly, perhaps via command line flags like in the server.py script.
server_url = "http://localhost:8000/"

request_uri = server_url + "get-inbox"


response = requests.get(request_uri, {"auth_data": args.login_as})

print("status response:", response.status_code) # 200 means OK
print()
messages = response.json()
print(messages)
