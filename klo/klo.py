#!/usr/bin/env python3

from FeatureExamples import FeatureExamples
from FeatureHandler import FeatureHandler
from matrix_client.client import MatrixClient
import os
from bs4 import BeautifulSoup
import requests


def find_room(sender, message):
    html = requests.get("https://foss-ag.de/").text
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.find(id="ag-termine").find_next_sibling("div").find("ul").find("li").get_text().strip()
    return date


def main():
    # connect to server and join room
    client = MatrixClient("https://matrix.org")
    token = client.login(username="foss-ag_klo", password=os.environ['KLO_PW'])
    room = client.join_room("#klotest:matrix.org")

    # create FeatureHandler
    fh = FeatureHandler(room, client)
    # add features to FeatureHandler that are called when the specified command is posted in the Matrix room
    fh.add_feature("!echo", FeatureExamples.echo)
    fh.add_feature("!room", find_room)

    # run script until it's stopped manually
    while True:
        pass


if __name__ == "__main__":
    main()
