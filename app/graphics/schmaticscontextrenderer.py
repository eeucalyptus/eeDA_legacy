from data import schematics

def RenderSchematicsContext(glWidget, schmaticsContext):
    gl = glWidget.gl
        
    for(symbol in schematicsContext.page[schematicsContext].symbols):
        gl.glCallList(symbol.renderer.callList)
        
    for(decoration in schematicsContext.page[schematicsContext].decorations):
        gl.glCallList(decoration.renderer.callList)
    
    for(joint in schematicsContext.page[schematicsContext].joints):
        gl.glCallList(joint.renderer.callList)
        
    for(label in schematicsContext.page[schematicsContext].labels):
        gl.glCallList(label.renderer.callList)
        
    for(wire in schematicsContext.page[schematicsContext].wires):
        gl.glCallList(wire.renderer.callList)
        