#!/usr/bin/env python3

import Pyro4

import mock_database_implementation as mockdb

# create a database instance, stored globally. In many cases this isn't a good structure for the code,
# but it is simple and will get our example going.

database = mockdb.MockDb()

@Pyro4.expose
class MessageServer:

    def send_message(self, auth_data, message, recipient):
        sender_username = auth_data
        database.add_message_to_user(sender_username, recipient, message)
        return "message sent OK"

    def read_inbox(self, auth_data, new_only):
        username = auth_data
        inbox = database.get_inbox_of(username)
        return inbox

# This code is just setting up the MessageServer class above as a Pyro service,
# so that clients can use it.

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(MessageServer)   # register the greeting maker as a Pyro object
ns.register("message.server", uri)

daemon.requestLoop()                   # start the event loop of the server to wait for calls
