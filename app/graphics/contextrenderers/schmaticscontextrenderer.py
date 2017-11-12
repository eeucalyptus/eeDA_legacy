import data.schematics
import data.util

from .contextrenderer import ContextRenderer

class SchematicsContextRenderer(ContextRenderer):
    def __init__(self, schematicsContext, gl):
        ContextRenderer.__init__(self, gl)
        self.gl = gl
        self.schematicsContext = schematicsContext

    def render(self):
        elements = self.schematicsContext.currentPage().elements
        for element in elements:
            if element and element.drawable != None:
                print("rendering: " + str(element) + " Calllist: " + str(element.drawable.callList))
                self.gl.glCallList(element.drawable.callList)

        # make grid invisible if it'd render too small.
        if (self.zoomLevel * max(self.grid.xRes, self.grid.yRes)) > 10:
            self.gl.glCallList(self.grid.drawable.callList)
