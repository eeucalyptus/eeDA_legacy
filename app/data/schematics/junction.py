import uuid

'''

A Junction is the only connector that may have more then one 
connection attached. This is supposed to lead to better 
readability of the schematics, since every node, involving
more then two adjacent nodes has to be depiceted by a junction.

'''

from data.util import Vector2i
from .schematicsconnector import SchematicsConnector

class Junction(SchematicsConnector):
    def __init__(self, schematicspage):
        self.uuid = uuid.uuid1()
        
        self.schematicspage = schematicspage
        self.connections = []
        self.pos = Vector2i()
        