'''

A decoration is a function-less part of the schematic that can be used for documentation purposes, notes and graphical.

'''

import uuid
from .schematicselement import SchematicsElement

class Decoration(SchematicsElement):
    def __init__(self, page):
        super().__init__(page)
        self.uuid = uuid.uuid1()
        
        self.parts = []
        
        self.pos = Vector2i()