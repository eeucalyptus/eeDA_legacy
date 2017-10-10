import OpenGL.GL as gl

class DecorationRenderer(Renderer):
    def __init__(self, decoration):
        super(DecorationRenderer).__init__(self)
        self.decoration = decoration
        self.callList = genSymbolCallList(self)
        
    def genSymbolCallList(self):
        genList = gl.glGenLists(1)
        gl.glNewList(genList, gl.GL_COMPILE)
        gl.glColor4f(0.282, 0.235, 0.196, 1.0)
        
        # TODO: Implement decoration rendering
        
        gl.glEndList()

        return genList