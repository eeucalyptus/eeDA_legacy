from .testinit import *

class TestCaseSchematicsContext(unittest.TestCase):
    
    def testInstantiatesCorrectly(self):
        scmContext = SchematicsContext("schematic", "page")
        self.assertEqual(scmContext.schematic, "schematic")
        self.assertEqual(scmContext.page, "page")
        self.assertEqual(scmContext.nets, [])
        
    def testHierarchy(self):
        schematic = Schematic()
        page = schematic.addPage()
        context = SchematicsContext(schematic, page)
        wire = page.addElem(Wire(page))
        self.assertEqual(context.page.elements[0].connectors[0].wire.page.schematic, schematic)
        