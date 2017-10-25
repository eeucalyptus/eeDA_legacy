from data import util

class SchematicsElement:
    def __init__(self, page = None):
        self.page = page
        self.pos = util.Vector2i()
        self.drawable = None

    def initDrawable(self, gl):
        pass
