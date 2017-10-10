from . import Renderer
from PIL import Image, ImageFont, ImageQt, ImageDraw
from PyQt5 import QtGui
import OpenGL.GL as gl
'''

Renders a single line of text at a given position.

'''

class TextRenderer(Renderer):
    
    MSFACTOR = 8
    
    def __init__(self, text, pos, size = 64):
        super().__init__()
        self.text = text
        self.pos = pos
        
        if size > 64:
            self.MSFACTOR = 4
        
        if size > 128:
            self.sizeAdjust = size / 128
            self.fSize = 128
        else:
            self.fSize = size
            self.sizeAdjust = 1
            
        self.callList = self.genSymbolCallList()
        
    def genSymbolCallList(self):
        genList = gl.glGenLists(1)
        
        
        try:
            font = ImageFont.truetype('resources/interface/Roboto.ttf', self.fSize * self.MSFACTOR)
        except OSError:
            print("Font not found, loading failsafe.")
            font = ImageFont.truetype('arial.ttf', self.fSize * self.MSFACTOR)
            # works on Windows; may still fail on Linux and OSX. Documentation unclear.

        textSize = font.getsize(self.text)

        border = 5

        image = Image.new("RGBA", (textSize[0] + 2*border, textSize[1] + 2*border), None)
        draw = ImageDraw.Draw(image)
        draw.text((border, border), self.text, font=font, fill="white")
        del draw
        
        imgWidth = float(self.sizeAdjust * image.size[0] / self.MSFACTOR)
        imgHeight = float(self.sizeAdjust * image.size[1] / self.MSFACTOR)
        
        self.vertices =[0.0, self.fSize - imgHeight, 2.0,
                        0.0, float(self.fSize), 2.0,
                        imgWidth, float(self.fSize), 2.0,
                        imgWidth, self.fSize - imgHeight, 2.0]
        self.texCoords=[0.0, 0.0, 2.0,
                        0.0, 1.0, 2.0,
                        1.0, 1.0, 2.0,
                        1.0, 0.0, 2.0]
        
        self.texture = QtGui.QOpenGLTexture(ImageQt.ImageQt(image), True)
        self.texture.setMinMagFilters(QtGui.QOpenGLTexture.LinearMipMapLinear, QtGui.QOpenGLTexture.Linear)

        gl.glNewList(genList, gl.GL_COMPILE)
        gl.glColor4f(1.0, 1.0, 1.0, 0.0)
        
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glPushMatrix()
        gl.glTranslated(self.pos.x - self.sizeAdjust * (image.size[0] / (2 * self.MSFACTOR) - border), self.pos.y - image.size[1] / (2 * self.MSFACTOR), 0)
        
        self.texture.bind()

        
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glEnableClientState(gl.GL_TEXTURE_COORD_ARRAY)
        gl.glVertexPointer(3, gl.GL_FLOAT, 0, self.vertices)
        gl.glTexCoordPointer(3, gl.GL_FLOAT, 0, self.texCoords)
        
        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.glDrawArrays(gl.GL_QUADS, 0, 4)
        gl.glDisable(gl.GL_TEXTURE_2D)
        
        self.texture.release()

        gl.glPopMatrix()

        gl.glEndList()

        return genList