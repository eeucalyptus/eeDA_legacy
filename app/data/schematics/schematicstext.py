'''

A schematicstext is a schematicselement text with a position (relative), content, font, etc

'''

from data.util import Vector2i
from .schematicselement import SchematicsElement

import uuid

class SchematicsText(SchematicsElement):
    def __init__(self, parent):
        self.uuid = uuid.uuid1()
        self.text = ''
        self.pos = Vector2i()
        self.font = ''
        self.fontsize = 1

    def __repr__(self):
        return "SchematicsText (text=\"%s\", uuid=%s)" % (self.text, self.uuid)
