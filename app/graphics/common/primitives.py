from data.util import Vector2i, Polygon
import math
'''

A collection of auxiliary functions capable of rendering a few primitives. Note that face color etc. must be configured by the calling renderer.

'''

# renders a circle as a counterclockwise trianle fan
def pRenderCircle(renderer, center = Vector2i(), radius = 10, depth = 1.0, resolution = 60):
    renderer.gl.glBegin(renderer.gl.GL_TRIANGLE_FAN)
    renderer.gl.glVertex3d(center.x, center.y, depth) # centroid

    for i in range(resolution + 1):
        x = center.x + math.cos(2 * math.pi * i/float(resolution)) * radius
        y = center.y - math.sin(2 * math.pi * i/float(resolution)) * radius
        renderer.gl.glVertex3d(x, y, depth)           # outer vertices


    renderer.gl.glVertex3d(center.x, center.y, depth) # centroid again
    renderer.gl.glEnd()
    
# def pRenderConvexPoly(renderer, polygon, pos, depth = 1.0):
#     renderer.gl.glBegin(renderer.gl.GL_TRIANGLE_FAN)
#     adjPolygon = polygon.translated(pos)
#     centroid = adjPolygon.centroid()
#     renderer.gl.glVertex3d(centroid.x, centroid.y, depth)
#     last = adjPolygon.points[-1]
#     renderer.gl.glVertex3d(last.x, last.y, depth)
#     for point in adjPolygon.points:
#         renderer.gl.glVertex3d(point.x, point.y, depth)
#     renderer.gl.glEnd()

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