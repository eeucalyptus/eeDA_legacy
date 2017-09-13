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
        
        # ----- begin drawing
        if self.wire.connectors[0] != None:                 # check whether there is a connector 1
            point1 = self.wire.connectors[0].pos            # true: set it as point 1
            if len(self.wire.points) > 0:                       # check whether there are additional points
                point2 = self.wire.points[0]                    # true: set the first one as point 2
            elif self.wire.connectors[1] != None:               # else check whether there is a second connector
                point2 = self.wire.connectors[1].pos            # true: draw the connection and return the genList
                                                                # in this branch, the wire is a straight line
                self.gl.glVertex3i(point1.x, point1.y, 1)
                self.gl.glVertex3i(point2.x, point2.y, 1)
                
                self.gl.glEnd()
                self.gl.glEndList()
                
                return genList
            else:                                               # if there is only one connector at all, don't render anything; return an empty genList
                # TODO: no-connector-render, s.b.
                self.gl.glEnd()
                self.gl.glEndList()
                return genList
        else:
            pass # TODO: implement general 'no connector'-render.
            
            self.gl.glVertex3i(point1.x, point1.y, 1)       # in this branch, points 1 and 2 are valid and can be rendered
            self.gl.glVertex3i(point2.x, point2.y, 1)
        
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
            pass
            # TODO: no-connector-render
        
        self.gl.glEnd()
        self.gl.glEndList()

        return genList