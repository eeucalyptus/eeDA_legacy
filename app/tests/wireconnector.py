from .testinit import *

class TestCaseWireConnector(unittest.TestCase):
    
    def setUp(self):
        self.wireCon = WireConnector("wire", Vector2i(10, 25))
        
    def tearDown(self):
        self.wireCon = None

    def testInstantiatesCorrectly(self):
        self.assertEqual(self.wireCon.wire, "wire")
        self.assertEqual(type(self.wireCon.pos), Vector2i)
        self.assertEqual(self.wireCon.pos.x, 10)
        self.assertEqual(self.wireCon.pos.y, 25)
        self.wireCon = WireConnector(None)
        self.assertEqual(self.wireCon.pos, Vector2i())