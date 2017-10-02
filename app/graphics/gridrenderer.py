from . import Renderer
from data.util import Vector2i, Grid
from .common import eeDAcolor

class GridRenderer(Renderer):
    def __init__(self, grid, gl):
        super().__init__(gl)
        self.grid = grid
        self.callList = self.genSymbolCallList()
        print("Grid Made")
        
    def genSymbolCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        self.setColor(eeDAcolor.GRID)
        self.gl.glDisable(self.gl.GL_MULTISAMPLE)
        
        self.gl.glLineWidth(1)
        
        # call some drawing functions
        
        self.renderVerticalLine(self.grid.origin.x)
        self.renderHorizontalLine(self.grid.origin.y)
        
        for i in range(5000):
            self.renderVerticalLine(self.grid.origin.x + self.grid.xRes * i)
            self.renderVerticalLine(self.grid.origin.x - self.grid.xRes * i)
            self.renderHorizontalLine(self.grid.origin.y + self.grid.xRes * i)
            self.renderHorizontalLine(self.grid.origin.y - self.grid.xRes * i)
        self.gl.glEnable(self.gl.GL_MULTISAMPLE)
        self.gl.glEndList()
        
        
        return genList
    
    def renderVerticalLine(self, x):
        self.gl.glBegin(self.gl.GL_LINES)
        self.gl.glVertex3d(x, -1000000, -0.02)
        self.gl.glVertex3d(x, 1000000, -0.02)
        self.gl.glEnd()
    
    def renderHorizontalLine(self, y):
        self.gl.glBegin(self.gl.GL_LINES)
        self.gl.glVertex3d(-1000000, y, -0.02)
        self.gl.glVertex3d(1000000, y, -0.02)
        self.gl.glEnd()