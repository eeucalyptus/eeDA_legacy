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

from data.util import Vector2i

from .schematicsconnector import SchematicsConnector
from .schematicselement import SchematicsElement
import graphics.drawables.schematics

class Label(SchematicsElement, SchematicsConnector):
    def __init__(self, page):
        SchematicsElement.__init__(self, page)
        SchematicsConnector.__init__(self, page)
        self.uuid = str(uuid.uuid4())

        self.text = ''
        self.globalLabel = False
        self.pos = Vector2i()
        self.other = None
        self._otherUuid = None


    def initDrawable(self, gl):
        self.drawable = graphics.drawables.schematics.LabelRenderer(self, gl)

    def associativeRepresentation(self):
        asRepr =  {}

        asRepr['type'] = 'label'
        asRepr['uuid'] = self.uuid
        asRepr['globallabel'] = self.globalLabel
        asRepr['pos'] = self.pos.associativeRepresentation()
        asRepr['text'] = self.text
        if other:
            asRepr['other'] = other.uuid

        return asRepr

    def fromAssociativeRepresentation(asRepr, parent):
        label = Label(parent)

        label.uuid = asRepr.get('uuid', None)
        label.pos = Vector2i.fromAssociativeRepresentation(asRepr)
        label.globalLabel = asRepr.get('globallabel', False)
        label.text = asRepr.get('text', '')
        label._otherUuid = asRepr.get('other', None)

        return label
