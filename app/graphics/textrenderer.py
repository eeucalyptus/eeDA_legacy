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
        genList = self.gl.glGenLists(1)
        
        
        try:
            font = ImageFont.truetype('resources/interface/Roboto.ttf', self.fSize * self.MSFACTOR)
        except OSError:
            print("Font not found, loading failsafe.")
            font = ImageFont.truetype('arial.ttf', self.fSize * self.MSFACTOR)
        

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
        self.gl.glTranslated(self.pos.x - self.sizeAdjust * (image.size[0] / (2 * self.MSFACTOR) - border), self.pos.y - image.size[1] / (2 * self.MSFACTOR), 0)
        
        self.text_texture.bind()

        self.gl.glEnable(self.gl.GL_TEXTURE_2D)
        self.gl.glBegin(self.gl.GL_QUADS)

        imgWidth = self.sizeAdjust * image.size[0] / self.MSFACTOR
        imgHeight = self.sizeAdjust * image.size[1] / self.MSFACTOR
        
        self.gl.glTexCoord3d(0, 0, -0.01)
        self.gl.glVertex3d(0, self.fSize - imgHeight, -0.01)

        self.gl.glTexCoord3d(0, 1, -0.01)
        self.gl.glVertex3d(0, self.fSize, -0.01)

        self.gl.glTexCoord3d(1, 1, -0.01)
        self.gl.glVertex3d(imgWidth, self.fSize, -0.01)

        self.gl.glTexCoord3d(1, 0, -0.01)
        self.gl.glVertex3d(imgWidth, self.fSize - imgHeight, -0.01)

        self.gl.glEnd()
        self.gl.glDisable(self.gl.GL_TEXTURE_2D)
        self.text_texture.release()

        self.gl.glPopMatrix()

        self.gl.glEndList()

        return genList