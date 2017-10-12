from .testinit import *
    
def pointInTriangle(point, triangle):
    last = None
    for i in range(3):
        p1 = triangle.points[i]
        p2 = triangle.points[(i + 1) % 3]
        edge = p2 - p1
        current = edge.convexVertex(point - p1)
        if last != None and current != last:
            return False
        last = current
    return True

class TestCasePIT(unittest.TestCase):
    
    def setUp(self):
        self.triangle = Polygon.fromPoints(Vector2d(), Vector2d(1, 0), Vector2d(0, 1))
        self.pointIn1 = Vector2d(0.1, 0.1)
        self.pointIn2 = Vector2d(0.5, 0.5)  # edge case
        self.pointIn3 = Vector2d(0.9, 0.01)
        self.pointIn4 = Vector2d(0.000001, 0.000001)
        self.pointOut1 = Vector2d(1, 1)
        self.pointOut2 = Vector2d(1, -1)
        self.pointOut3 = Vector2d(-0.0001, -0.0001)
        
    def testPointInTriangle(self):
        self.assertTrue(pointInTriangle(self.pointIn1, self.triangle))
        self.assertTrue(pointInTriangle(self.pointIn2, self.triangle))
        self.assertTrue(pointInTriangle(self.pointIn3, self.triangle))
        self.assertTrue(pointInTriangle(self.pointIn4, self.triangle))
        self.assertFalse(pointInTriangle(self.pointOut1, self.triangle))
        self.assertFalse(pointInTriangle(self.pointOut2, self.triangle))
        self.assertFalse(pointInTriangle(self.pointOut3, self.triangle))