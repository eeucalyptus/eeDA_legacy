from . import Renderer
from .common import pRenderCircle, pRenderPolygon, eeDAcolor
from data.util import Vector2i, Polygon
'''

The RhinocerosRenderer holds the gl display list for a single rhinoceros
and is able to update it, when the underlying biology changes.

'''

class RhinocerosRenderer(Renderer):
    
    def __init__(self, gl):
        super().__init__(gl)
        self.callList = self.genSymbolCallList()
        
    def genSymbolCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        #self.gl.glColor4f(0.75, 1.0, 0.93, 1.0) # the best color in the world
        self.setColor(eeDAcolor.RHINO)
        
        
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
        pRenderPolygon(self, rhinopoly, Vector2i())
        

        # -- some additional testing of the new primitive renderers
        self.gl.glColor4f(0.0, 1.0, 0.0, 1.0)
        pRenderCircle(self, Vector2i(-200, -200), 25)
        self.gl.glColor4f(0.0, 0.0, 1.0, 1.0)
        polly = Polygon.fromPoints(\
        Vector2i(0, 0),\
        Vector2i(25, 0),\
        Vector2i(35, 12),\
        Vector2i(25, 25),\
        Vector2i(0, 25))
        pRenderPolygon(self, polly, Vector2i(-400, -400))
        # --
        self.gl.glEndList()

        return genList
        