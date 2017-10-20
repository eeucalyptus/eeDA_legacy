from .testinit import *

class TestCaseVector2d(unittest.TestCase):
    
    def setUp(self):
        self.N = Vector2d()
        self.A = Vector2d(1, 1)
        self.B = Vector2d(0, 1)
        self.C = Vector2d(1, -1)
        self.D = Vector2d(-1, -1)
        self.E = Vector2d(1, 0)

    def testDotProduct(self):
        self.assertEqual(self.A.dot(self.A), 2)
        self.assertEqual(self.C.dot(self.D), 0)
        self.assertEqual(self.N.dot(self.A), 0)
        self.assertEqual(self.A.dot(self.B), 1)
        
    def testConvexVertex(self):
        self.assertTrue(self.A.convexVertex(self.N))    # zero vector edge case
        self.assertTrue(self.A.convexVertex(self.A))    # identical vector edge case
        self.assertFalse(self.A.convexVertex(self.D))   # antilinear edge case
        self.assertTrue(self.A.convexVertex(self.B))
        self.assertFalse(self.A.convexVertex(self.E))