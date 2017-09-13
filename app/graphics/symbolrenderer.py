from PyQt5 import QtWidgets, QtGui
from .renderer import Renderer

class SymbolRenderer(Renderer):
    def __init__(self, symbol, gl):
        super().__init__(gl)
        self.symbol = symbol
        self.callList = self.genSymbolCallList()
        
    def genSymbolCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        
        self.gl.glColor4f(0.9, 0.1, 0.1, 1.0)
        
        # TODO: Replace dummy renderer
        
        # DUMMY
        self.gl.glLineWidth(2.5)
        for polygon in self.symbol.polygons:
            self.gl.glBegin(self.gl.GL_LINE_LOOP)
            for vertex in polygon.points:
                self.gl.glVertex3d(vertex.x, vertex.y, 0)
            self.gl.glEnd()
        # DUMMY END
        
        
        self.gl.glEndList()

        return genList