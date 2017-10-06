from data.util import Vector2i, Polygon
import math
from graphics import Renderer
from .eedacolors import eeDAcolor
'''

A collection of auxiliary functions capable of rendering a few primitives. Note that face color etc. must be configured by the calling renderer.

'''

# renders a circle as a counterclockwise trianle fan
def pMakeCircleArray(center = Vector2i(), radius = 10, depth = 1.0, resolution = 60):
    array = []

    for i in range(resolution + 1):
        x = center.x + math.cos(2 * math.pi * i/float(resolution)) * radius
        y = center.y - math.sin(2 * math.pi * i/float(resolution)) * radius
        array += [x, y, depth]

    return array

def pRenderTriangle(renderer, triangle, pos, depth = 1.0):
    renderer.gl.glBegin(renderer.gl.GL_TRIANGLES)
    adjTri = triangle.translated(pos)
    for point in adjTri.points:
        renderer.gl.glVertex3d(point.x, point.y, depth)
    renderer.gl.glEnd()
    
def pRenderPolygon(renderer, polygon, pos, depth = 1.0):
    triAry = polygon.triangles()
    for tri in triAry:
        pRenderTriangle(renderer, tri, pos)
        
        
def pMakePolygonArray(polygon, pos, depth = 1.0):
    triangles = polygon.triangles()
    array = []
    
    for tri in triangles:
        for point in tri.points:
            point += pos
            array += [point.x, point.y, depth]
    
    return array

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