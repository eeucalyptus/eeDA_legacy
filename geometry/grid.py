from point2D import *

class Grid():
    
    def __init__(self, xRes = 1.0, yRes = None, origin = Point2D()):
        
        if yRes == None:
            yRes = float(xRes)
            
        self.origin = origin
        self.xRes = float(xRes)
        self.yRes = float(yRes)
        
    def setOrigin(self, point):
        self.origin = point
        
    def setxRes(self, res):
        self.xRes = float(res)
    
    def setyRes(self, res):
        self.yRes = float(res)
        
    def setRes(self, res):
        self.xRes = float(res)
        self.yRes = float(res)
    
    def nearestSnap(self, point):
        pointAdj = point - self.origin
        
        xMult = round(pointAdj.x / self.xRes)
        yMult = round(pointAdj.y / self.xRes)
        
        xSnap = self.xRes * xMult
        ySnap = self.yRes * yMult
        
        return Point2D(xSnap, ySnap)
        