class WireRenderer(Renderer):
    def __init__(self, wire, gl):
        super(WireRenderer).__init__(self, gl)
        self.wire = wire
        self.callList = genSymbolCallList(self)
        
    def genSymbolCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        self.gl.glColor4f(0.282, 0.235, 0.196, 1.0)
        
        # TODO: Implement wire rendering
        
        self.gl.glEndList()

        return genList