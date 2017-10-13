from . import Renderer
from data.util import Vector2i, Vector2d
from .common import eeDAcolor, pMakeCircleArray, pMakeLineArray

class WireRenderer(Renderer):
    
    DEPTH = 1.0
    
    def __init__(self, wire, gl):
        super().__init__(gl)
        self.wire = wire
        self.callList = self.genSymbolCallList()
        
    def genSymbolCallList(self):
        
        self.width = self.wire.style['width'] / 2
        self.color = self.wire.style['color']
        
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
        
        self.vertices = pMakeLineArray(self.pointAry, Vector2i(), self.width, self.DEPTH)
        
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        
        self.setColor(eeDAcolor.WIRE_UNCONNECTED)
        if self.unCon1:
            self.renderUnconnected(self.pointAry[0])
        if self.unCon2:
            self.renderUnconnected(self.pointAry[-1])
        self.setColor(self.color)
        
        self.gl.glEnableClientState(self.gl.GL_VERTEX_ARRAY)
        self.gl.glVertexPointer(3, self.gl.GL_FLOAT, 0, self.vertices)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLE_STRIP, 0, len(self.vertices) / 3)
        self.gl.glDisableClientState(self.gl.GL_VERTEX_ARRAY)
        
        self.gl.glEndList()

        return genList
    
    def renderUnconnected(self, pos):
        
        self.gl.glEnableClientState(self.gl.GL_VERTEX_ARRAY)
        circle = pMakeCircleArray(pos, self.width * 1.5, self.DEPTH, 30)
        self.gl.glVertexPointer(3, self.gl.GL_FLOAT, 0, circle)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLE_FAN, 0, len(circle) / 3)
        self.gl.glDisableClientState(self.gl.GL_VERTEX_ARRAY)