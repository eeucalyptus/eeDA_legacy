from data.util import Vector2i, Vector2d, Polygon
import math
from graphics import Renderer
from .eedacolors import eeDAcolor
'''

A collection of auxiliary functions capable of producing vertex arrays for a few primitives.

'''

# renders a circle as a counterclockwise trianle fan
def pMakeCircleArray(center = Vector2i(), radius = 10, depth = 1.0, resolution = 60):
    array = []

    for i in range(resolution + 1):
        x = center.x + math.cos(2 * math.pi * i/float(resolution)) * radius
        y = center.y - math.sin(2 * math.pi * i/float(resolution)) * radius
        array += [x, y, depth]

    return array

def pMakePolygonArray(polygon, pos, depth = 1.0):
    triangles = polygon.triangles()
    array = []
    
    for tri in triangles:
        for point in tri.points:
            point += pos
            array += [point.x, point.y, depth]
    
    return array

def pMakeLineArray(pointArray, pos, lineWidth, depth = 1.0):
    vertices = []
    pointArray = [point + pos for point in pointArray]
    for i in range(len(pointArray) - 1):
        vertices += pSingleLineVertices(pointArray[i], pointArray[i+1], lineWidth, depth)
    return vertices
    
def pSingleLineVertices(point1, point2, width, depth):
    point1 = Vector2d.fromVector2i(point1)
    point2 = Vector2d.fromVector2i(point2)
    
    vector = point2 - point1
    unitVector = vector.normalize()
    uvRotated = unitVector.normalCW()
    
    pointAry = []
    
    pointAry.append(point1 + uvRotated * width)
    pointAry.append(point1 - uvRotated * width)
    
    pointAry.append(point2 + uvRotated * width)
    pointAry.append(point2 - uvRotated * width)
    
    resAry = []
    
    for point in pointAry:
        resAry += [point.x, point.y, depth]
    
    return resAry

class PointRenderer(Renderer):  # kludged together for debug
    def __init__(self, gl, x, y):
        super().__init__(gl)
        self.x = x
        self.y = y
        self.callList = self.genSymbolCallList()
        
    def genSymbolCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        self.setColor(eeDAcolor.RHINO)
        
        self.gl.glPointSize(20)
        self.gl.glBegin(self.gl.GL_POINTS)
        self.gl.glVertex3d(self.x, self.y, 1.0)
        self.gl.glEnd()
        
        self.gl.glEndList()
        
        
        return genList