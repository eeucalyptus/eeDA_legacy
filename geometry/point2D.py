class Point2D():
    def __init__(self, x = 0.0, y = 0.0):
        self.x = float(x)
        self.y = float(y)
        
    def moveTo(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def move(self, x, y):
        self.x += x
        self.y += y
    
    def __add__(self, other):
        xSum = self.x + other.x
        ySum = self.y + other.y
        return Point2D(xSum, ySum)
        
    def __sub__(self, other):
        xSum = self.x - other.x
        ySum = self.y - other.y
        return Point2D(xSum, ySum)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
    
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"