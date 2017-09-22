from .copperstructure import CopperStructure
from enum import Enum

class PadShape(Enum):
    ROUND = 1
    RECTANGLE = 2
    TRAPEZOID = 3


class Pad(CopperStructure):
    def __init__(self):
        self.uuid = ''
        
        self.pinuuid = ''
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
    