import data.schematics as schematics
import data.util as util
import yaml

class SchematicsLoaderError(Exception):
    pass

class SchematicsLoader:
    def __init__(self, path):
        self.path = path
        pass
    def loadSchematic(self):
        self._openSchematicsFile()
        return self._parseSchematic()

    def _openSchematicsFile(self):
        filestream = open(self.path, 'r')
        filenode = yaml.safe_load(filestream)

        # TODO Implement error handling (not found, no schematics, corrupted, etc)

        self.schematicnode = filenode.get('schematic', {})

    def _parseSchematic(self):
        if not self.schematicnode:
            raise NoSchematicsFileError()
        schematic = schematics.Schematic()

        schematic.uuid = self.schematicnode.get('uuid', '')

        for pagenode in self.schematicnode.get('pages', []):
            page = self._parsePage(pagenode, schematic)
            schematic.addPage(page)

        schematic.fields = self.schematicnode.get('fields', [])

        return schematic

    def _parsePage(self, node, schematic):
        page = schematics.SchematicsPage(schematic)

        page.uuid = node.get('uuid', '')
        page.schematic = schematic

        self._pageConnectorsByUuid = {}

        for elementnode in node.get('elements', []):
            element = self._parseElement(elementnode, page)
            page.elements.append(element)

        self._linkPageConnectors()

        return page

    def _parseElement(self, node, page):
        elementType = node.get('type', 'no_type')
        switch = {
            'symbol': self._parseSymbolElement,
            'wire': self._parseWireElement,
            'decoration': self._parseDecorationElement,
            'junction': self._parseJunctionElement,
            'label': self._parseLabelElement
        }

        parse = switch.get(elementType, self._parseUnknownElement)

        return parse(node, page)


    def _parseSymbolElement(self, node, page):
        symbol = schematics.Symbol(page, None)
        symbol.uuid = node.get('uuid', '')
        symbol.pos.x = node.get('pos', [])[0]
        symbol.pos.y = node.get('pos', [])[1]

        for part in node.get('parts', []):
            parttype = part.get('type', '')

            if parttype == 'polygon':
                polygon = self._parsePolygon(part)
                symbol.parts.append(polygon)
            elif parttype == 'text':
                text = self._parseText(part, symbol)
                symbol.parts.append(text)
            elif parttype == 'connector':
                connector = schematics.SymbolConnector(symbol)
                coonnector.uuid = part.get('uuid', '')
                connector.parent = symbol
                connector.pinname = part.get('pinname', '')
                connector.pinnumber = part.get('pinnumber', -1)
                connector.pinname = part.get('pinname', '')
                self._pageConnectorsByUuid[connector.uuid] = connector
                symbol.connectors.append(connector)
            else:
                print("Part type not implemented!")

        print("Symbol!")
        return symbol

    def _parseWireElement(self, node, page):
        #wire = schematics.Wire()
        print("Wire!")


    def _parseDecorationElement(self, node, page):
        print("Decoration!")


    def _parseJunctionElement(self, node, page):
        print("Junction!")


    def _parseLabelElement(self, node, page):
        print("Label!")


    def _parseUnknownElement(self, node, page):
        print("Unknown!")

    def _parsePolygon(self, node):
        ptary = util.PointArray()

        for vertex in node.get('verticies', []):
            vect = util.Vector2i()
            vect.x = vertex[0]
            vect.y = vertex[1]
            ptary.append(vect)
        polygon = util.Polygon(ptary)

        return polygon

    def _parseText(self, node, parent):
        text = schematics.SchematicsText(parent)
        text.text = node.get('text', '')
        pos = node.get('pos', [])
        text.pos = util.Vector2i(pos[0], pos[1])
        text.uuid = node.get('uuid', '')
        text.font = node.get('font', '')
        text.fontsize = node.get('fontsize', '')
        return text

    def _linkPageConnectors(self):
        pass

if __name__ == '__main__':
    loader = SchematicsLoader('resources/testschematics.eesc')
    schematic = loader.loadSchematic()

    print("schematic="+str(schematic))
    print("schematic.field="+str(schematic.fields))
    print("schematic.pages=")
    for page in schematic.pages:
        print("\t"+str(page))
        print("\t\tschematic="+str(page.schematic))
        print("\t\telements=")
        for element in page.elements:
            print("\t\t\t"+str(element))
            if(type(element) is schematics.Symbol):
                print("\t\t\t\tpos="+str(element.pos))
                print("\t\t\t\tparts=")
                for part in element.parts:
                    print("\t\t\t\t\t"+str(part).replace('\n', ' '))
                print("\t\t\t\tconnectors=")
                for connector in element.connectors:
                    print("\t\t\t\t\t"+str(connector).replace('\n', ' '))
        if(type(element) is schematics.Wire):
            print("\t\t\t\tpos="+str(element.pos))
            print("\t\t\t\tparts=")
            for part in element.parts:
                print("\t\t\t\t\t"+str(part).replace('\n', ' '))
