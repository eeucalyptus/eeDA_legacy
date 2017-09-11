class Renderer:
    def __init__(self, gl):
        self.gl = gl
        self.callList = None
        
    def updateCallList(self):
        self.gl.glDeleteLists(self.callList, 1)
        self.callList = genSymbolCallList(self)