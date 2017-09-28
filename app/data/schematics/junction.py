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

class Junction(SchematicsElement, SchematicsConnector):
    def __init__(self, page):
        SchematicsElement.__init__(self, page)
        self.uuid = uuid.uuid1()

        self.connections = []
        self.pos = Vector2i()


    def fromConnector(connector):
        newJunction = Junction(connector.parent.page)
        newJunction.pos = connector.pos
        newJunction.connect(connector)
        return newJunction

    def isConnected(self, connection):
        if connection in self.connections:
            return True
        else:
            return False

    def connect(self, connector):
        self.connections.append(connector)


    def disconnect(self, connector):
        if self.isConnected(connector):
            self.connections.remove(connector)

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
