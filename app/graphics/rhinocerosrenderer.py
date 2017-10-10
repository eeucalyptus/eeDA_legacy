from . import Renderer
from .common import pMakePolygonArray, eeDAcolor
from data.util import Vector2i, Polygon

import OpenGL.GL as gl
'''

The RhinocerosRenderer holds the gl display list for a single rhinoceros
and is able to update it, when the underlying biology changes.

'''

class RhinocerosRenderer(Renderer):
    
    def __init__(self):
        super().__init__()
        self.callList = self.genSymbolCallList()
        
    def genSymbolCallList(self):
        
        
        rhinopoly = Polygon.fromPoints(\
        Vector2i(23, 146), #1\
        Vector2i(68, 183), #2\
        Vector2i(66, 163), #3\
        Vector2i(88, 168), #4\
        Vector2i(112, 134), #5\
        Vector2i(100, 132), #6\
        Vector2i(96, 103), #7\
        Vector2i(125, 122), #8\
        Vector2i(116, 115), #9\
        Vector2i(119, 92), #10\
        Vector2i(134, 111), #11\
        Vector2i(157, 92), #12\
        Vector2i(144, 204), #13\
        Vector2i(88, 237), #14\
        Vector2i(72, 240), #15\
        Vector2i(62, 211), #16\
        Vector2i(35, 188)) #17
        self.rhinoVertices = pMakePolygonArray(rhinopoly, Vector2i(), 1)
        
        gl.glColor4f(0.0, 0.0, 1.0, 1.0)
        polly = Polygon.fromPoints(\
        Vector2i(0, 0),\
        Vector2i(25, 0),\
        Vector2i(35, 12),\
        Vector2i(25, 25),\
        Vector2i(0, 25))
        self.quadVertices = pMakePolygonArray(polly, Vector2i(-400, -400), 1)
        # alright, it's not a quadrilateral. I never said I could count... - M
        # --
        genList = gl.glGenLists(1)
        gl.glNewList(genList, gl.GL_COMPILE)
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        
        self.setColor(eeDAcolor.RHINO)
        gl.glVertexPointer(3, gl.GL_INT, 0, self.rhinoVertices)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, len(self.rhinoVertices) / 3)
        
        self.setColor(eeDAcolor.WIRE)
        gl.glVertexPointer(3, gl.GL_INT, 0, self.quadVertices)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, len(self.quadVertices) / 3)
        
        gl.glEndList()

        return genList
        