from PyQt5 import QtWidgets, QtGui

class SymbolRenderer(Renderer):
    def __init__(self, symbol, gl):
        super(SymbolRenderer).__init__(self, gl)
        self.symbol = symbol
        self.callList = genSymbolCallList(self)
        
    def genSymbolCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        
        self.gl.glColor4f(0.282, 0.235, 0.196, 1.0)
        
        # TODO: Replace dummy renderer
        
        # DUMMY
        for polygon in self.symbol.polygons:
            self.gl.glBegin(self.gl.GL_LINE_LOOP)
            for vertex in system.polygons:
                self.gl.glVertex3d(vertex.x, vertex.y, 0)
            self.gl.glEnd()
        # DUMMY END
        
        
        self.gl.glEndList()

        return genList