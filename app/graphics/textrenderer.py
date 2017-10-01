from . import Renderer
from PIL import Image, ImageFont, ImageQt, ImageDraw
from PyQt5 import QtGui
'''

Renders a single line of text at a given position.

'''

class TextRenderer(Renderer):
    
    MSFACTOR = 8
    
    def __init__(self, gl, text, pos, size = 64):
        super().__init__(gl)
        self.text = text
        self.pos = pos
        self.fSize = size
        self.callList = self.genSymbolCallList()
        
    def genSymbolCallList(self):
        genList = self.gl.glGenLists(1)
        
        
        try:
            font = ImageFont.truetype('resources/Roboto.ttf', self.fSize * self.MSFACTOR)
        except OSError:
            font = ImageFont.truetype('OpenSans-Regular.ttf', self.fSize * self.MSFACTOR)
        

        textSize = font.getsize(self.text)

        border = 5

        image = Image.new("RGBA", (textSize[0] + 2*border, textSize[1] + 2*border), None)
        draw = ImageDraw.Draw(image)
        draw.text((border, border), self.text, font=font, fill="white")
        del draw
        
        
        self.text_texture = QtGui.QOpenGLTexture(ImageQt.ImageQt(image), True)
        self.text_texture.setMinMagFilters(QtGui.QOpenGLTexture.LinearMipMapLinear, QtGui.QOpenGLTexture.Linear)

        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        self.gl.glColor4f(1.0, 1.0, 1.0, 0.0)
        
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)
        self.gl.glPushMatrix()
        self.gl.glTranslated(self.pos.x - image.size[0] / (2 * self.MSFACTOR) - border, self.pos.y - image.size[1] / (2 * self.MSFACTOR) - border, 0)
        
        self.text_texture.bind()

        self.gl.glEnable(self.gl.GL_TEXTURE_2D)
        self.gl.glBegin(self.gl.GL_QUADS)

        imgWidth = image.size[0] / self.MSFACTOR
        imgHeight = image.size[1] / self.MSFACTOR
        self.gl.glTexCoord3d(0, 0, -1)
        self.gl.glVertex3d(0, self.fSize - imgHeight, -1)

        self.gl.glTexCoord3d(0, 1, -1)
        self.gl.glVertex3d(0, self.fSize, -1)

        self.gl.glTexCoord3d(1, 1, -1)
        self.gl.glVertex3d(imgWidth, self.fSize, -1)

        self.gl.glTexCoord3d(1, 0, -1)
        self.gl.glVertex3d(imgWidth, self.fSize - imgHeight, -1)

        self.gl.glEnd()
        self.gl.glDisable(self.gl.GL_TEXTURE_2D)
        self.text_texture.release()

        self.gl.glPopMatrix()

        self.gl.glEndList()

        return genList