from . import Renderer

class WireRenderer(Renderer):
    def __init__(self, wire, gl):
        super().__init__(gl)
        self.wire = wire
        self.callList = self.genSymbolCallList()
        
    def genSymbolCallList(self):
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)
        self.gl.glColor4f(0.5, 0.5, 0.5, 1.0)
        
        # TODO: Implement wire rendering
        # Let's try and do this, shall we?
        # It's gonna be a bumpy ride -- M
        self.gl.glLineWidth(5)
        
        self.gl.glBegin(self.gl.GL_LINES)
        if self.wire.connectors[0] != None:
            point1 = self.wire.connectors[0].pos
            if len(self.wire.points) > 0:
                #print("Branch 1")
                point2 = self.wire.points[0]
            elif self.wire.connectors[1] != None:
                #print("Branch 2")
                point2 = self.wire.connectors[1].pos
                self.gl.glEnd()
                self.gl.glEndList()
                return genList
            else:
                #print("Branch 3")
                self.gl.glEnd()
                self.gl.glEndList()
                return genList
            
            self.gl.glVertex3i(point1.x, point1.y, 1)
            self.gl.glVertex3i(point2.x, point2.y, 1)
        
        for i in range(0, len(self.wire.points)-1):
            point1 = self.wire.points[i]
            point2 = self.wire.points[i+1]
            self.gl.glVertex3i(point1.x, point1.y, 1)
            self.gl.glVertex3i(point2.x, point2.y, 1)
        
        if self.wire.connectors[1] != None:
            point1 = self.wire.points[-1]
            point2 = self.wire.connectors[1].pos
            self.gl.glVertex3i(point1.x, point1.y, 1)
            self.gl.glVertex3i(point2.x, point2.y, 1)
        
        self.gl.glEnd()
        self.gl.glEndList()

        return genList