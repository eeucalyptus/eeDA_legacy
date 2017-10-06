'''

Abstract class for every connector in the schematics. Two
connectors can be connected to another connector.

'''

import uuid

class SchematicsConnector:
    def __init__(self, parent):
        self.uuid = str(uuid.uuid4())
        self.parent = parent
        self.other = None

    def isConnected(self, other):
        if(self.other == other):
            return True
        else:
            return False

    def connect(self, other):
        # disconnect from current
        if self.other != None:
            self.other.connector = None
        # connect to other
        self.other = other
        other.connector = self
