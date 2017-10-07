import math

class Vector2d():
    def __init__(self, x = 0, y = 0):
        self.x = float(x)
        self.y = float(y)
    
    def fromVector2i(vector):
        return Vector2d(vector.x, vector.y)
    
    def euDist(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def normalize(self):
        return self / self.euDist()
    
    def normalCW(self):
        unitVector = self.normalize()
        return Vector2d(-unitVector.y, +unitVector.x)
    
    def normalCCW(self):
        unitVector = self.normalize()
        return Vector2d(+unitVector.y, -unitVector.x)
    
    def __add__(self, other):
        xSum = self.x + other.x
        ySum = self.y + other.y
        return Vector2d(xSum, ySum)
        
    def __sub__(self, other):
        xSum = self.x - other.x
        ySum = self.y - other.y
        return Vector2d(xSum, ySum)
        
    def __truediv__(self, scalar):
        x = self.x / scalar
        y = self.y / scalar
        return Vector2d(x, y)
    
    def __div__(self, scalar):
        x = self.x / scalar
        y = self.y / scalar
        return Vector2d(x, y)
        
    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector2d(x, y)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
    
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

class Vector2i():
    def __init__(self, x = 0, y = 0):
        self.x = int(x)
        self.y = int(y)
        
    def fromVector2d(vector):
        return Vector2i(vector.x, vector.y)
    
    def normalize(self):
        newVec = Vector2d.fromVector2i(self)
        return newVec / newVec.euDist()
    
    def __add__(self, other):
        xSum = self.x + other.x
        ySum = self.y + other.y
        return Vector2i(xSum, ySum)
        
    def __sub__(self, other):
        xSum = self.x - other.x
        ySum = self.y - other.y
        return Vector2i(xSum, ySum)
    
    def __truediv__(self, scalar):
        x = self.x / scalar
        y = self.y / scalar
        return Vector2i(x, y)
    
    def __div__(self, scalar):
        x = self.x / scalar
        y = self.y / scalar
        return Vector2i(x, y)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
    
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"