from data import schematics

def RenderSchematicsContext(glWidget, schmaticsContext):
    gl = glWidget.gl
        
    for(symbol in schematicsContext.page[schematicsContext].elements):
        gl.glCallList(symbol.renderer.callList)