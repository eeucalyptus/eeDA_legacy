'''

The schematic class contains the whole data structure needed for
the circuit representation and manipulation. It is divided into
pages which themselves contain symbols, wires, etc.

'''

import uuid
from .schematicspage import SchematicsPage

class Schematic:
    def __init__(self):
        self.uuid = str(uuid.uuid4());

        self.pages = []
        self.fields = {}

    def addPage(self, page = None):
        if page == None:
            page = SchematicsPage(self)
            self.pages.append(page)
        else:
            self.pages.append(page)
        return page

    def __repr__(self):
        return "Schematics (uuid=%s)" % [self.uuid]
