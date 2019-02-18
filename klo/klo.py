#!/usr/bin/env python3

from FeatureExamples import FeatureExamples
from FeatureHandler import FeatureHandler
from matrix_client.client import MatrixClient
import os


def main():
    # connect to server and join room
    client = MatrixClient("https://matrix.org")
    token = client.login(username="foss-ag_klo", password=os.environ['KLO_PW'])
    room = client.join_room("#klotest:matrix.org")

    # create FeatureHandler
    fh = FeatureHandler(room, client)
    # add features to FeatureHandler that are called when the specified command is posted in the Matrix room
    fh.add_feature("!echo", FeatureExamples.echo)
    fh.add_feature("!CUPS", FeatureExamples.caps)

    # run script until it's stopped manually
    while True:
        pass


if __name__ == "__main__":
    main()
