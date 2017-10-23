from PyQt5 import QtWidgets, QtGui
from .renderer import Renderer
from data import util
from .common import eeDAcolor, pMakePolygonArray, pMakeLineArray

class SymbolRenderer(Renderer):
    def __init__(self, symbol, gl):
        super().__init__(gl)
        self.symbol = symbol
        self.callList = self._genCallList()
        print(str(self.symbol) + " has calllist: " + str(self.callList))

    def _genCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)

        self.gl.glEnableClientState(self.gl.GL_VERTEX_ARRAY)
        self.setColor(eeDAcolor.SYMBOL)

        for part in self.symbol.parts:
            if isinstance(part, util.Polygon):
                vertices = pMakePolygonArray(part, self.symbol.pos, 0.8)
                self.gl.glVertexPointer(3, self.gl.GL_FLOAT, 0, vertices)
                self.gl.glDrawArrays(self.gl.GL_TRIANGLES, 0, len(vertices) / 3)

        self.gl.glDisableClientState(self.gl.GL_VERTEX_ARRAY)

        self.gl.glEndList()

        return genList
