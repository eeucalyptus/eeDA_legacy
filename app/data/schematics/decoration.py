'''

A decoration is a function-less part of the schematic that can be used for
documentation purposes, notes and graphical.

'''

import uuid
import graphics.drawables.schematics
from .schematicselement import SchematicsElement
import data.util

class Decoration(SchematicsElement):
    def __init__(self, page):
        super().__init__(page)
        self.uuid = str(uuid.uuid4())

        self.parts = []

        self.pos = Vector2i()

    def initDrawable(self, gl):
        self.drawable = graphics.drawables.schematics.DecorationRenderer(self, gl)

    def associativeRepresentation(self):
        asRepr =  {}

        asRepr['type'] = 'decoration'
        asRepr['uuid'] = self.uuid
        asRepr['pos'] = self.pos.associativeRepresentation()
        asRepr['parts'] = []
        for part in self.parts:
            asRepr['parts'].append(part.associativeRepresentation())

        return asRepr

    def fromAssociativeRepresentation(asRepr, parent):
        deco = Decoration(parent)

        deco.uuid = asRepr.get('uuid', None)
        for partRepr in asRepr.get('parts', []):
            partType = partRepr.get('type', None)
            if partType == 'polygon':
                part = data.util.Polygon.fromAssociativeRepresentation(partRepr, deco)
                deco.parts.append(part)
            elif partType == 'text':
                part = data.schematics.SchematicsText.fromAssociativeRepresentation(partRepr, deco)
                deco.parts.append(part)

        deco.pos = data.util.Vector2i.fromAssociativeRepresentation(asRepr)

        return deco
