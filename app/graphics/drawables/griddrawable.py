from graphics.drawables import Drawable
from data.util import Vector2i, Grid
from graphics.common import eeDAcolor

class GridDrawable(Drawable):
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
        self.lines = []
        self.addVerticalLine(self.grid.origin.x)
        self.addHorizontalLine(self.grid.origin.y)

        for i in range(5000):
            self.addVerticalLine(self.grid.origin.x + self.grid.xRes * i)
            self.addVerticalLine(self.grid.origin.x - self.grid.xRes * i)
            self.addHorizontalLine(self.grid.origin.y + self.grid.xRes * i)
            self.addHorizontalLine(self.grid.origin.y - self.grid.xRes * i)

        self.gl.glEnableClientState(self.gl.GL_VERTEX_ARRAY)
        self.gl.glVertexPointer(3, self.gl.GL_FLOAT, 0, self.lines)
        self.gl.glDrawArrays(self.gl.GL_LINES, 0, len(self.lines) / 3)

        self.gl.glEnable(self.gl.GL_MULTISAMPLE)
        self.gl.glEndList()

        self.gl.glDisableClientState(self.gl.GL_VERTEX_ARRAY)
        return genList

    def addVerticalLine(self, x):
        self.lines += [x, -1000000, 1.0, x, 1000000, 1.0]

    def addHorizontalLine(self, y):
        self.lines += [-1000000, y, 1.0, 1000000, y, 1.0]
