class SchematicsElement:
    def __init__(self, page = None):
        self.page = page
        self.renderer = self.createRenderer()
        
    def createRenderer(self):
        return None # abstract, to be re-implemented in every subclass that has a renderer.
    
    def selected(self, pos):    # re-implement in subclasses
        return False