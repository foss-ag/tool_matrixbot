#!/usr/bin/env python3

from matrix_client.client import MatrixClient


# Called when a message is recieved.
def on_message(room, event):
    if event['type'] == "m.room.message":
        if event['content']['msgtype'] == "m.text":
            print("{0}: {1}".format(event['sender'], event['content']['body']))


client = MatrixClient("https://matrix.org")
# New user
#token = client.register_with_password(username="foobar", password="monkey")

# Existing user
token = client.login(username="foss-ag_klo", password="justklo")

#room = client.create_room("#klotest:matrix.org")
room = client.join_room("#klotest:matrix.org")
room.send_text("Hello!")

room.add_listener(on_message)
client.start_listener_thread()
