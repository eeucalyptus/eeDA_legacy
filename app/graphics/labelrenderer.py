class LabelRenderer(Renderer):
    def __init__(self, label, gl):
        super(LabelRenderer).__init__(self, gl)
        self.label = label
        self.callList = self._genCallList()

    def _genCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        self.gl.glColor4f(0.282, 0.235, 0.196, 1.0)

        # TODO: Implement label rendering

        self.gl.glEndList()

        return genList
