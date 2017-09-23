from data.common import TabContext

class SchematicsContext(TabContext):
    def __init__(self, schematic = None, page = None):
        self.schematic = schematic
        self.nets = []
        self.page = page
        
    def setSchematic(self, schematic):
        self.schematic = schematic
        
    def setPage(self, page):
        self.page = page
        