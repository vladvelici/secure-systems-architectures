#!/usr/bin/env python3

import Pyro4

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--login-as", required=True, help="login username")
args = parser.parse_args()

server_proxy = Pyro4.Proxy("PYRONAME:message.server")    # use name server object lookup uri shortcut

# class AuthData:
#     def __init__(self, username):
#         self.username = username

# auth_data = AuthData(args.login_as)

result = server_proxy.read_inbox(args.login_as, new_only=False)
print(result)
