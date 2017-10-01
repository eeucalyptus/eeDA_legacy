import math
from data.util import Vector2d, Vector2i
from .shortcut import Shortcut
from PyQt5 import QtWidgets, QtGui, QtCore
from graphics.common import eeDAcolor

from graphics import GridRenderer # to be removed
from data.util import Grid # to be removed
from graphics.common.primitives import PointRenderer
from PIL import Image, ImageFont, ImageQt

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
        self.object3 = self.makeTestText()
        self.gl.glShadeModel(self.gl.GL_FLAT)
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
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
        self.gl.glCallList(self.object1)
        self.gl.glCallList(self.object2)
        self.gl.glCallList(self.object3)
        if self.injectedList != None:
            self.gl.glCallList(self.injectedList)
        if (self.zoomLevel * max(self.grid.xRes, self.grid.yRes)) > 10: # make grid invisible if it'd render too small.
                                                                        # 10 is an empiric value, may not apply to all resolutions.
            self.gl.glCallList(self.gridRenderer.callList)
        if self.pointList != None:
            self.gl.glCallList(self.pointList)
        self.gl.glDisable(self.gl.GL_BLEND)
        self.gl.glDisable(self.gl.GL_MULTISAMPLE)

        p = QtGui.QPainter(self)
        p.setPen(QtGui.QColor(210, 210, 210))
        p.setFont(QtGui.QFont('Comic Sans MS', int(32*self.zoomLevel)))
        p.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)
        textPos = self.worldCoordsToWidget(300, 300)
        p.drawText(textPos.x, textPos.y, 'Who this reads is dumb')
<<<<<<< HEAD
        
        # self.gl.glDeleteLists(self.object3, 1)
        # self.object3 = self.makeTestText()
        
=======

>>>>>>> 0c9a944fc7b61e8e2363873f96662fd9a3da6d38
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
        self.gl.glTranslated(400.0, 400.0, 0)

        self.gl.glColor4f(1.0, 1.0, 1.0, 0.0)

        self.texture = QtGui.QOpenGLTexture(QtGui.QImage('resources/side1.png'), True)
        self.texture.setMinMagFilters(QtGui.QOpenGLTexture.LinearMipMapLinear, QtGui.QOpenGLTexture.Linear)
        self.texture.bind()

        self.gl.glEnable(self.gl.GL_TEXTURE_2D)
        self.gl.glBegin(self.gl.GL_QUADS)

        self.gl.glTexCoord3d(0, 0, -1)
        self.gl.glVertex3d(0, 0, -1)

        self.gl.glTexCoord3d(0, 1, -1)
        self.gl.glVertex3d(0, 100, -1)

        self.gl.glTexCoord3d(1, 1, -1)
        self.gl.glVertex3d(100, 100, -1)

        self.gl.glTexCoord3d(1, 0, -1)
        self.gl.glVertex3d(100, 0, -1)

        self.gl.glEnd()
        self.gl.glDisable(self.gl.GL_TEXTURE_2D)
        self.texture.release()
        self.gl.glPopMatrix()

        self.gl.glEndList()

        return genList
<<<<<<< HEAD
        
    def makeTestText(self):
        
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        

        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)
        self.gl.glPushMatrix()
        self.gl.glTranslated(200.0, 200.0, 0)
        
        self.gl.glColor4f(1.0, 1.0, 1.0, 0.0)
        
        self.textureAry = []
        
        text = 'This is a very long string.'
        fSize = 512
        xPos = 0
        font = ImageFont.truetype('gui/Roboto.ttf', fSize)
        for i, char in enumerate(text):
            if char == ' ':
                xPos += 32
                self.textureAry.append(None)
                continue
            self.charImg = ImageQt.ImageQt(Image.Image()._new(font.getmask(char)))
            
            self.textureAry.append(QtGui.QOpenGLTexture(self.charImg))
            self.textureAry[i].setMinMagFilters(self.gl.GL_NEAREST, self.gl.GL_NEAREST)
            self.textureAry[i].bind()
            
            self.gl.glEnable(self.gl.GL_TEXTURE_2D)
            self.gl.glBegin(self.gl.GL_QUADS)
            
            imgWidth = self.charImg.width() / 8
            imgHeight = self.charImg.height() / 8
            self.gl.glTexCoord3d(0, 0, -1)
            self.gl.glVertex3d(xPos, 64 - imgHeight, -1)
            
            self.gl.glTexCoord3d(0, 1, -1)
            self.gl.glVertex3d(xPos, 64, -1)
            
            self.gl.glTexCoord3d(1, 1, -1)
            self.gl.glVertex3d(xPos + imgWidth, 64, -1)
            
            self.gl.glTexCoord3d(1, 0, -1)
            self.gl.glVertex3d(xPos + imgWidth, 64 - imgHeight, -1)
            
            self.gl.glEnd()
            self.gl.glDisable(self.gl.GL_TEXTURE_2D)
            self.textureAry[i].release()
            
            xPos += imgWidth
        
        fSize = 64
        font = ImageFont.truetype('gui/Roboto.ttf', fSize)
        self.gl.glPopMatrix()

        self.gl.glEndList()

        return genList
        
=======

>>>>>>> 0c9a944fc7b61e8e2363873f96662fd9a3da6d38
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
