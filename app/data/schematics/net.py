import uuid

 class Net:
    def __init__(self):
        self.name = ''
        self.connections = []
        self.junctions = []
        self.wires = []
        self.fields = {}
        self.uuid = uuid.uuid1()