from data import schematics

from .contextrenderer import ContextRenderer

class SchematicsContextRenderer(ContextRenderer):
    def __init__(self, schematicsContext, gl):
         self.gl = gl
         self.schematicsContext = schematicsContext

    def render(self):
        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.gl.glLoadIdentity()
        #self.gl.glTranslated(self.cameraposition.x, self.cameraposition.y, -10.0)
        #self.zoomGL()
        self.gl.glEnable(self.gl.GL_MULTISAMPLE)
        self.gl.glEnable(self.gl.GL_BLEND)
        self.gl.glBlendFunc(self.gl.GL_ONE,self.gl.GL_ONE_MINUS_SRC_ALPHA)

        elements = self.schematicsContext.currentPage().elements
        for element in elements:
            if element and element.renderer != None:
                print("rendering:")
                print(element)
                self.gl.glCallList(element.renderer.callList)

        self.gl.glDisable(self.gl.GL_BLEND)
        self.gl.glDisable(self.gl.GL_MULTISAMPLE)
