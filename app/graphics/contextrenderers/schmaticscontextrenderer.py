from data import schematics

from .contextrenderer import ContextRenderer

class SchematicsContextRenderer(ContextRenderer):
    def __init__(self, schematicsContext, gl):
         self.gl = gl
         self.schematicsContext = schematicsContext

    def render(self):
        elements = self.schematicsContext.currentPage().elements
        for element in elements:
            if element and element.drawable != None:
                print("rendering: " + str(element) + " Calllist: " + str(element.drawable.callList))
                self.gl.glCallList(element.drawable.callList)
