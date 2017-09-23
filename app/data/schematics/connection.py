'''

A Connection is the binding between two connectors. Every connector
may have one (multiple for junctions) connection attached, but they
may also be unconnected (connector.connection = None).

'''

import uuid

class Connection:
    def __init__(self, page, connector0, connector1):
        self.uuid = uuid.uuid1()
        self.page = page
        
        self.connector0 = connector0
        self.connector1 = connector1
        
    def CheckConnection(self):
        if (connector0.pos == connector1.pos):
            return False
            
        if (!connector0.isConnected(self)):
            return False
        if (!connector1.isConnected(self)):
            return False
            
        return True