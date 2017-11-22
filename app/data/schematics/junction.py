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
import graphics.drawables.schematics

class Junction(SchematicsElement, SchematicsConnector):
    def __init__(self, page):
        SchematicsElement.__init__(self, page)
        self.uuid = str(uuid.uuid4())

        self.others = []
        self._otherUuids = None
        self.pos = Vector2i()

    def initDrawable(self, gl):
        self.drawable = graphics.drawables.schematics.JunctionDrawable(self, gl)

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
        self.drawable = renderer

    def __iadd__(self, connector):
        self.connect(connector)

    def __isub__(self, connector):
        self.disconnect(connector)

    def __repr__(self):
        other_uuids = []
        for other in self.others:
            other_uuids.append(other.uuid)

        return 'Junction (uuid=%s, pos=%s, others=%s)' % (self.uuid, self.pos, str(other_uuids))

    def associativeRepresentation(self):
        asRepr =  {}

        asRepr['type'] = 'junction'
        asRepr['uuid'] = self.uuid
        asRepr['pos'] = self.pos.associativeRepresentation()

        if self.others:
            asRepr['others'] = []
            for other in self.others:
                asRepr['others'].append(other.uuid)

        return asRepr


    def fromAssociativeRepresentation(asRepr, parent):
        junction = Junction(parent)

        junction.uuid = asRepr.get('uuid', None)
        junction.pos = Vector2i.fromAssociativeRepresentation(asRepr.get('pos', None))

        junction._otherUuids = []
        for other in asRepr.get('others', []):
            junction._otherUuids.append(other)

        return junction


        return junction
