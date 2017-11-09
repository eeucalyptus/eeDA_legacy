from graphics.drawables import Drawable
from graphics.common import eeDAcolor
from data.util import Vector2i, Polygon
from graphics.common import pMakePolygonArray

'''

The RhinocerosRenderer holds the gl display list for a single rhinoceros
and is able to update it, when the underlying biology changes.

'''

class RhinocerosDrawable(Drawable):

    def __init__(self, gl):
        super().__init__(gl)
        self.callList = self._genCallList()

    def _genCallList(self):


        rhinopoly = Polygon.fromPoints(\
        Vector2i(23, 146), #1\
        Vector2i(68, 183), #2\
        Vector2i(66, 163), #3\
        Vector2i(88, 168), #4\
        Vector2i(112, 134), #5\
        Vector2i(100, 132), #6\
        Vector2i(96, 103), #7\
        Vector2i(125, 122), #8\
        Vector2i(116, 115), #9\
        Vector2i(119, 92), #10\
        Vector2i(134, 111), #11\
        Vector2i(157, 92), #12\
        Vector2i(144, 204), #13\
        Vector2i(88, 237), #14\
        Vector2i(72, 240), #15\
        Vector2i(62, 211), #16\
        Vector2i(35, 188)) #17
        self.rhinoVertices = pMakePolygonArray(rhinopoly, Vector2i(), 1)

        self.gl.glColor4f(0.0, 0.0, 1.0, 1.0)
        polly = Polygon.fromPoints(\
        Vector2i(0, 0),\
        Vector2i(25, 0),\
        Vector2i(35, 12),\
        Vector2i(25, 25),\
        Vector2i(0, 25))
        self.quadVertices = pMakePolygonArray(polly, Vector2i(-400, -400), 1)
        # alright, it's not a quadrilateral. I never said I could count... - M
        # --
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        self.gl.glEnableClientState(self.gl.GL_VERTEX_ARRAY)

        self.setColor(eeDAcolor.RHINO)
        self.gl.glVertexPointer(3, self.gl.GL_INT, 0, self.rhinoVertices)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLES, 0, len(self.rhinoVertices) / 3)

        self.setColor(eeDAcolor.WIRE)
        self.gl.glVertexPointer(3, self.gl.GL_INT, 0, self.quadVertices)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLES, 0, len(self.quadVertices) / 3)

        self.gl.glEndList()

        return genList
