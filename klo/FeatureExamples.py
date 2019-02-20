from matrix_client.client import MatrixClient

class FeatureExamples:

    @staticmethod
    def echo(sender, message, room):
        """
        Print sender and message.

        :param sender:
            String.
        :param message:
            String.
        :param room:
            Matrix room
        """
        room.sendText(message)

    @staticmethod
    def caps(sender, message, room):
        """
        Message to upper case.

        :param sender:
            String.
        :param message:
            String.
        :param room:
            Matrix room.
        """
        print(message.upper())
