from . import Renderer
from data.util import Vector2i, Vector2d
from .common import eeDAcolor, pMakeCircleArray, pMakeLineArray
import OpenGL.GL as gl

class WireRenderer(Renderer):
    
    WIREWIDTH = 2.0 # actually half the width of the representation
    DEPTH = 1.0
    
    def __init__(self, wire):
        super().__init__()
        self.wire = wire
        self.callList = self.genSymbolCallList()
        
    def genSymbolCallList(self):
        self.unCon1 = False
        self.unCon2 = False
        
        self.pointAry = []
        if self.wire.connectors[0] != None:
            if self.wire.connectors[0].isUnconnected():
                self.unCon1 = True
            self.pointAry.append(self.wire.connectors[0].pos)
        else:
            self.unCon1 = True
        self.pointAry += self.wire.points
        if self.wire.connectors[1] != None:
            if self.wire.connectors[1].isUnconnected():
                self.unCon2 = True
            self.pointAry.append(self.wire.connectors[1].pos)
        else:
            self.unCon2 = True
        
        self.vertices = pMakeLineArray(self.pointAry, Vector2i(), self.WIREWIDTH, self.DEPTH)
        
        genList = gl.glGenLists(1)
        gl.glNewList(genList, gl.GL_COMPILE)
        
        self.setColor(eeDAcolor.WIRE_UNCONNECTED)
        if self.unCon1:
            self.renderUnconnected(self.pointAry[0])
        if self.unCon2:
            self.renderUnconnected(self.pointAry[-1])
        self.setColor(eeDAcolor.WIRE)
        
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glVertexPointer(3, gl.GL_FLOAT, 0, self.vertices)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, len(self.vertices) / 3)
        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        
        gl.glEndList()

        return genList
    
    def renderUnconnected(self, pos):
        
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        circle = pMakeCircleArray(pos, self.WIREWIDTH * 1.5, self.DEPTH, 30)
        gl.glVertexPointer(3, gl.GL_FLOAT, 0, circle)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 0, len(circle) / 3)
        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)