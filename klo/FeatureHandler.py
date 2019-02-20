class FeatureHandler:

    def __init__(self, room, client):
        """
        Initialize FeatureHandler.
        """
        # Matrix room and client
        self.__room = room
        self.__client = client
        # add on message listener to room and start listener thread
        room.add_listener(self.__on_message)
        client.start_listener_thread()
        # initialize list of known command
        self.__commands = []
        # initialize dictionary defining mapping from commands to features
        self.__features = {}

    @property
    def client(self):
        """
        :return:
            Matirx client
        """
        return self.__client

    @property
    def commands(self):
        """
        :return:
            List of known commands
        """
        return self.__commands

    @property
    def features(self):
        """
        :return:
            Dictionary containing commands and corresponding features.
        """
        return self.__features

    @property
    def room(self):
        """
        :return:
            Matrix room
        """
        return self.__room

    def add_feature(self, command, feature):
        """
        Add feature for specified command to room.

        :param command:
            String.
        :param feature:
            Callable. The feature will be called when the specified command occurs in the Matrix room.
            feature must take two arguments: 'sender' and 'message'.
        :raises KeyError:
            Raises KeyError if command is already defined.
        """
        if command in self.__commands:
            raise KeyError("Command %s already in use!" % command)

        self.__features[command] = feature

    def feature(self, command):
        """
        Get features that is mapped to the specified command.

        :param command:
            String.
        :return:
            Corresponding feature.
        :raises KeyError:
            Raises KeyError for unknown command.
        """
        return self.__features[command]

    def __on_message(self, room, event):
        """
        Handle message events in Matrix room and call feature functions if command was posted.

        :param room:
            Matrix room
        :param event:
            Current event in Matrix room.
        """
        if event['type'] == "m.room.message":
            # check if message is of type text
            if event['content']['msgtype'] == "m.text":
                # obtain sender and message
                sender = event['sender']
                msg = event['content']['body']
                # check if message starts with known command
                for command in self.__commands:
                    if msg.startswith(command):
                        # call corresponding feature
                        self.__features[command](sender=sender, message=msg, room=self.__room)
