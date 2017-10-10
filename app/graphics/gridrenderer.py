from . import Renderer
from data.util import Vector2i, Grid
from .common import eeDAcolor
import OpenGL.GL as gl

class GridRenderer(Renderer):
    def __init__(self, grid):
        super().__init__()
        self.grid = grid
        self.callList = self.genSymbolCallList()
        print("Grid Made")
        
    def genSymbolCallList(self):
        genList = gl.glGenLists(1)
        gl.glNewList(genList, gl.GL_COMPILE)
        self.setColor(eeDAcolor.GRID)
        gl.glDisable(gl.GL_MULTISAMPLE)
        
        gl.glLineWidth(1)
        
        # call some drawing functions
        self.lines = []
        self.addVerticalLine(self.grid.origin.x)
        self.addHorizontalLine(self.grid.origin.y)
        
        for i in range(5000):
            self.addVerticalLine(self.grid.origin.x + self.grid.xRes * i)
            self.addVerticalLine(self.grid.origin.x - self.grid.xRes * i)
            self.addHorizontalLine(self.grid.origin.y + self.grid.xRes * i)
            self.addHorizontalLine(self.grid.origin.y - self.grid.xRes * i)
        
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glVertexPointer(3, gl.GL_FLOAT, 0, self.lines)
        gl.glDrawArrays(gl.GL_LINES, 0, int(len(self.lines) / 3))
        
        gl.glEnable(gl.GL_MULTISAMPLE)
        gl.glEndList()
        
        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        return genList
    
    def addVerticalLine(self, x):
        self.lines += [x, -1000000, 1.0, x, 1000000, 1.0]
    
    def addHorizontalLine(self, y):
        self.lines += [-1000000, y, 1.0, 1000000, y, 1.0]