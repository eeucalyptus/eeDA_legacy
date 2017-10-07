from . import Renderer
from data.util import Vector2i, Vector2d
from .common import eeDAcolor, pMakeCircleArray

class WireRenderer(Renderer):
    
    WIREWIDTH = 5.0
    DEPTH = 1.0
    
    def singleLineVertices(self, point1, point2):
        point1 = Vector2d.fromVector2i(point1)
        point2 = Vector2d.fromVector2i(point2)
        
        vector = point2 - point1
        unitVector = vector.normalize()
        uvRotated = unitVector.normalCW()
        
        pointAry = []
        
        pointAry.append(point1 + uvRotated * self.WIREWIDTH)
        pointAry.append(point1 - uvRotated * self.WIREWIDTH)
        
        pointAry.append(point2 + uvRotated * self.WIREWIDTH)
        pointAry.append(point2 - uvRotated * self.WIREWIDTH)
        
        resAry = []
        
        for point in pointAry:
            resAry += [point.x, point.y, self.DEPTH]
        
        return resAry
    
    def __init__(self, wire, gl):
        super().__init__(gl)
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
        
        self.vertices = []
        
        for i in range(len(self.pointAry) - 1):
            self.vertices += WireRenderer.singleLineVertices(self, self.pointAry[i], self.pointAry[i+1])
            
        
        
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        
        self.setColor(eeDAcolor.WIRE_UNCONNECTED)
        if self.unCon1:
            self.renderUnconnected(self.pointAry[0])
        if self.unCon2:
            self.renderUnconnected(self.pointAry[-1])
        self.setColor(eeDAcolor.WIRE)
        
        self.gl.glEnableClientState(self.gl.GL_VERTEX_ARRAY)
        self.gl.glVertexPointer(3, self.gl.GL_FLOAT, 0, self.vertices)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLE_STRIP, 0, len(self.vertices) / 3)
        self.gl.glDisableClientState(self.gl.GL_VERTEX_ARRAY)
        
        self.gl.glEndList()

        return genList
    
    def renderUnconnected(self, pos):
        
        self.gl.glEnableClientState(self.gl.GL_VERTEX_ARRAY)
        circle = pMakeCircleArray(pos, self.WIREWIDTH, self.DEPTH, 30)
        self.gl.glVertexPointer(3, self.gl.GL_FLOAT, 0, circle)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLE_FAN, 0, len(circle) / 3)
        self.gl.glDisableClientState(self.gl.GL_VERTEX_ARRAY)