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
from graphics.common import eeDAcolor

class Wire(SchematicsElement):
    def __init__(self, page):
        super().__init__(page)
        self.uuid = uuid.uuid1()
        self.style = {'width' : 4.0, 'color' : eeDAcolor.WIRE}
        
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
        
    def selected(self, pos):
        for i in range(len(self.points) - 1):
            p1 = self.points[i]
            p2 = self.points[i + 1]
            
            if Wire.lineSegmentDistance(pos, p1, p2) < self.style['width'] / 2.0:
                return True
        return False
    def lineSegmentDistance(p, p1, p2):
        segment = p2 - p1
        vector = p - p1
        dist1 = segment.dot(vector)
        if dist1 <= 0:
            return (p - p1).euDist()
        dist2 = segment.dot(segment)
        if dist2 <= dist1:
            return (p - p2).euDist()
        factor = dist1 / dist2
        projectionPoint = p1 + segment * factor
        return (p - projectionPoint).euDist()