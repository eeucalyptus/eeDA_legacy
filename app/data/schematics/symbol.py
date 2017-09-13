'''

A symbol is the schematics representation of a component. A component 
may have one or more symbols. The symbols have symbol connectors 
which may be connected to other connectors like wires and labels, etc. 
A symbol has also multiple parts for graphical presentation. These may 
be Polygons or texts or other graphical parts.

'''

import uuid

from data.util import Vector2i

class Symbol:
    def __init__(self, component):
        self.uuid = uuid.uuid1();
        self.component = component
        
        self.renderer = None
        
        self.connectors = []
        self.parts = []
        
        self.pos = Vector2i()