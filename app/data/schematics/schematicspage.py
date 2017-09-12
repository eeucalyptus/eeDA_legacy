import uuid

class SchematicsPage:
    def __init__(self, schematic):
        self.uuid = uuid.uuid1();
        
        self.schematic = schematic
        
        self.symbols = []
        self.decorations = []
        self.junctions = []
        self.labels = []
        self.wires = []