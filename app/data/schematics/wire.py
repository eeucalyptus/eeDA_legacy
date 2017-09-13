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
from data.util import Vector2i

class Wire:
    def __init__(self, schematicspage):
        self.uuid = uuid.uuid1()
        self.schematicspage = schematicspage
        
        self.renderer = None
        self.connectors = [None, None]
        self.points = []
        
    def setPoints(self, ary):
        for point in ary:
            if not type(point) == Vector2i:
                raise TypeError('We done fucked up')
        self.points = ary
        
    def setConnectors(self, con1, con2):
        self.connectors = [con1, con2]
        
    def setRenderer(self, renderer):
        self.renderer = renderer