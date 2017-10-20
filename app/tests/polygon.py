from .testinit import *

class TestCasePolygon(unittest.TestCase):
    
    def setUp(self):
        self.poly1 = Polygon.fromPoints(Vector2d(),
            Vector2d(0, 1), Vector2d(1, 1), Vector2d(1, 0))
        self.poly2 = Polygon.fromPoints(Vector2d(),
            Vector2d(1, 0), Vector2d(1, 1), Vector2d(0, 1))
        self.poly3 = Polygon.fromPoints(Vector2d(),
            Vector2d(1, 0), Vector2d(1, 1), Vector2d(0.9, 0.1))
            
    def testConvexityTest(self):
        self.assertTrue(self.poly1.isConvex())
        self.assertTrue(self.poly2.isConvex())
        self.assertFalse(self.poly3.isConvex())
        
    def testPointInPoly(self):
        p1 = Vector2d(0.4, 0.6)
        p2 = Vector2d(1.5, 0.5)
        self.assertTrue(self.poly1.containsPoint(p1))
        self.assertFalse(self.poly1.containsPoint(p2))