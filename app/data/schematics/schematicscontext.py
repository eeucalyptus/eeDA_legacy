from data.common import TabContext

class SchematicsContext(TabContext):
    def __init__(self, schematics = None, page = None):
        self.schematic = None
        self.nets = []
        self.page = None
        
    def setSchematic(self, schematic):
        self.schematic = schematic
        
    def setPage(self, page):
        self.page = page
        