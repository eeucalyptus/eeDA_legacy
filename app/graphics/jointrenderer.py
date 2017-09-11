class JointRenderer(Renderer):
    def __init__(self, joint, gl):
        super(JointRenderer).__init__(self, gl)
        self.joint = joint
        self.callList = genSymbolCallList(self)
        
    def genSymbolCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        self.gl.glColor4f(0.282, 0.235, 0.196, 1.0)
        
        # TODO: Implement joint rendering
        
        self.gl.glEndList()

        return genList