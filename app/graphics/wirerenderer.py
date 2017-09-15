from . import Renderer
from data.util import Vector2i

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
        
        # ----- begin drawing
        if self.wire.connectors[0] != None:                 # check whether there is a connector 1
            point1 = self.wire.connectors[0].pos            # true: set it as point 1
            #print("Bingo 1")
            if len(self.wire.points) > 0:                       # check whether there are additional points
                #print("Bingo 2")
                point2 = self.wire.points[0]                    # true: set the first one as point 2
            elif self.wire.connectors[1] != None:               # else check whether there is a second connector
                point2 = self.wire.connectors[1].pos            # true: draw the connection and return the genList
                                                                # in this branch, the wire is a straight line
                self.gl.glVertex3i(point1.x, point1.y, 1)
                self.gl.glVertex3i(point2.x, point2.y, 1)
                
                self.gl.glEnd()
                self.gl.glEndList()
                
                return genList
            else:                                               # if there is only one connector at all, only render unconnected symbol; return an empty genList
                self.renderUnconnected(self.wire.connectors[0].pos)
                self.gl.glEnd()
                self.gl.glEndList()
                return genList

            self.gl.glVertex3i(point1.x, point1.y, 1)       # in this branch, points 1 and 2 are valid and can be rendered
            self.gl.glVertex3i(point2.x, point2.y, 1)
        else:
            if len(self.wire.points) > 0:                   # if there's no first connector, try drawing the unconnected symbol at the first intermediate vertex
                self.renderUnconnected(self.wire.points[0])
            elif self.wire.connectors[1] != None:
                self.renderUnconnected(self.wire.connectors[1].pos) # if there are also no intermediate vertices, try using the other connector
                self.gl.glEnd()                             # at this point, the work is done and the genList can be returned
                self.gl.glEndList()
                return genList
        
        
        for i in range(0, len(self.wire.points)-1):         # draw all the intermediate lines
            point1 = self.wire.points[i]
            point2 = self.wire.points[i+1]
            self.gl.glVertex3i(point1.x, point1.y, 1)
            self.gl.glVertex3i(point2.x, point2.y, 1)
        
        if self.wire.connectors[1] != None:                 # if there is a second connector, do draw a connection
                                                            # note that if there are no intermediate points, this branch will not be reached
            point1 = self.wire.points[-1]
            point2 = self.wire.connectors[1].pos
            self.gl.glVertex3i(point1.x, point1.y, 1)
            self.gl.glVertex3i(point2.x, point2.y, 1)
        else:
            self.renderUnconnected(self.wire.points[-1])         # this branch should only be reached if there are intermediate points. I hope.
        
        self.gl.glEnd()
        self.gl.glEndList()

        return genList
    
    def renderUnconnected(self, pos):
        self.gl.glColor4f(1.0, 0.0, 0.0, 1.0)
        self.gl.glVertex3i(pos.x - 10, pos.y - 10, 1.5)
        self.gl.glVertex3i(pos.x + 10, pos.y + 10, 1.5)
        self.gl.glVertex3i(pos.x + 10, pos.y - 10, 1.5)
        self.gl.glVertex3i(pos.x - 10, pos.y + 10, 1.5)
        self.gl.glColor4f(0.5, 0.5, 0.5, 1.0)