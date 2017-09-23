from data import schematics

def RenderSchematicsContext(glWidget, schmaticsContext):
    gl = glWidget.gl
        
    # for(symbol in schematicsContext.page[schematicsContext].elements):    # I'm still unsure what page[schematicsContext] is supposed to mean :) - M
    #     gl.glCallList(symbol.renderer.callList)
        
    for(symbol in schematicsContext.page.elements):
        if symbol.renderer != None:
            gl.glCallList(symbol.renderer.callList)