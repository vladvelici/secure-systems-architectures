"""
This package is provided just as a simple layer for "storing" data. It simply
uses a dict to store all inboxes.

Every time you restart your server all data is lost.
"""

from collections import namedtuple

class MockDb:

    """ This is a very basic implementation, provided as an example only.

    All the data is stored in a dict, in memory. All data is lost when you
    restart the server.

    You will have to implement your own data storage mechanisms and methods to
    enable you to implement the full range of required featres for the
    assignment. You need to also think of data persistence: keep data even if
    the server restarts, and think about the security of data stored on disk."""

    def __init__(self):
        """initialize the mock database as empty"""
        self._inbox = {}

    def add_message_to_user(self, from_username, to_username, content):
        """ Adds given message to relevant user's inbox """

        msg = {
            "from_username": from_username,
            "to_username": to_username,
            "content": content,
            "read": False
        }
        if to_username in self._inbox:
            # user already exists (has an inbox, add the new message)
            self._inbox[to_username].append(msg)
        else:
            # this is the first message for this user, create a new array and
            # save the new message
            self._inbox[to_username] = [msg]

    def get_inbox_of(self, username):
        """Returns inbox of user (array of messages) or empty array if it doesn't exist."""
        return self._inbox.get(username, [])
