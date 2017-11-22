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
import graphics.drawables.schematics
from graphics.common import eeDAcolor

class Wire(SchematicsElement):
    def __init__(self, page):
        super().__init__(page)
        self.uuid = str(uuid.uuid4())
        self.connectors = [WireConnector(self), WireConnector(self)]
        self.points = []
        self.style = {'width': 5, 'color': eeDAcolor.WIRE}

    def initDrawable(self, gl):
        self.drawable = graphics.drawables.schematics.WireDrawable(self, gl)

    def setPoints(self, ary):
        self.points = ary

    def isConnected(self, connection):
        return self.connectors[0].isConnected(connection) | self.connectors[1].isConnected(connection)

    def __repr__(self):
        return 'Wire (uuid=%s, numPoints=%d, start=%s, end=%s)' % (self.uuid, len(self.points)+2, str(self.connectors[0].pos), str(self.connectors[1].pos))

    def selected(self, pos):
        lastPoint = self.connectors[0].pos
        for point in (self.points + [self.connectors[1].pos]):
            if Wire.lineSegmentDistance(pos, lastPoint, point) < self.style['width'] / 2.0:
                return True
            lastPoint = point

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


    def associativeRepresentation(self):
        asRepr =  {}

        asRepr['type'] = 'wire'
        asRepr['uuid'] = self.uuid
        asRepr['connectors'] = []
        asRepr['connectors'].append(self.connectors[0].associativeRepresentation())
        asRepr['connectors'].append(self.connectors[1].associativeRepresentation())

        if self.points:
            asRepr['points'] = []
            for point in self.points:
                asRepr['points'].append(point.associativeRepresentation())

        return asRepr

    def fromAssociativeRepresentation(asRepr, parent):
        wire = Wire(parent)

        wire.uuid = asRepr.get('uuid', None)
        wire.points = []
        for pointRepr in asRepr.get('points', []):
            wire.points.append(Vector2i.fromAssociativeRepresentation(pointRepr))
        wire.connectors[0] = WireConnector.fromAssociativeRepresentation(asRepr.get('connectors', [])[0], wire)
        wire.connectors[1] = WireConnector.fromAssociativeRepresentation(asRepr.get('connectors', [])[1], wire)

        return wire
