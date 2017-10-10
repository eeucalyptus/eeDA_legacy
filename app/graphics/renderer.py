import OpenGL.GL as gl

class Renderer:
    def __init__(self):
        self.callList = None
        
    def updateCallList(self):
        gl.glDeleteLists(self.callList, 1)
        self.callList = self.genSymbolCallList()
        
    def setColor(self, color):        # the word 'color' looks weirder the more you look at it.
        gl.glColor4f(*color)# I mean, look at it. It's blatantly 'Coh-lore'.
                                # I could swear it's missing a 'u' somewhere. -- M