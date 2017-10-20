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
        schematic = self._parseSchematic()

        print('schematic='+str(schematic))
        print('schematic.field='+str(schematic.fields))
        print('schematic.pages=')
        for page in schematic.pages:
            print('\t'+str(page))
            print('\t\tschematic='+str(page.schematic))
            print('\t\telements=')
            for element in page.elements:
                print('\t\t\t'+str(element))
                if(type(element) is schematics.Symbol):
                    print('\t\t\t\tpos='+str(element.pos))
                    print('\t\t\t\tparts=')
                    for part in element.parts:
                        print('\t\t\t\t\t'+str(part).replace('\n', ' '))
                    print('\t\t\t\tconnectors=')
                    for connector in element.connectors:
                        print('\t\t\t\t\t'+str(connector).replace('\n', ' '))
            if(type(element) is schematics.Wire):
                print('\t\t\t\tpos='+str(element.pos))
                print('\t\t\t\tparts=')
                for part in element.parts:
                    print('\t\t\t\t\t'+str(part).replace('\n', ' '))

        return schematic

    def _openSchematicsFile(self):
        filestream = open(self.path, 'r')
        filenode = yaml.safe_load(filestream)

        # TODO Implement error handling (not found, no schematics, corrupted, etc)


        self.schematicnode = filenode.get('schematic', {})

        #if self._checkFileInfo(filenode.get('info', {})):
        #    self.schematicnode = filenode.get('schematic', {})
        #else:
        #    pass

    def _checkFileInfo(self, node):
        if not node:
            return False
        if node.get('type', '') != 'schematics':
            return False
        if not self._isVersionCompatible(node.get('version', 0)):
            return False

        return True


    def _isVersionCompatible(self, version):
        return True

    def _parseSchematic(self):
        if not self.schematicnode:
            raise NoSchematicsFileError()
        schematic = schematics.Schematic()

        schematic.uuid = self.schematicnode.get('uuid', '')

        for pagenode in self.schematicnode.get('pages', []):
            page = self._parsePage(pagenode, schematic)
            schematic.addPage(page)

        schematic.fields = self.schematicnode.get('fields', {})

        return schematic

    def _parsePage(self, node, schematic):
        page = schematics.SchematicsPage(schematic)
        self._currentPage = page

        page.uuid = node.get('uuid', '')
        page.schematic = schematic

        self._pageConnectorsByUuid = {}
        self._pageConnectorOtherUuids = {}

        for elementnode in node.get('elements', []):
            element = self._parseElement(elementnode)
            page.elements.append(element)

        self._linkPageConnectors()

        return page

    def _parseElement(self, node):
        elementType = node.get('type', 'no_type')
        switch = {
            'symbol': self._parseSymbolElement,
            'wire': self._parseWireElement,
            'decoration': self._parseDecorationElement,
            'junction': self._parseJunctionElement,
            'label': self._parseLabelElement
        }

        parse = switch.get(elementType, self._parseUnknownElement)

        return parse(node)


    def _parseSymbolElement(self, node):
        symbol = schematics.Symbol(self._currentPage, None)
        self._currentSymbol = symbol

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
                connector = self._parseSymbolConnector(part)
                symbol.connectors.append(connector)
            else:
                print('Part type not implemented!')

        print('Symbol!')
        return symbol

    def _parseSymbolConnector(self, node):
        print(node)
        connector = schematics.SymbolConnector(self._currentSymbol)
        connector.uuid = node.get('uuid', '')
        connector.pinname = node.get('pinname', '')
        connector.pinnumber = node.get('pinnumber', -1)
        connector.pinname = node.get('pinname', '')
        self._pageConnectorsByUuid[connector.uuid] = connector
        self._pageConnectorOtherUuids[connector] = [node.get('other', 'NONE')]

        return connector

    def _parseWireElement(self, node):
        print('Wire!')
        if node:
            wire = schematics.Wire(self._currentPage)
            wire.uuid = node.get('uuid', '')
            for point in node.get('points', []):
                wire.points.append(util.Vector2i(int(point[0]), int(point[1])))
            connectors_node = node.get('connectors', {})
            if connectors_node:
                wire.connectors[0] = self._parseWireConnector(connectors_node[0], wire)
                wire.connectors[1] = self._parseWireConnector(connectors_node[1], wire)
            return wire
        else:
            return None

    def _parseWireConnector(self, node, wire):
        connector = schematics.WireConnector(wire)
        connector.uuid = node.get('uuid', '')
        connector.pos = util.Vector2i(node.get('pos', [0, 0])[0],
            node.get('pos', [0, 0])[1])
        self._pageConnectorsByUuid[connector.uuid] = connector
        self._pageConnectorOtherUuids[connector] = [node.get('other', 'NONE')]

        return connector


    def _parseDecorationElement(self, node):
        print('Decoration!')


    def _parseJunctionElement(self, node):
        junction = schematics.Junction(self._currentPage)
        junction.uuid = node.get('uuid', '')
        self._pageConnectorsByUuid[junction.uuid] = junction
        self._pageConnectorOtherUuids[junction] = node.get('others', [])
        print('Junction')
        return junction


    def _parseLabelElement(self, node):
        label = schematics.Label(self._currentPage)
        label.uuid = node.get('uuid', '')
        label.pos = node.get('pos', util.Vector2i())
        label.text = _parseText(node, label)

        self._pageConnectorsByUuid[label.uuid] = label
        self._pageConnectorOtherUuids[label] = node.get('other', 'NONE')

        print('Label!')


    def _parseUnknownElement(self, node):
        print('Unknown!')

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
        print('Connectors by UUID:')
        print(self._pageConnectorsByUuid)
        print('\nOthers by connectors:')
        print(self._pageConnectorOtherUuids)
        print('\n')

        for connector, other_uuids in self._pageConnectorOtherUuids.items():
            if type(connector) is schematics.Junction:
                for other_uuid in other_uuids:
                    other = self._pageConnectorsByUuid.get(other_uuid, None)
                    connector.others.append(other)
            else:
                other = self._pageConnectorsByUuid.get(other_uuids[0], None)
                connector.other = other

if __name__ == '__main__':
    loader = SchematicsLoader('resources/testschematics.eesc')
    schematic = loader.loadSchematic()
