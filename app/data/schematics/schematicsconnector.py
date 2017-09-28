'''

Abstract class for every connector in the schematics. Two
connectors can be connected to another connector.

'''

import uuid

class SchematicsConnector:
    def __init__(self, parent):
        self.uuid = uuid.uuid1()
        self.parent = parent
        self.connector = None

    def isConnected(self, other):
        if(self.connector == other):
            return True
        else:
            return False

    def connect(self, other):
        # disconnect from current
        if self.connector != None:
            self.connector.connector = None
        # connect to other
        self.connector = other
        other.connector = self
