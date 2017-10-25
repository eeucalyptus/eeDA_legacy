from graphics.drawables import Drawable
from graphics.common import pMakeCircleArray
from data.util import Vector2i
import math

'''

The JunctionDrawable holds the gl display list for a single junction
and is able to update it, when the underlying junction changes.

'''
class JunctionDrawable(Drawable):

    RESOLUTION = 60

    def __init__(self, junction, gl):
        super().__init__(gl)
        self.junction = junction
        self.callList = self._genCallList()

    def _genCallList(self):
        self.vertices = pMakeCircleArray(self.junction.pos, resolution = self.RESOLUTION)


        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        self.gl.glColor4f(0.75, 1.0, 0.93, 1.0) # the best color in the world

        self.gl.glEnableClientState(self.gl.GL_VERTEX_ARRAY)
        self.gl.glVertexPointer(3, self.gl.GL_FLOAT, 0, self.vertices)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLE_FAN, 0, self.RESOLUTION)
        self.gl.glDisableClientState(self.gl.GL_VERTEX_ARRAY)

        self.gl.glEndList()

        return genList
