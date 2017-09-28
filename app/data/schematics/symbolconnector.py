'''

A symbolconnector is the schematics representation for a pin of a
component. It is connected to other connectors using connections.
It can be attached to one connection.

'''

import uuid

from .schematicsconnector import SchematicsConnector

class SymbolConnector(SchematicsConnector):
    def __init__(self, symbol,):
        super().__init__(symbol)
        self.uuid = uuid.uuid1();
        self.symbol = symbol

        self.pinnumber = 0
        self.pinname = ''

        self.pos = Vector2i()
        self.polygons = []
