from .vector2 import Vector2i
import dependencies.polytri as polytri

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
        ary.append(Vector2i(minX, minY))
        ary.append(Vector2i(maxX, maxY))
        return ary
    
class Polygon():
    def __init__(self, pointAry):
        self.points = pointAry
        self.color = None   # eeDAcolor
    
    def fromArray(ary):
        pAry = PointArray()
        for elem in ary:
            elem = Vector2i(elem[0], elem[1])
            pAry.append(elem)
        return Polygon(pAry)
        
    def fromPoints(*args):
        ary = PointArray()
        for i in args:
            ary.append(i)
        return Polygon(ary)
        
    def pointInTriangle(point, triangle):
        last = 0
        for i in range(3):
            p1 = triangle.points[i]
            p2 = triangle.points[(i + 1) % 3]
            edge = p2 - p1
            current = edge.convexityDeterminant(point - p1)
            
            if current * last < 0:
                return False
            if  i > 0 and current * last == 0:   # if the vectors are collinear, check whether the point is between the two triangle vertices
                if not ((p1.x < point.x < p2.x or p1.x > point.x > p2.x) and (p1.y < point.y < p2.y or p1.y > point.y > p2.y)):
                    return False
            last = current
        return True
        
    def changeColor(self, color):
        self.color = color
    
    def centroid(self): # this isn't really a centroid. But if the polygon is convex, the point is inside the polygon.
        if len(self.points) == 0:
            return Vector2i()
        
        sum = Vector2i()
        
        for point in self.points:
            sum = sum + point       # maybe implement in-place calculations for vectors later on
        
        return sum / len(self.points)
        
    def translated(self, vector):   # non-mutating
        newPoints = PointArray()
        for point in self.points:
            newPoints.append(point + vector)
        return Polygon(newPoints)
        
    def translate(self, vector):    # mutating
        for point in self.points:
            point = point + vector
        
    def boundingBox(self):
        minMax = self.points.minMaxXY()
        topLeft = Vector2i(minMax[0].x, minMax[0].y)
        topRight = Vector2i(minMax[1].x, minMax[0].y)
        botLeft = Vector2i(minMax[0].x, minMax[1].y)
        botRight = Vector2i(minMax[1].x, minMax[1].y)
        box = Polygon.fromPoints(topLeft, topRight, botLeft, botRight)
        return box
        
    def scale(self, factor):
        self.points = [point * factor for point in self.points]
        
    def isConvex(self):
        n = len(self.points)
        lastVertexConvex = None   # stores convexity of last vertex
        for i in range(n):
            edge1 = self.points[(i + 1) % n] - self.points[i % n]
            edge2 = self.points[(i + 2) % n] - self.points[(i + 1) % n]
            currentVertexConvex = edge1.convexVertex(edge2)
            if lastVertexConvex != None and currentVertexConvex != lastVertexConvex:
                return False
            lastVertexConvex = currentVertexConvex
        return True
        
    def containsPoint(self, point):
        for tri in self.triangles():
            if Polygon.pointInTriangle(point, tri):
                return True
        return False
        
    def __repr__(self):
        string = "Polygon:"
        for i in self.points:
            string += "\n"+i.__repr__()
        return string
        
    def triangles(self):
        '''
        returns an array of triangles using polytri
        '''
        ary = [[point.x, point.y] for point in self.points]
        triangles = polytri.triangulate(ary)
        returnAry = []
        for tri in triangles:
            returnAry.append(Polygon.fromPoints(Vector2i(tri[0][0], tri[0][1]), Vector2i(tri[1][0], tri[1][1]), Vector2i(tri[2][0], tri[2][1])))
        
        return returnAry
