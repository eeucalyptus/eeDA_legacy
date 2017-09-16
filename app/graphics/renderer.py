class Renderer:
    def __init__(self, gl):
        self.gl = gl
        self.callList = None
        
    def updateCallList(self):
        self.gl.glDeleteLists(self.callList, 1)
        self.callList = genSymbolCallList(self)
        
    def setColor(self, color):        # the word 'color' looks weirder the more you look at it.
        self.gl.glColor4f(*color)# I mean, look at it. It's blatantly 'Coh-lore'.
                                # I could swear it's missing a 'u' somewhere. -- M