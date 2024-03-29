'''

A decoration is a function-less part of the schematic that can be used for
documentation purposes, notes and graphical.

'''

import uuid
import graphics
from .schematicselement import SchematicsElement

class Decoration(SchematicsElement):
    def __init__(self, page):
        super().__init__(page)
        self.uuid = str(uuid.uuid4())

        self.parts = []

        self.pos = Vector2i()

    def initRenderer(self, gl):
        self.renderer = graphics.DecorationRenderer(self, gl)
