import sys, math
from PyQt5 import QtCore, QtWidgets, QtGui

class TreeViewWidget(QtWidgets.QTreeWidget):
    def __init__(self):
        super().__init__()
        self.initTree()
    
    def initTree(self):
        
        self.setHeaderLabel("Tree")
        topItem = QtWidgets.QTreeWidgetItem()
        topItem.setText(0, "Root")
        child = QtWidgets.QTreeWidgetItem()
        child.setText(0, "Branch")
        topItem.addChild(child)
        self.addTopLevelItem(topItem)
        

class TreeViewDock(QtWidgets.QDockWidget):
    def __init__(self):
        super().__init__()
        self.tree = self.initTV
        
    def initTV(self):
        
        self.setWindowTitle("Tree view")
        treeWidget = TreeViewWidget()
        self.setWidget(treeWidget)
        treeWidget.setWindowTitle("Tree view")
        return treeWidget
        
class GLWidget(QtWidgets.QOpenGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)


    def initializeGL(self):
        version = QtGui.QOpenGLVersionProfile()
        version.setVersion(2, 1)
        self.gl = self.context().versionFunctions(version)
        self.gl.initializeOpenGLFunctions()

        self.gl.glClearColor(0.0, 0.0, 0.0, 1.0)
        self.object = self.makeTriangle()
        self.gl.glShadeModel(self.gl.GL_FLAT)
        self.gl.glEnable(self.gl.GL_DEPTH_TEST)
        self.gl.glEnable(self.gl.GL_CULL_FACE)
        self.gl.glEnable(self.gl.GL_MULTISAMPLE)

    def paintGL(self):
        self.gl.glClear(
                self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.gl.glLoadIdentity()
        self.gl.glTranslated(0.0, 0.0, -10.0)
        self.gl.glCallList(self.object)

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        self.gl.glViewport((width - side) // 2, (height - side) // 2, side, side)

        self.gl.glMatrixMode(self.gl.GL_PROJECTION)
        self.gl.glLoadIdentity()
        self.gl.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        self.gl.glMatrixMode(self.gl.GL_MODELVIEW)

    def makeTriangle(self):
    
        genList = self.gl.glGenLists(1)
        self.gl.glNewList(genList, self.gl.GL_COMPILE)

        self.gl.glBegin(self.gl.GL_TRIANGLES)
        
        self.gl.glColor4f(0.282, 0.235, 0.196, 1.0)
        
        for i in range(3):
            angle = 80.0 - i*120.0
            x = 0.3 * math.cos(math.radians(angle))
            y = 0.3 * math.sin(math.radians(angle))
            self.gl.glVertex3d(x, y, -0.05)

        self.gl.glEnd()
        self.gl.glEndList()

        return genList


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initMenu()
        self.initTreeView()
        
    def initUI(self):    
        fmt = QtGui.QSurfaceFormat.defaultFormat()
        fmt.setSamples(4)
        QtGui.QSurfaceFormat.setDefaultFormat(fmt)
        
        self.glWidget = GLWidget(self)
        self.txtWidget = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.glWidget)
        
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        
        self.setWindowTitle("eeDA 2017 Unprofessional Edition")
        self.statusBar().showMessage("Welcome!")
        
    def initTreeView(self):
        treeview = TreeViewDock()
        treeview.setWindowTitle("Tree View")
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, treeview)
        treeview.tree().resize(200, 0)
        
        
    def initMenu(self):
        exitAct = QtWidgets.QAction("Exit", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("Exit the application.")
        exitAct.triggered.connect(self.close)
        
        mysteryAct = QtWidgets.QAction("Mystery option", self, checkable = True)
        mysteryAct.setStatusTip("Not even I know what this does.")
        mysteryAct.setShortcut("Ctrl+Tab")
        mysteryAct.triggered.connect(self.toggleCentralWidget)
        
        mbar = self.menuBar()
        filemenu = mbar.addMenu("&File")
        filemenu.addAction(exitAct)
        filemenu.addAction(mysteryAct)
        
        moremenu = QtWidgets.QMenu("More", self)
        aboutAct = QtWidgets.QAction("About", self)
        aboutAct.setStatusTip("About this software.")
        moremenu.addAction(aboutAct)
        
        filemenu.addMenu(moremenu)
        
    def toggleCentralWidget(self):
        pass
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    w.setGeometry(300, 300, 300, 300)
    w.showMaximized()

    sys.exit(app.exec_())