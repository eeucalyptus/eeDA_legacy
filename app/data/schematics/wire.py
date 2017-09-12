'''

The wire class holds points, forming a line. It consists 
of two end points (connectors) and multiple (or no) 
intermediate points. The connectors are either connected 
to a connection or not at all.
Wires have to be splitted to attach another connector to
them, then ending in a junction.

'''

import uuid

from .schematicsconnector import SchematicsConnector

class Wire:
    def __init__(self, schematicspage):
        self.uuid = uuid.uuid1()
        self.schematicspage = schematicspage
        
        self.renderer = None
        self.connectors = []
        self.points = []