'''

A symbol is the schematics representation of a component. A component
may have one or more symbols. The symbols have symbol connectors
which may be connected to other connectors like wires and labels, etc.
A symbol has also multiple parts for graphical presentation. These may
be Polygons or texts or other graphical parts.

'''

import uuid

import graphics
from data.util import Vector2i, Polygon
from .schematicselement import SchematicsElement

class Symbol(SchematicsElement):
    def __init__(self, page, component):
        super().__init__(page)

        self.uuid = str(uuid.uuid4());
        self.component = component

        self.connectors = []
        self.parts = []

        self.pos = Vector2i()

        # graphics
        self.polygons = []

    def initRenderer(self, gl):
        self.renderer = graphics.SymbolRenderer(self, gl)

    def addPolygon(self, poly):
        self.polygons.append(poly)
