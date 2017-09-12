import uuid

class Schematic:
    def __init__(self):
        self.uuid = uuid.uuid1();
        
        self.pages = []
        self.fields = {}
        