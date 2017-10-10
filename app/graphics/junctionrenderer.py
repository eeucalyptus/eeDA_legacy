from . import Renderer
from .common import pMakeCircleArray
from data.util import Vector2i
import math
import OpenGL.GL as gl

'''

The JunctionRenderer holds the gl display list for a single junction
and is able to update it, when the underlying junction changes.

'''

class JunctionRenderer(Renderer):
    
    RESOLUTION = 60
    
    def __init__(self, junction):
        super().__init__(gl)
        self.junction = junction
        self.callList = self.genSymbolCallList()
        
    def genSymbolCallList(self):
        self.vertices = pMakeCircleArray(self.junction.pos, resolution = self.RESOLUTION)
        
        
        genList = gl.glGenLists(1)
        gl.glNewList(genList, gl.GL_COMPILE)
        gl.glColor4f(0.75, 1.0, 0.93, 1.0) # the best color in the world
        
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glVertexPointer(3, gl.GL_FLOAT, 0, self.vertices)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 0, self.RESOLUTION)
        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        
        gl.glEndList()

        return genList