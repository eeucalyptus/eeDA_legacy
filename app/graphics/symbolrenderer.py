from PyQt5 import QtWidgets, QtGui
from .renderer import Renderer
from .common import eeDAcolor
from data import util

class SymbolRenderer(Renderer):
    def __init__(self, symbol, gl):
        super().__init__(gl)
        self.symbol = symbol
        self.callList = self._genCallList()
        print(str(self.symbol) + " has calllist: " + str(self.callList))

    def _genCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)

        # TODO: Replace dummy renderer

        self.gl.glColor4f(0.282, 0.235, 0.196, 1.0)

        # DUMMY
        self.gl.glLineWidth(2.5)
        for part in self.symbol.parts:
            if isinstance(part, util.Polygon):
                self.gl.glBegin(self.gl.GL_LINE_LOOP)
                for vertex in part.points:
                    self.gl.glVertex3d(vertex.x, vertex.y, 0)
                self.gl.glEnd()
        # DUMMY END


        self.gl.glEndList()

        return genList
