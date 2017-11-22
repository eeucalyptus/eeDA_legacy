'''

A schematicstext is a schematicselement text with a position (relative), content, font, etc

'''

from data.util import Vector2i
from .schematicselement import SchematicsElement

import uuid

class SchematicsText(SchematicsElement):
    def __init__(self, parent):
        self.uuid = str(uuid.uuid4())
        self.text = ''
        self.pos = Vector2i()
        self.font = ''
        self.fontsize = 1

    def __repr__(self):
        return "SchematicsText (text=\"%s\", uuid=%s)" % (self.text, self.uuid)

    def associativeRepresentation(self):
        asRepr =  {}

        asRepr['type'] = 'schematicstext'
        asRepr['uuid'] = self.uuid
        asRepr['text'] = self.text
        asRepr['pos'] = self.pos.associativeRepresentation()
        asRepr['font'] = self.font
        asRepr['fontsize'] = self.fontsize

        return asRepr

    def fromAssociativeRepresentation(asRepr, parent):
        text = SchematicsText(parent)

        text.uuid = asRepr.get('uuid', None)
        text.text = asRepr.get('text', None)
        text.pos = Vector2i.fromAssociativeRepresentation(asRepr.get('pos', None))
        text.font = asRepr.get('font', None)
        text.fontsize = asRepr.get('fontsize', None)

        return text
