from .testinit import *

class TestCaseWire(unittest.TestCase):
    
    def setUp(self):
        self.wire = Wire("page")
        
    def tearDown(self):
        self.wire = None
        
    def testInstantiatesCorrectly(self):
        self.assertEqual(type(self.wire), Wire)
        self.assertEqual(self.wire.page, "page")
        
    def testConnectsCorrectly(self):
        self.wire.connectors[0].connect("Alice")
        self.wire.connectors[1].connect("Bob")
        self.assertTrue(self.wire.isConnected("Alice"))
        self.assertTrue(self.wire.isConnected("Bob"))
        self.assertFalse(self.wire.isConnected("Charlie"))
        
    def testPointsStoredCorrectly(self):
        points = ["Point 1", "Point 2"]
        self.wire.setPoints(points)
        self.assertEqual(self.wire.points[0], "Point 1")
        self.assertEqual(self.wire.points[1], "Point 2")