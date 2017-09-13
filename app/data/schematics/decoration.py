'''

A decoration is a function-less part of the schematic that can be used for documentation purposes, notes and graphical.

'''

import uuid

class Decoration:
    def __init__(self):
        self.uuid = uuid.uuid1()
        
        self.renderer = None
        self.parts = []
        
        self.pos = Vector2i()