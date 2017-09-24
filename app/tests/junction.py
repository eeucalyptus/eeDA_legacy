from .testinit import *

class TestCaseJunction(unittest.TestCase):
    
    def setUp(self):
        self.junction = Junction("page")
    
    def tearDown(self):
        self.junction = None
        
    def testConnecting(self):
        self.junction.connect("Alice")
        self.junction.connect("Bob")
        self.junction.disconnect("Alice")
        self.junction.disconnect("Dave")    # I'm sorry, I can't do that.
        self.assertTrue(self.junction.isConnected("Bob"))
        self.assertFalse(self.junction.isConnected("Alice"))
        self.assertFalse(self.junction.isConnected("Charlie"))
    
    def testFromConnectorAndWireConnection(self):
        wire = Wire("page")
        connector = WireConnector(wire, Vector2i(42, 73))
        connector2 = WireConnector(wire, Vector2i(10, 10))
        wire.setConnectors(connector, connector2)
        junction = Junction.fromConnector(connector)
        self.assertEqual(junction.pos.x, 42)
        self.assertTrue(junction.isConnected(connector))
        self.assertFalse(junction.isConnected(connector2))
        self.assertTrue(junction.isWireConnected(wire))
        