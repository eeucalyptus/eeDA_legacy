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
