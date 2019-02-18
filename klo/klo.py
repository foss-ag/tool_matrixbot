#!/usr/bin/env python3

from matrix_client.client import MatrixClient
import os
from bs4 import BeautifulSoup
import requests

def find_room():
    html = requests.get("https://foss-ag.de/").text
    soup = BeautifulSoup(html, 'html.parser')
    dates = soup.find(id="ag-termine").next_sibling.find("ul").children
    for date in dates:
        print(date)

# Called when a message is recieved.
def on_message(room, event):
    if event['type'] == "m.room.message":
        if event['content']['msgtype'] == "m.text":
            print("{0}: {1}".format(event['sender'], event['content']['body']))

def main():
    client = MatrixClient("https://matrix.org")

    token = client.login(username="foss-ag_klo", password=os.environ['KLO_PW'])

    room.add_listener(on_message)
    client.start_listener_thread()

    while True:
        pass

if __name__ == "__main__":
    main()
