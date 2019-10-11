#!/usr/bin/env python3

import Pyro4

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--login-as", required=True, help="login username")
parser.add_argument("--to", required=True, help="recipient username")
parser.add_argument("--message", required=True, help="message")
args = parser.parse_args()

server_proxy = Pyro4.Proxy("PYRONAME:message.server")    # use name server object lookup uri shortcut

result = server_proxy.send_message(auth_data=args.login_as, message=args.message, recipient=args.to)
print(result)
