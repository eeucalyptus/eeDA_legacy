import math
from data.util import Vector2d, Vector2i
from .shortcut import Shortcut
from PyQt5 import QtWidgets, QtGui, QtCore
from graphics.common import eeDAcolor

from graphics import GridRenderer, TextRenderer # to be removed
from data.util import Grid # to be removed
from graphics.common.primitives import PointRenderer
from PIL import Image, ImageFont, ImageQt, ImageDraw

# Be aware that calls to parent() may fail because the parent is now an EditFrame, not the main window -- M

class GLWidget(QtWidgets.QOpenGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        surfFormat = QtGui.QSurfaceFormat()
        surfFormat.setSamples(16)
        self.setFormat(surfFormat)

        self.setMouseTracking(True)
        self.cameraposition = Vector2d()
        self.lastScreenPos = None

        self.zoomLevel = 1.0
        self.initContextMenu()
        self.initShortcuts()

        self.injectedList = None

        self.pointList = None # debug


    def mousePressEvent(self, event):
        if(event.buttons() == QtCore.Qt.RightButton):
            self.contextMenu.popup(event.globalPos())

        if(event.buttons() == QtCore.Qt.LeftButton):
            currentScreenPos = event.globalPos()
            self.buttonDownScreenPos = currentScreenPos
            self.buttonDownCameraPos = self.cameraposition

    def setInject(self, genList):
        self.injectedList = genList

    def mouseMoveEvent(self, event):
        worldCoords = self.widgetCoordsToWorld(event.x(), event.y())
        self.parent().positionWidget.setText("x={}, y={}".format(worldCoords.x, worldCoords.y))
        currentScreenPos = event.screenPos()
        lastExists = self.lastScreenPos != None
        leftPressed = event.buttons() == QtCore.Qt.LeftButton
        if(lastExists and leftPressed):
            dx = self.lastScreenPos.x() - currentScreenPos.x()
            dy = self.lastScreenPos.y() - currentScreenPos.y()

            self.cameraposition += Vector2d(-dx/self.zoomLevel, -dy/self.zoomLevel)

        self.lastScreenPos = currentScreenPos

        self.renderMouseSnap(worldCoords)
        self.repaint()
        if(event.buttons() == QtCore.Qt.LeftButton):
            pass

    def leaveEvent(self, event):
            self.parent().positionWidget.setText("x= , y=")
            self.pointList = None
            self.repaint()

    def wheelEvent(self, event): # feel free to re-implement. I know this sucks :)
        direction = event.angleDelta().y()/120
        mousePos = event.pos()
        mouseX = mousePos.x()
        mouseY = mousePos.y()
        ctrX = self.frameGeometry().width()/2
        ctrY = self.frameGeometry().height()/2
        deltaX = (ctrX - mouseX) / self.zoomLevel
        deltaY = (ctrY - mouseY) / self.zoomLevel
        if direction > 0:
            self.cameraposition += Vector2d(deltaX * 0.1, deltaY * 0.1)
        self.multZoom(1.0 + direction * 0.1)



    def initializeGL(self):
        version = QtGui.QOpenGLVersionProfile()
        version.setVersion(2, 1)
        self.gl = self.context().versionFunctions(version)
        self.gl.initializeOpenGLFunctions()

        self.gl.glClearColor(*eeDAcolor.SCM_BACKGROUND)
        self.object1 = self.makeTriangle()
        self.object2 = self.makeQuad()
        self.gl.glShadeModel(self.gl.GL_FLAT)
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        self.gl.glEnable(self.gl.GL_BLEND)
        self.gl.glBlendFunc(self.gl.GL_ZERO, self.gl.GL_ONE)
        #self.gl.glCullFace(self.gl.GL_BACK)
        #self.gl.glEnable(self.gl.GL_CULL_FACE)
        self.initGrid()

    def paintGL(self):
        self.gl.glClear(
                self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.gl.glLoadIdentity()
        self.gl.glTranslated(self.cameraposition.x, self.cameraposition.y, -10.0)
        self.zoomGL()
        self.gl.glEnable(self.gl.GL_MULTISAMPLE)
        self.gl.glEnable(self.gl.GL_BLEND)
        self.gl.glBlendFunc(self.gl.GL_ONE,self.gl.GL_ONE_MINUS_SRC_ALPHA)
        self.gl.glCallList(self.object1)
        self.gl.glCallList(self.object2)
        if (self.zoomLevel * max(self.grid.xRes, self.grid.yRes)) > 10: # make grid invisible if it'd render too small.
                                                                        # 10 is an empiric value, may not apply to all resolutions.
            self.gl.glCallList(self.gridRenderer.callList)
        if self.pointList != None:
            self.gl.glCallList(self.pointList)
        if self.injectedList != None:
            self.gl.glCallList(self.injectedList)
        self.gl.glDisable(self.gl.GL_BLEND)
        self.gl.glDisable(self.gl.GL_MULTISAMPLE)

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        self.gl.glViewport((width - side) // 2, (height - side) // 2, side, side)

        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        self.gl.glLoadIdentity()
        self.gl.glOrtho(-0.5*width, +0.5*width, +0.5*height, -0.5*height, 4.0, 15.0)
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)

    def zoomGL(self):
        width = self.frameGeometry().width() / self.zoomLevel
        height = self.frameGeometry().height() / self.zoomLevel

        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        self.gl.glLoadIdentity()
        self.gl.glOrtho(-0.5*width, +0.5*width, +0.5*height, -0.5*height, 4.0, 15.0)
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)

    def nudgeView(self, delta):
        self.cameraposition += delta/self.zoomLevel
        print("Nudge, nudge.")
        self.repaint()

    def makeTriangle(self):

        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        self.gl.glBegin(self.gl.GL_TRIANGLES)

        self.gl.glColor4f(0.282, 0.235, 0.196, 1.0)

        vertices = []
        
        for i in range(3):
            angle = 80.0 - i*120.0
            x = 200 * math.cos(math.radians(angle))
            y = 200 * math.sin(math.radians(angle))
            vertices += [x, y, -0.2]

        
        self.gl.glEnableClientState(self.gl.GL_VERTEX_ARRAY)
        self.gl.glVertexPointer(3, self.gl.GL_INT, 0, vertices)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLES, 0, 3)
        self.gl.glDisableClientState(self.gl.GL_VERTEX_ARRAY)

        self.gl.glEndList()

        return genList

    def makeQuad(self):
        self.quadVertices = (0, 0, -1, 0, 100, -1, 100, 100, -1, 100, 0, -1)
        self.quadTexCoords = (0, 0, -1, 0, 1, -1, 1, 1, -1, 1, 0, -1)
        self.texture = QtGui.QOpenGLTexture(QtGui.QImage('resources/side1.png'), True)
        self.texture.setMinMagFilters(QtGui.QOpenGLTexture.LinearMipMapLinear, QtGui.QOpenGLTexture.Linear)
        # if these lines can stay above the call to glGenLists(), performance should be better, right?
        # every renderer should be able to store their own vertex and texture arrays (or tuples) and textures.
        
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)

        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)
        self.gl.glPushMatrix()
        self.gl.glTranslated(400.0, 400.0, 0)

        self.gl.glColor4f(1.0, 1.0, 1.0, 1.0)

        self.texture.bind()
        
        self.gl.glEnableClientState(self.gl.GL_VERTEX_ARRAY)
        self.gl.glEnableClientState(self.gl.GL_TEXTURE_COORD_ARRAY)
        self.gl.glVertexPointer(3, self.gl.GL_INT, 0, self.quadVertices)
        self.gl.glTexCoordPointer(3, self.gl.GL_INT, 0, self.quadTexCoords)
        
        self.gl.glEnable(self.gl.GL_TEXTURE_2D)
        self.gl.glDrawArrays(self.gl.GL_QUADS, 0, 4)
        self.gl.glDisable(self.gl.GL_TEXTURE_2D)
        
        self.gl.glDisableClientState(self.gl.GL_VERTEX_ARRAY)
        self.gl.glDisableClientState(self.gl.GL_TEXTURE_COORD_ARRAY)
        
        self.texture.release()
        self.gl.glPopMatrix()

        self.gl.glEndList()
        
        return genList

    def initContextMenu(self):
        self.contextMenu = QtWidgets.QMenu()
        self.contextMenu.addAction(_('Check baby!'))
        zoomMenu = self.contextMenu.addMenu('Zoom')

        zoomLow = QtWidgets.QAction('50%', zoomMenu)
        zoomLow.triggered.connect(lambda: self.changeZoom('low'))
        zoomMenu.addAction(zoomLow)

        zoomMid = QtWidgets.QAction('100%', zoomMenu)
        zoomMid.triggered.connect(lambda: self.changeZoom('mid'))
        zoomMenu.addAction(zoomMid)

        zoomHi = QtWidgets.QAction('150%', zoomMenu)
        zoomHi.triggered.connect(lambda: self.changeZoom('hi'))
        zoomMenu.addAction(zoomHi)

    def initShortcuts(self):
        self.addAction(Shortcut(self, "Ctrl+S", lambda: print("Success!")).act)
        # nudge left
        self.addAction(Shortcut(self, "Ctrl+Left", lambda: self.nudgeView(Vector2d(50.0, 0))).act)
        # nudge right
        self.addAction(Shortcut(self, "Ctrl+Right", lambda: self.nudgeView(Vector2d(-50.0,0))).act)
        # nudge up
        self.addAction(Shortcut(self, "Ctrl+Up", lambda: self.nudgeView(Vector2d(0,50.0))).act)
        # nudge down
        self.addAction(Shortcut(self, "Ctrl+Down", lambda: self.nudgeView(Vector2d(0,-50.0))).act)
        # recenter view
        self.addAction(Shortcut(self, "Home", lambda: self.recenterView()).act)

    def changeZoom(self, key):
        zoomFactor = {'low': 0.5,
                      'mid': 1.0,
                      'hi': 1.5}.get(key, 1.0)
        print('Changing zoom level to ' + str(zoomFactor))
        self.zoomLevel = zoomFactor
        self.repaint()

    def multZoom(self, factor):
        self.zoomLevel *= factor
        self.repaint()

    def recenterView(self):
        print('Recentering view.')
        self.cameraposition = Vector2i()
        self.zoomLevel = 1.0
        self.repaint()

    def initGrid(self):
        self.grid = self.makeGrid()
        self.gridRenderer = self.makeGridRenderer(self.grid)

    def makeGrid(self):
        return Grid()

    def makeGridRenderer(self, grid):
        return GridRenderer(grid, self.gl)

    def widgetCoordsToWorld(self, x, y):
        xAdj = (x - self.frameGeometry().width() / 2 ) / self.zoomLevel - self.cameraposition.x
        yAdj = (y - self.frameGeometry().height() / 2 ) / self.zoomLevel - self.cameraposition.y
        return Vector2i(xAdj, yAdj)

    def worldCoordsToWidget(self, x, y):
        xAdj = (x + self.cameraposition.x) * self.zoomLevel + self.frameGeometry().width() / 2
        yAdj = (y + self.cameraposition.y) * self.zoomLevel + self.frameGeometry().height() / 2
        return Vector2i(xAdj, yAdj)

    def renderMouseSnap(self, pos):
        snapCoords = self.grid.nearestSnap(pos)
        self.pointList = PointRenderer(self.gl, snapCoords.x, snapCoords.y).genSymbolCallList()
        