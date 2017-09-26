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

    def containsPoint(self, point):
        pass

    def centroid(self): # this isn't really a centroid. But if the polygon is convex, the point is inside the polygon.
        if len(self.points) == 0:
            # TODO Error handling (don't just return 0, exception?)
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
