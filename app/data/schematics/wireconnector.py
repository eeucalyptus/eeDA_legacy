'''

A wire has two wire connectors, one at each end. These connectors
may be attached to another connector by a connection. If connection is
None, the wire connector is unattached.

'''

import uuid

from .schematicsconnector import SchematicsConnector
from data.util import Vector2i

class WireConnector(SchematicsConnector):
    def __init__(self, wire, pos = Vector2i()):
        super().__init__(wire)
        self.uuid = str(uuid.uuid4())

        self.wire = wire
        self.pos = pos

    def associativeRepresentation(self):
        asRepr =  {}

        asRepr['uuid'] = self.uuid
        if self.other:
            asRepr['other'] = self.other.uuid
        asRepr['pos'] = self.pos.associativeRepresentation()

        return asRepr

    def fromAssociativeRepresentation(asRepr, parent):
        connector = WireConnector(parent)

        connector.pos = Vector2i.fromAssociativeRepresentation(asRepr.get('pos', []))
        connector.uuid = asRepr.get('uuid', None)

        return connector
