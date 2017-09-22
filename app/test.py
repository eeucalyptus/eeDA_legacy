# run with: python -m unittest test.py
# add '-v' for more verbosity

import unittest
from data import *
from dependencies import *
from graphics import *
from gui import *
from logic import *
from resources import *

class TestSomeMiscStuff(unittest.TestCase):
    def testWireConnectsCorrectly(self):
        wire = Wire(None)
        wire.connectors[0].connect("Alice")
        wire.connectors[1].connect("Bob")
        self.assertTrue(wire.isConnected("Alice"))
        self.assertFalse(wire.isConnected("Charlie"))