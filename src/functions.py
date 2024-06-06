from src.Connection import Connection

class Functions:

    def __init__(self):
        self.connection = Connection()

    def connect(self):
        return self.connection.connect()