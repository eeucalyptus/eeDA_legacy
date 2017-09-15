from . import Renderer

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
        self.gl.glColor4f(0.75, 1.0, 0.93, 1.0) # the best color in the world
        
        self.gl.glLineWidth(4.0)
        self.gl.glBegin(self.gl.GL_LINE_LOOP)
        self.gl.glVertex3d(23, 146, 1.1) #1
        self.gl.glVertex3d(68, 183, 1.1) #2
        self.gl.glVertex3d(66, 163, 1.1) #3
        self.gl.glVertex3d(88, 168, 1.1) #4
        self.gl.glVertex3d(112, 134, 1.1) #5
        self.gl.glVertex3d(100, 132, 1.1) #6
        self.gl.glVertex3d(96, 103, 1.1) #7
        self.gl.glVertex3d(125, 122, 1.1) #8
        self.gl.glVertex3d(116, 115, 1.1) #9
        self.gl.glVertex3d(119, 92, 1.1) #10
        self.gl.glVertex3d(134, 111, 1.1) #11
        self.gl.glVertex3d(157, 92, 1.1) #12
        self.gl.glVertex3d(144, 204, 1.1) #13
        self.gl.glVertex3d(88, 237, 1.1) #14
        self.gl.glVertex3d(72, 240, 1.1) #15
        self.gl.glVertex3d(62, 211, 1.1) #16
        self.gl.glVertex3d(35, 188, 1.1) #17
        self.gl.glVertex3d(23, 146, 1.1) #1
        
        
        
        
        self.gl.glEnd()
        
        
        
        self.gl.glEndList()

        return genList
        