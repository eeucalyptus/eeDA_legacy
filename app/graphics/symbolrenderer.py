from PyQt5 import QtWidgets, QtGui
from .renderer import Renderer
from .common import eeDAcolor, pMakePolygonArray, pMakeLineArray
import OpenGL.GL as gl

class SymbolRenderer(Renderer):
    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol
        self.callList = self.genSymbolCallList()
        
    def genSymbolCallList(self):
        genList = gl.glGenLists(1)
        gl.glNewList(genList, gl.GL_COMPILE)
        
        
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        
        self.setColor(eeDAcolor.SYMBOL)
        for polygon in self.symbol.polygons:
            vertices = pMakePolygonArray(polygon, self.symbol.pos, 0.8)
            gl.glVertexPointer(3, gl.GL_FLOAT, 0, vertices)
            gl.glDrawArrays(gl.GL_TRIANGLES, 0, len(vertices) / 3)
            
        self.setColor(eeDAcolor.SYMBOL2)
        for linestrip in self.symbol.linestrips:
            vertices = pMakeLineArray(linestrip.points, self.symbol.pos, 3.0, 0.9)
            gl.glVertexPointer(3, gl.GL_FLOAT, 0, vertices)
            gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, len(vertices) / 3)
            
        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        
        gl.glEndList()

        return genList