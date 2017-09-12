import uuid

class Symbol:
    def __init__(self, component):
        self.uuid = uuid.uuid1();
        self.component = component
        
        self.renderer = None
        
        self.connectors = []
        self.parts = []