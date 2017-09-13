'''

The schematic class contains the whole data structure needed for
the circuit representation and manipulation. It is divided into 
pages which themselves contain symbols, wires, etc.

'''

import uuid

class Schematic:
    def __init__(self):
        self.uuid = uuid.uuid1();
        
        self.pages = []
        self.fields = {}
        