import uuid

class Component:
    def __init__(self):
        self.uuid = uuid.uuid1()

        self.symbols = []
        self.footprints = []
        self.reference = ''

        self.fields = {}
