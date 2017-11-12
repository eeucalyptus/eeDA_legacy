import math
from data.util import Vector2d, Vector2i
from .shortcut import Shortcut
from PyQt5 import QtWidgets, QtGui, QtCore
from graphics.common import eeDAcolor
from data.util import Grid, Polygon # to be removed
from graphics.drawables import GridDrawable
import graphics.contextrenderers
from PIL import Image, ImageFont, ImageQt, ImageDraw
from data.schematics import Wire

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

        self.initContextMenu()
        self.initShortcuts()


    def mousePressEvent(self, event):
        if(event.buttons() == QtCore.Qt.RightButton):
            self.contextMenu.popup(event.globalPos())


    def mouseMoveEvent(self, event):
        worldCoords = self.widgetCoordsToWorld(event.x(), event.y())
        self.parent().positionWidget.setText("x={}, y={}".format(worldCoords.x, worldCoords.y))
        currentScreenPos = event.screenPos()
        lastExists = self.lastScreenPos != None
        leftPressed = event.buttons() == QtCore.Qt.LeftButton
        if(lastExists and leftPressed):
            dx = self.lastScreenPos.x() - currentScreenPos.x()
            dy = self.lastScreenPos.y() - currentScreenPos.y()

            self.contextRenderer.cameraposition += Vector2d(-dx/self.contextRenderer.zoomLevel, -dy/self.contextRenderer.zoomLevel)

        self.lastScreenPos = currentScreenPos

        # self.renderMouseSnap(worldCoords)
        self.repaint()

        # if self.testWire.selected(worldCoords):
        #     print(str(worldCoords) + " In!")
        # else:
        #     print(str(worldCoords) + " Out!")

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
        deltaX = (ctrX - mouseX) / self.contextRenderer.zoomLevel
        deltaY = (ctrY - mouseY) / self.contextRenderer.zoomLevel
        if direction > 0:
            self.contextRenderer.cameraposition += Vector2d(deltaX * 0.1, deltaY * 0.1)
        self.multZoom(1.0 + direction * 0.1)



    def initializeGL(self):
        version = QtGui.QOpenGLVersionProfile()
        version.setVersion(2, 1)
        self.gl = self.context().versionFunctions(version)
        self.gl.initializeOpenGLFunctions()

        self.gl.glClearColor(*eeDAcolor.SCM_BACKGROUND)
        self.gl.glShadeModel(self.gl.GL_FLAT)
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        self.gl.glEnable(self.gl.GL_BLEND)
        self.gl.glBlendFunc(self.gl.GL_ZERO, self.gl.GL_ONE)
        #self.gl.glCullFace(self.gl.GL_BACK)
        #self.gl.glEnable(self.gl.GL_CULL_FACE)

        self.contextRenderer = graphics.contextrenderers.EmptyContextRenderer(self.gl)

    def paintGL(self):
        self.gl.glClear(
                self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.gl.glLoadIdentity()
        self.gl.glTranslated(self.contextRenderer.cameraposition.x, self.contextRenderer.cameraposition.y, -10.0)
        self.zoomGL()
        self.gl.glEnable(self.gl.GL_MULTISAMPLE)
        self.gl.glEnable(self.gl.GL_BLEND)
        self.gl.glBlendFunc(self.gl.GL_ONE,self.gl.GL_ONE_MINUS_SRC_ALPHA)

        self.contextRenderer.render()

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
        width = self.frameGeometry().width() / self.contextRenderer.zoomLevel
        height = self.frameGeometry().height() / self.contextRenderer.zoomLevel

        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        self.gl.glLoadIdentity()
        self.gl.glOrtho(-0.5*width, +0.5*width, +0.5*height, -0.5*height, 4.0, 15.0)
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)

    def nudgeView(self, delta):
        self.cameraposition += delta/self.contextRenderer.zoomLevel
        print("Nudge, nudge.")
        self.repaint()

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
        self.contextRenderer.zoomLevel = zoomFactor
        self.repaint()

    def multZoom(self, factor):
        self.contextRenderer.zoomLevel *= factor
        self.repaint()

    def recenterView(self):
        print('Recentering view.')
        self.cameraposition = Vector2i()
        self.contextRenderer.zoomLevel = 1.0
        self.repaint()

    def makeGrid(self):
        return Grid()

    def makeGridDrawable(self, grid):
        return GridDrawable(grid, self.gl)

    def widgetCoordsToWorld(self, x, y):
        xAdj = (x - self.frameGeometry().width() / 2 ) / self.contextRenderer.zoomLevel - self.cameraposition.x
        yAdj = (y - self.frameGeometry().height() / 2 ) / self.contextRenderer.zoomLevel - self.cameraposition.y
        return Vector2i(xAdj, yAdj)

    def worldCoordsToWidget(self, x, y):
        xAdj = (x + self.cameraposition.x) * self.contextRenderer.zoomLevel + self.frameGeometry().width() / 2
        yAdj = (y + self.cameraposition.y) * self.contextRenderer.zoomLevel + self.frameGeometry().height() / 2
        return Vector2i(xAdj, yAdj)

    # def renderMouseSnap(self, pos):
    #     snapCoords = self.grid.nearestSnap(pos)
    #     #self.pointList = PointRenderer(self.gl, snapCoords.x, snapCoords.y).genSymbolCallList()

    def initTestWire(self):
        self.testWire = Wire(None)
        self.testWire.connectors[0].pos = Vector2d(-500, -500)
        self.testWire.connectors[1].pos = Vector2d(-400, -350)
        self.testWire.setPoints([Vector2d(-450, -500), Vector2d(-200, -200)])
        self.testWire.initDrawable(self.gl)
        self.testWireList = self.testWire.drawable.callList
