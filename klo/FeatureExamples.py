

class FeatureExamples:

    @staticmethod
    def echo(sender, message):
        """
        Print sender and message.

        :param sender:
            String.
        :param message:
            String.
        """
        print(sender, message)

    @staticmethod
    def caps(sender, message):
        """
        Message to upper case.

        :param sender:
            String.
        :param message:
            String.
        """
        print(message.upper())
