'''

A label is a connector that can be used to connect a net without
a wire in between. This is useful for readability and to enable
connected nets between pages.
A label has a defined scope. It can either be local or global.
Hierarchical pins are not supported, because their behaviour
leads to multiple usages of the same label name, on different
sheets, some connected, some unconnected, which is mosly hard
to read and understand.

'''

import uuid

from .schematicsconnector import SchematicsConnector
from .schematicselement import SchematicsElement

class Label(SchematicsElement, SchematicsConnector):
    def __init__(self, page):
        SchematicsElement.__init__(self, page)
        self.uuid = str(uuid.uuid4())
        
        self.text = ''
        self.globalLabel = False
        
        self.pos = Vector2i()