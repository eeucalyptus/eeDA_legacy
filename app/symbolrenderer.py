from PyQt5 import QtWidgets, QtGui

def getSymbolCallList(gl, symbol):
    genList = self.gl.glGenLists(1)
    self.gl.glNewList(genList, self.gl.GL_COMPILE)

    
    self.gl.glColor4f(0.282, 0.235, 0.196, 1.0)
    
    for polygon in symbol.polygons:
        self.gl.glBegin(self.gl.GL_LINE_LOOP)
        for vertex in system.polygons:
            self.gl.glVertex3d(vertex.x, vertex.y, 0)
        self.gl.glEnd()
    
    self.gl.glEndList()

    return genList