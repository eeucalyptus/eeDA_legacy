from . import Renderer
from data.util import Vector2i
from .common import eeDAcolor

class WireRenderer(Renderer):
    def __init__(self, wire, gl):
        super().__init__(gl)
        self.wire = wire
        self.callList = self._genCallList()

    def _genCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)

        self.gl.glLineWidth(5)
        self.setColor(eeDAcolor.WIRE)

        self.gl.glBegin(self.gl.GL_LINE_STRIP)


        con0_pos = self.wire.connectors[0].pos
        con1_pos = self.wire.connectors[1].pos

        self.gl.glVertex3i(con0_pos.x, con0_pos.y, 1) # Start point

        for point in self.wire.points:
            self.gl.glVertex3i(point.x, point.y, 1) # Intermediate points

        self.gl.glVertex3i(con1_pos.x, con1_pos.y, 1) # End point

        self.gl.glEnd()

        if not self.wire.connectors[0].other:
            self.renderUnconnected(con0_pos)
        if not self.wire.connectors[1].other:
            self.renderUnconnected(con1_pos)

        self.gl.glEndList()

        return genList

    def renderUnconnected(self, pos):
        self.setColor(eeDAcolor.WIRE_UNCONNECTED)


        self.gl.glBegin(self.gl.GL_LINES)
        self.gl.glVertex3i(pos.x - 10, pos.y - 10, 2)
        self.gl.glVertex3i(pos.x + 10, pos.y + 10, 2)
        self.gl.glVertex3i(pos.x + 10, pos.y - 10, 2)
        self.gl.glVertex3i(pos.x - 10, pos.y + 10, 2)
        self.gl.glEnd()
