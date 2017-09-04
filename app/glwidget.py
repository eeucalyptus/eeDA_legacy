import math
from PyQt5 import QtWidgets, QtGui

class GLWidget(QtWidgets.QOpenGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.parent().positionWidget.setText("x={}, y={}".format(event.x(), event.y()))
        

    def initializeGL(self):
        version = QtGui.QOpenGLVersionProfile()
        version.setVersion(2, 1)
        self.gl = self.context().versionFunctions(version)
        self.gl.initializeOpenGLFunctions()

        self.gl.glClearColor(0.0, 0.0, 0.0, 1.0)
        self.object1 = self.makeTriangle()
        self.object2 = self.makeQuad()
        self.gl.glShadeModel(self.gl.GL_FLAT)
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        self.gl.glEnable(self.gl.GL_CULL_FACE)
        self.gl.glEnable(self.gl.GL_MULTISAMPLE)

    def paintGL(self):
        self.gl.glClear(
                self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.gl.glLoadIdentity()
        self.gl.glTranslated(0.0, 0.0, -10.0)
        self.gl.glCallList(self.object1)
        self.gl.glCallList(self.object2)

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        self.gl.glViewport((width - side) // 2, (height - side) // 2, side, side)

        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        self.gl.glLoadIdentity()
        self.gl.glOrtho(-0.5*width, +0.5*width, +0.5*height, -0.5*height, 4.0, 15.0)
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)

    def makeTriangle(self):
    
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)

        self.gl.glBegin(self.gl.GL_TRIANGLES)
        
        self.gl.glColor4f(0.282, 0.235, 0.196, 1.0)
        
        for i in range(3):
            angle = 80.0 - i*120.0
            x = 200 * math.cos(math.radians(angle))
            y = 200 * math.sin(math.radians(angle))
            self.gl.glVertex3d(x, y, -0.05)

        self.gl.glEnd()
        
        self.gl.glEndList()

        return genList

    def makeQuad(self):
    
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)

        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)
        self.gl.glPushMatrix()
        self.gl.glLoadIdentity()
        self.gl.glTranslated(400.0, 0.0, -10.0)
        
        self.gl.glColor4f(0.5, 0.5, 0.196, 1.0)
        
        self.gl.glBegin(self.gl.GL_QUADS)
        self.gl.glVertex3d(-50, -50, -0.05)
        self.gl.glVertex3d(-50, +50, -0.05)
        self.gl.glVertex3d(+50, +50, -0.05)
        self.gl.glVertex3d(+50, -50, -0.05)
        self.gl.glEnd()
        
        self.gl.glPopMatrix()
        
        self.gl.glEndList()

        return genList
