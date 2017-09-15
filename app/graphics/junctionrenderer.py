from . import Renderer
from data.util import Vector2i
import math
'''

The JunctionRenderer holds the gl display list for a single junction
and is able to update it, when the underlying junction changes.

'''

class JunctionRenderer(Renderer):
    
    RESOLUTION = 120
    
    def __init__(self, junction, gl):
        super().__init__(gl)
        self.junction = junction
        self.callList = self.genSymbolCallList()
        
    def genSymbolCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        self.gl.glColor4f(0.75, 1.0, 0.93, 1.0) # the best color in the world
        
        # HALFDONE: Implement junction rendering
        self.drawCircle(self.junction.pos, 7.5)
        
        self.gl.glEndList()

        return genList
        
    def drawCircle(self, center, radius):
        self.gl.glBegin(self.gl.GL_TRIANGLE_FAN)
        self.gl.glVertex3d(center.x, center.y, 1.1) # centroid
    
        for i in range(JunctionRenderer.RESOLUTION + 1):
            x = center.x + math.cos(2 * math.pi * i/float(JunctionRenderer.RESOLUTION)) * radius
            y = center.y - math.sin(2 * math.pi * i/float(JunctionRenderer.RESOLUTION)) * radius
            self.gl.glVertex3d(x, y, 1.1)           # outer vertices
    
    
        self.gl.glVertex3d(center.x, center.y, 1.1) # centroid again
        self.gl.glEnd()