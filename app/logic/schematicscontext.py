from logic import fileloaders
import graphics
from data.util import Vector2i, Vector2d
from .filecontext import FileContext

class SchematicsContext(FileContext):
    def __init__(self, filepath):
        self._filepath = filepath
        schematicsloader = fileloaders.SchematicsLoader(filepath)
        self._schematics = schematicsloader.loadSchematic()
        self._camera_center = Vector2d()
        self._zoom = 1
        self._currentPageIndex = 0

    def initRenderers(self, gl):
        self.contextRenderer = graphics.SchematicsContextRenderer(self, gl)

        for page in self._schematics.pages:
            for element in page.elements:
                if element:
                    element.initRenderer(gl)

    def currentPage(self):
        i = self._currentPageIndex
        page = self._schematics.pages[i]
        return page
