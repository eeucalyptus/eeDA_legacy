import data
from data.util import Vector2i
from .contextrenderer import ContextRenderer
import graphics
import gui.util

class TestContextRenderer(ContextRenderer):
    def __init__(self, glWidget):
        self.glWidget = glWidget
        self.gl = glWidget.gl
        self._symbol = self._makeSymbol()
        self._symbolRenderer = self._symbol.drawable
        self._showSymbol = False

        self._wire = self._makeWire()
        self._wireRenderer = self._wire.drawable
        self._showWire = False

        self._junction = self._makeJunction()
        self._junctionRenderer = self._junction.drawable
        self._showJunction = False

        self._rhinoRenderer = self._makeRhino()
        self._showRhino = False



        self._showText = False

    def render(self):
        if self._showSymbol:
            self._symbolRenderer.render()
        if self._showWire:
            self._wireRenderer.render()
        if self._showJunction:
            self._junctionRenderer.render()
        if self._showRhino:
            self._rhinoRenderer.render()

    def _makeTriangle(self):
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

    def _makeQuad(self):
        self.quadPoly = Polygon.fromPoints(Vector2d(0, 0), Vector2d(0, 100),
            Vector2d(100, 100), Vector2d(100, 0))
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

    def _makeSymbol(self):
        # -- symbol
        symbol = data.schematics.Symbol(None, None)
        symbol.addPolygon(data.util.Polygon.fromPoints(\
        Vector2i(-100, -100),\
        Vector2i(-100, 0),\
        Vector2i(0, 0),\
        Vector2i(0, -50),\
        Vector2i(-75, -150),\
        ))
        symbol.pos = Vector2i(300, 200)

        symbol.initDrawable(self.gl)

        return symbol

    def _makeWire(self):
        testWire = data.schematics.Wire(None)
        testWire.setPoints([\
        Vector2i(0, 200),\
        Vector2i(50, 100),\
        Vector2i(100, 200)])

        testWire.connectors[0].pos = Vector2i(-50, 0)
        testWire.connectors[1].pos = Vector2i(150, 0)

        testWire.initDrawable(self.gl)

        return testWire

    def _makeJunction(self):
        testJunction = data.schematics.Junction(None)
        testJunction.setPos(Vector2i(500, 500))
        testJunction.initDrawable(self.gl)
        return testJunction

    def _makeRhino(self):
        renderer = graphics.drawables.RhinocerosDrawable(self.gl)
        return renderer

    def save_handler(self):
        gui.util.UserMessage("Can't save test context")

    def saveAs_handler(self):
        gui.util.UserMessage("Can't save test context")

    def fileInfo_handler(self):
            gui.util.UserMessage("This is a testing context")

    def showWire(self):
        self._showWire = True
        self._showSymbol = False
        self._showSymbol = False
        self._showJunction = False
        self._showRhino = False
        self._showText = False

        self.glWidget.repaint()

    def showSymbol(self):
        self._showWire = False
        self._showSymbol = True
        self._showJunction = False
        self._showRhino = False
        self._showText = False

        self.glWidget.repaint()

    def showJunction(self):
        self._showWire = False
        self._showSymbol = False
        self._showJunction = True
        self._showRhino = False
        self._showText = False

        self.glWidget.repaint()

    def showRhino(self):
        self._showWire = False
        self._showSymbol = False
        self._showJunction = False
        self._showRhino = True
        self._showText = False

        self.glWidget.repaint()

    def showText(self):
        self._showWire = False
        self._showSymbol = False
        self._showJunction = False
        self._showRhino = False
        self._showText = True

        self.glWidget.repaint()
