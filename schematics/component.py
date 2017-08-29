import uuid
from . import Model

class Component:
    def __init__(self, model):
        self.model = model
        self. description = model.description
        self.name = model.name
        self.reference = model.referenceprefix + '#'
        self.fields = model.fields
        self.uuid = uuid.uuid1()