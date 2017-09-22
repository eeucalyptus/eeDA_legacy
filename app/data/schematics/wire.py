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
from .schematicselement import SchematicsElement
from .wireconnector import WireConnector
from data.util import Vector2i

class Wire(SchematicsElement):
    def __init__(self, schematicspage):
        self.uuid = uuid.uuid1()
        self.schematicspage = schematicspage
        
        self.renderer = None
        self.connectors = [WireConnector(self), WireConnector(self)]
        self.points = []
        
    def setPoints(self, ary):
        self.points = ary
        
    def setConnectors(self, con1, con2):
        self.connectors = [con1, con2]
        
    def setRenderer(self, renderer):
        self.renderer = renderer
        
    def isConnected(self, connection):
        return self.connectors[0].isConnected(connection) | self.connectors[1].isConnected(connection)