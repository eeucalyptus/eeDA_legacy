'''

A single page in a schematic. Contains symbols, decorations,
junctions, labels and wires. Local labels are visible on their
own page, but not on other pages.

'''

import uuid
import data.util

class SchematicsPage:
    def __init__(self, schematic = None):
        self.uuid = str(uuid.uuid4());
        self.schematic = schematic
        self.elements = []

    def addElem(self, elem):
        self.elements.append(elem)

    def __repr__(self):
        return "SchematicsPage (uuid=%s)" % [self.uuid]


    def associativeRepresentation(self):
        asRepr =  {}

        asRepr['uuid'] = self.uuid
        if self.elements:
            asRepr['elements'] = []
            for element in self.elements:
                asRepr['elements'].append(element.associativeRepresentation())
        return asRepr

    def fromAssociativeRepresentation(asRepr, parent):
        page = SchematicsPage(parent)

        page.uuid = asRepr.get('uuid', None)
        for elementRepr in asRepr.get('elements', []):
            elementTypeString = elementRepr.get('type', 'no_type')
            switch = {
                'symbol': data.schematics.Symbol,
                'wire': data.schematics.Wire,
                'decoration': data.schematics.Decoration,
                'junction': data.schematics.Junction,
                'label': data.schematics.Label
            }

            elementType = switch.get(elementTypeString, None)
            if elementType:
                element = elementType.fromAssociativeRepresentation(elementRepr, page)
                page.elements.append(element)

        return page
