'''

A symbolconnector is the schematics representation for a pin of a
component. It is connected to other connectors using connections.
It can be attached to one connection.

'''

import uuid

from data import util

from .schematicsconnector import SchematicsConnector

class SymbolConnector(SchematicsConnector):
    def __init__(self, symbol):
        super().__init__(symbol)
        self.uuid = str(uuid.uuid4());

        self.pinnumber = 0
        self.pinname = ''

        self.pos = util.Vector2i()
        self.polygons = []

    def __repr__(self):
        if self.other is not None:
            otheruuid = self.other.uuid
        else:
            otheruuid = "NONE"
        return "SymbolConnector (uuid=%s, pos=%s, other_uuid=%s)" % (self.uuid, str(self.pos), otheruuid)

    def associativeRepresentation(self):
        asRepr =  {}

        asRepr['type'] = 'connector'
        asRepr['uuid'] = self.uuid
        asRepr['pinnumber'] = self.pinnumber
        asRepr['pinname'] = self.pinname
        asRepr['pos'] = self.pos.associativeRepresentation()
        asRepr['polygons'] = []
        for poly in self.polygons:
            asRepr['polygons'].append(poly.associativeRepresentation())
        if self.other:
            asRepr['other'] = self.other.uuid

        return asRepr
