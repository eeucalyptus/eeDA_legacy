'''

A Connection is the binding between two connectors. Every connector
may have one (multiple for junctions) connection attached, but they 
may also be unconnected (connector.connection = None).

'''

import uuid

class Connection:
    def __init__(self, schematicspage, connector0, connector1):
        self.uuid = uuid.uuid1()
        self.schematicspage = schematicspage
        
        self.connector0 = connector0
        self.connector1 = connector1
        
    def CheckConnection(self):
        pos0 = connector0.pos
        pos1 = connector1.pos
        
        return (pos0 == pos1)