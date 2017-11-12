from logic import filehandlers
import graphics.contextrenderers
from data.util import Vector2i, Vector2d
from logic.filecontext import FileContext

class SchematicsContext(FileContext):
    def __init__(self, filepath):
        self._filepath = filepath
        schematicsfilehandler = filehandlers.SchematicsFileHandler(filepath)
        self._schematics = schematicsfilehandler.loadSchematic()
        self._camera_center = Vector2d()
        self._zoom = 1
        self._currentPageIndex = 0

    def initDrawables(self, gl):
        self.contextRenderer = graphics.contextrenderers.SchematicsContextRenderer(self, gl)

        for page in self._schematics.pages:
            for element in page.elements:
                if element:
                    element.initDrawable(gl)

    def currentPage(self):
        i = self._currentPageIndex
        page = self._schematics.pages[i]
        return page
