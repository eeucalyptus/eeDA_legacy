from PyQt5.QtWidgets import QApplication, QWidget, QOpenGLWidget
import sys


def initializeGL(self):
    self.gl = self.context().versionFunctions(self.version_profile)
    self.gl.initializeGLFunctions()

    self.gl.glClearColor(1.0, 0.5, 0.5, 1.0)
    self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT)
    
if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    w = QOpenGLWidget()
    w.initializeGL = initializeGL
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())