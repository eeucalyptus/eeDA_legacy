'''

Abstract class for every connector in the schematics. Two
connectors can be connected using a connection.

'''

class SchematicsConnector:
    def isConnected(self, connection):
        if(self.connection == connection):
            return True
        else:
            return False
        
    def connect(self, connection):
        self.connection = connection