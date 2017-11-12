from graphics.drawables import Drawable
from PIL import Image, ImageFont, ImageQt, ImageDraw
from PyQt5 import QtGui
'''

Renders a single line of text at a given position.

'''

class TextRenderer(Drawable):

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

        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        self.gl.glColor4f(1.0, 1.0, 1.0, 0.0)

        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)
        self.gl.glPushMatrix()
        self.gl.glTranslated(self.pos.x - self.sizeAdjust * (image.size[0] / (2 * self.MSFACTOR) - border), self.pos.y - image.size[1] / (2 * self.MSFACTOR), 0)

        self.texture.bind()


        self.gl.glEnableClientState(self.gl.GL_VERTEX_ARRAY)
        self.gl.glEnableClientState(self.gl.GL_TEXTURE_COORD_ARRAY)
        self.gl.glVertexPointer(3, self.gl.GL_FLOAT, 0, self.vertices)
        self.gl.glTexCoordPointer(3, self.gl.GL_FLOAT, 0, self.texCoords)

        self.gl.glEnable(self.gl.GL_TEXTURE_2D)
        self.gl.glDrawArrays(self.gl.GL_QUADS, 0, 4)
        self.gl.glDisable(self.gl.GL_TEXTURE_2D)

        self.texture.release()

        self.gl.glPopMatrix()

        self.gl.glEndList()

        return genList
