import OpenGL.GL as gl

class LabelRenderer(Renderer):
    def __init__(self, label):
        super(LabelRenderer).__init__(self)
        self.label = label
        self.callList = genSymbolCallList(self)
        
    def genSymbolCallList(self):
        genList = gl.glGenLists(1)
        gl.glNewList(genList, gl.GL_COMPILE)
        gl.glColor4f(0.282, 0.235, 0.196, 1.0)
        
        # TODO: Implement label rendering
        
        gl.glEndList()

        return genList