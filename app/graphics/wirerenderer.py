from . import Renderer
from data.util import Vector2i, Vector2d
from .common import eeDAcolor, pMakeCircleArray, pMakeLineArray

class WireRenderer(Renderer):

    DEPTH = 1.0

    def __init__(self, wire, gl):
        super().__init__(gl)
        self.wire = wire
        self.callList = self._genCallList()

    def _genCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)

        self.width = self.wire.style['width'] / 2
        self.color = self.wire.style['color']

        self.pointAry = []

        con0_pos = self.wire.connectors[0].pos
        con1_pos = self.wire.connectors[1].pos

        self.pointAry.append(self.wire.connectors[0].pos) # Start point
        for point in self.wire.points:
            self.pointAry.append(point) # Intermediate points
        self.pointAry.append(self.wire.connectors[1].pos) # End point

        self.vertices = pMakeLineArray(self.pointAry, Vector2i(), self.width, self.DEPTH)

        if not self.wire.connectors[0].other:
            self.renderUnconnected(self.pointAry[0])
        if not self.wire.connectors[0].other:
            self.renderUnconnected(self.pointAry[-1])
        self.setColor(self.color)

        self.gl.glEnableClientState(self.gl.GL_VERTEX_ARRAY)
        self.gl.glVertexPointer(3, self.gl.GL_FLOAT, 0, self.vertices)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLE_STRIP, 0, len(self.vertices) / 3)
        self.gl.glDisableClientState(self.gl.GL_VERTEX_ARRAY)

        self.gl.glEndList()

        return genList

    def renderUnconnected(self, pos):
        self.setColor(eeDAcolor.WIRE_UNCONNECTED)

        self.gl.glEnableClientState(self.gl.GL_VERTEX_ARRAY)
        circle = pMakeCircleArray(pos, self.width * 1.5, self.DEPTH, 30)
        self.gl.glVertexPointer(3, self.gl.GL_FLOAT, 0, circle)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLE_FAN, 0, len(circle) / 3)
        self.gl.glDisableClientState(self.gl.GL_VERTEX_ARRAY)
