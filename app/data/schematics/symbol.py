'''

A symbol is the schematics representation of a component. A component
may have one or more symbols. The symbols have symbol connectors
which may be connected to other connectors like wires and labels, etc.
A symbol has also multiple parts for graphical presentation. These may
be Polygons or texts or other graphical parts.

'''

import uuid

from data.util import Vector2i, Polygon
from .schematicselement import SchematicsElement

class Symbol(SchematicsElement):
    def __init__(self, page, component):
        super().__init__(page)
        
        self.uuid = uuid.uuid1();
        self.component = component
        
        self.connectors = []
        self.parts = []
        
        self.pos = Vector2i()
        
        # graphics
        self.polygons = []
        self.linestrips = []
        
    def addPolygon(self, poly):
        self.polygons.append(poly)
        
    def addLinestrip(self, strip):  # technically identical to polygons, only that it's rendered similar to a line strip
        self.linestrips.append(strip)
        
    def setRenderer(self, renderer):
        self.renderer = renderer
        
    def setPos(self, pos):
        self.pos = pos