'''

A Junction is the only connector that may have more than one
connection attached. This is supposed to lead to better
readability of the schematics, since every node involving
more than two adjacent nodes has to be represented by a junction.

'''

import uuid

from data.util import Vector2i
from .schematicsconnector import SchematicsConnector
from .schematicselement import SchematicsElement
import graphics

class Junction(SchematicsElement, SchematicsConnector):
    def __init__(self, page):
        SchematicsElement.__init__(self, page)
        self.uuid = str(uuid.uuid4())

        self.others = []
        self.pos = Vector2i()

    def initRenderer(self, gl):
        self.renderer = graphics.JunctionRenderer(self, gl)

    def fromConnector(connector):
        newJunction = Junction(connector.parent.page)
        newJunction.pos = connector.pos
        newJunction.connect(connector)
        return newJunction

    def isConnected(self, other):
        if other in self.others:
            return True
        else:
            return False

    def connect(self, other):
        self.others.append(other)


    def disconnect(self, other):
        if self.isConnected(other):
            self.others.remove(other)

    def isWireConnected(self, wire):
        for connector in wire.connectors:
            if self.isConnected(connector):
                return True
        return False

    def setPos(self, pos):
        self.pos = pos

    def setRenderer(self, renderer):
        self.renderer = renderer

    def __iadd__(self, connector):
        self.connect(connector)

    def __isub__(self, connector):
        self.disconnect(connector)

    def __repr__(self):
        other_uuids = []
        for other in self.others:
            other_uuids.append(other.uuid)

        return 'Junction (uuid=%s, pos=%s, others=%s)' % (self.uuid, self.pos, str(other_uuids))
