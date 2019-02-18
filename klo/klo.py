#!/usr/bin/env python3

from matrix_client.client import MatrixClient

client = MatrixClient("https://matrix.org")

# New user
#token = client.register_with_password(username="foobar", password="monkey")

# Existing user
token = client.login(username="foss-ag_klo", password="justklo")

#room = client.create_room("#klotest:matrix.org")
room = client.join_room("#klotest:matrix.org")
room.send_text("Hello!")