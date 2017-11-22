'''

A symbol is the schematics representation of a component. A component
may have one or more symbols. The symbols have symbol connectors
which may be connected to other connectors like wires and labels, etc.
A symbol has also multiple parts for graphical presentation. These may
be Polygons or texts or other graphical parts.

'''

import uuid

import data.schematics
import graphics.drawables.schematics
from data.util import Vector2i, Polygon
from .schematicselement import SchematicsElement

class Symbol(SchematicsElement):
    def __init__(self, page):
        super().__init__(page)

        self.uuid = str(uuid.uuid4());
        self.parts = []
        self.pos = Vector2i()
        self.reference = ''

    def initDrawable(self, gl):
        self.drawable = graphics.drawables.schematics.SymbolDrawable(self, gl)

    def addPolygon(self, poly):
        self.parts.append(poly)

    def __repr__(self):
        return 'Symbol (uuid=%s, numParts=%d, pos=%s)' % (self.uuid, len(self.parts), str(self.pos))


    def associativeRepresentation(self):
        asRepr =  {}

        asRepr['type'] = 'symbol'
        asRepr['uuid'] = self.uuid
        asRepr['pos'] = self.pos.associativeRepresentation()
        asRepr['reference'] = self.reference
        asRepr['parts'] = []
        for part in self.parts:
            asRepr['parts'].append(part.associativeRepresentation())

        return asRepr

    def fromAssociativeRepresentation(asRepr, parent):
        symbol = data.schematics.Symbol(parent)

        symbol.uuid = asRepr.get('uuid', None)
        symbol.reference = asRepr.get('reference', '')
        symbol.pos = data.util.Vector2i.fromAssociativeRepresentation(asRepr.get('pos', None))
        for partRepr in asRepr.get('parts', []):
            partType = partRepr.get('type', None)
            if partType == 'polygon':
                poly = data.util.Polygon.fromAssociativeRepresentation(partRepr, symbol)
                symbol.parts.append(poly)
            elif partType == 'text':
                text = data.schematics.SchematicsText.fromAssociativeRepresentation(partRepr, symbol)
                symbol.parts.append(text)

        return symbol
