from point2D import *

class PointArray(list):
    def __init__(self):
        super().__init__()
        
        
    def minMaxXY(self):
        minX = self[0].x
        maxX = self[0].x
        minY = self[0].y
        maxY = self[0].y
        for point in self:
            if point.x < minX:
                minX = point.x
            elif point.x > maxX:
                maxX = point.x
                
            if point.y < minY:
                minY = point.y
            elif point.y > maxY:
                maxY = point.y
                
        ary = PointArray()
        ary.append(Point2D(minX, minY))
        ary.append(Point2D(maxX, maxY))
        return ary
    
class Polygon():
    
    def __init__(self, pointAry):
        self.points = pointAry
    
    def fromArray(ary):
        pAry = PointArray()
        for elem in ary:
            elem = Point2D(elem[0], elem[1])
            pAry.append(elem)
        return Polygon(pAry)
    
    def fromPoints(*args):
        ary = PointArray()
        for i in args:
            ary.append(i)
        return Polygon(ary)
        
    def containsPoint(self, point):
        pass
        
    def boundingBox(self):
        minMax = self.points.minMaxXY()
        topLeft = Point2D(minMax[0].x, minMax[0].y)
        topRight = Point2D(minMax[1].x, minMax[0].y)
        botLeft = Point2D(minMax[0].x, minMax[1].y)
        botRight = Point2D(minMax[1].x, minMax[1].y)
        box = Polygon.fromPoints(topLeft, topRight, botLeft, botRight)
        return box
        
    def __repr__(self):
        string = "Polygon:"
        for i in self.points:
            string += "\n"+i.__repr__()
        return string
        

if __name__=="__main__":
    p1 = Point2D(-1, 2)
    p2 = Point2D(4, 3)
    p3 = Point2D(2, 10)
    polly = Polygon.fromPoints(p1, p2, p3)
    boxy = polly.boundingBox()
    
    print(boxy)