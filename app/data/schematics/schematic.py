'''

The schematic class contains the whole data structure needed for
the circuit representation and manipulation. It is divided into
pages which themselves contain symbols, wires, etc.

'''

import uuid
from .schematicspage import SchematicsPage
import data.schematics

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

    def associativeRepresentation(self):
        asRepr =  {}

        asRepr['uuid'] = self.uuid
        asRepr['pages'] = []
        for page in self.pages:
            asRepr['pages'].append(page.associativeRepresentation())
        if self.fields:
            asRepr['fields'] = {}
            for key, value in self.fields:
                asRepr['fields'][key] = value

        return asRepr

    def fromAssociativeRepresentation(asRepr):
        schematic = Schematic()

        schematic.uuid = asRepr.get('uuid', None)
        for key, value in asRepr.get('fields', {}):
            schematic.fields[key] = value

        print(asRepr)
        for pageRepr in asRepr.get('pages', []):
            page = data.schematics.SchematicsPage.fromAssociativeRepresentation(pageRepr, schematic)
            schematic.pages.append(page)

        return schematic
