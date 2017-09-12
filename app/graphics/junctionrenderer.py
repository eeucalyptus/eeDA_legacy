'''

The JunctionRenderer holds the gl display list for a single junction
and is able to update it, when the underlying junction changes.

'''

class JunctionRenderer(Renderer):
    def __init__(self, junction, gl):
        super(JunctionRenderer).__init__(self, gl)
        self.junction = junction
        self.callList = genSymbolCallList(self)
        
    def genSymbolCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        self.gl.glColor4f(0.282, 0.235, 0.196, 1.0)
        
        # TODO: Implement junction rendering
        
        self.gl.glEndList()

        return genList