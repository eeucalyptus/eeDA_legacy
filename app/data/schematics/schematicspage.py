'''

A single page in a schematic. Contains symbols, decorations,
junctions, labels and wires. Local labels are visible on their
own page, but not on other pages.

'''

import uuid

class SchematicsPage:
    def __init__(self, schematic = None):
        self.uuid = uuid.uuid1();

        self.schematic = schematic

        self.elements = []

    def addElem(self, elem):
        self.elements.append(elem)
