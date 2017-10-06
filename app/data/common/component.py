import uuid

class Component:
    def __init__(self):
        self.uuid = str(uuid.uuid4())

        self.symbols = []
        self.footprints = []
        self.reference = ''

        self.fields = {}
