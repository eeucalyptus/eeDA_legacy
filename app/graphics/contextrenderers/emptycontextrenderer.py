import data.util

from .contextrenderer import ContextRenderer

class EmptyContextRenderer(ContextRenderer):
    def __init__(self, gl):
        ContextRenderer.__init__(self, gl)
        self.gl = gl

    def render(self):
        # make grid invisible if it'd render too small.
        if (self.zoomLevel * max(self.grid.xRes, self.grid.yRes)) > 10:
            self.gl.glCallList(self.grid.drawable.callList)
