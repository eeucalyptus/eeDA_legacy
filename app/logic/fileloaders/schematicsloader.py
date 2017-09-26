import data.schematics as schematics
import data.util as util
import yaml

def loadSchematic(path):
    filestream = open(path, 'r')
    filenode = yaml.safe_load(filestream)

    # TODO Implement error handling (not found, no schematics, corrupted, etc)

    schematicnode = filenode.get('schematic', {})

    if schematicnode:
        return parseSchematic(schematicnode)
    else:
        # no schematic
        print("No schematic")


def parseSchematic(node):
    schematic = schematics.Schematic()

    schematic.uuid = node.get('uuid', '')

    for pagenode in node.get('pages', []):
        page = parsePage(pagenode, schematic)
        schematic.addPage(page)

    schematic.fields = node.get('fields', [])

    return schematic


def parsePage(node, schematic):
    page = schematics.SchematicsPage(schematic)

    page.uuid = node.get('uuid', '')
    page.schematic = schematic

    for elementnode in node.get('elements', []):
        element = parseElement(elementnode, page)
        page.elements.append(element)

    return page


def parseElement(node, page):
    elementType = node.get('type', 'no_type')
    switch = {
        'symbol': parseSymbolElement,
        'wire': parseWireElement,
        'decoration': parseDecorationElement,
        'junction': parseJunctionElement,
        'label': parseLabelElement
    }

    parse = switch.get(elementType, parseUnknownElement)

    return parse(node, page)


def parseSymbolElement(node, page):
    symbol = schematics.Symbol(page, None)
    symbol.uuid = node.get('uuid', '')
    symbol.pos.x = node.get('pos', [])[0]
    symbol.pos.y = node.get('pos', [])[1]

    for part in node.get('parts', []):
        parttype = part.get('type', '')
        if parttype == 'polygon':
            print("Poly")
            ptary = util.PointArray()

            for vertex in part.get('verticies', []):
                vect = util.Vector2i()
                vect.x = vertex[0]
                vect.y = vertex[1]
                ptary.append(vect)
            polygon = util.Polygon(ptary)
            symbol.parts.append(polygon)

        else:
            print("No poly")

    print("Symbol!")
    return symbol


def parseWireElement(node, page):
    print("Wire!")


def parseDecorationElement(node, page):
    print("Decoration!")


def parseJunctionElement(node, page):
    print("Junction!")


def parseLabelElement(node, page):
    print("Label!")


def parseUnknownElement(node, page):
    print("Unknown!")
