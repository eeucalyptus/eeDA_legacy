import uuid

class Schematic:
	def __init__(self):
        self.components = []
        self.nets = []
        self.fields = []
        self.uuid = uuid.uuid1()