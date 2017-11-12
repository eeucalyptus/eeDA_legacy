import data.util

class ContextRenderer:
    def __init__(self, gl):
        self.grid = data.util.Grid()
        self.grid.initDrawable(gl)
        self.zoomLevel = 1.0
        self.cameraposition = data.util.Vector2i()

    def render(self):
        pass
