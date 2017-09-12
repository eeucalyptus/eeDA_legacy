import uuid

from .schematicsconnector import SchematicsConnector

class SymbolConnector(SchematicsConnector):
    def __init__(self, symbol):
        self.uuid = uuid.uuid1();
        self.symbol = symbol
        
        self.pinnumber = 0
        self.pinname = ''
        
        self.position = Vector2i()
        self.parts = []