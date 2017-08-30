import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class TreeViewWidget(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.initTree()
    
    def initTree(self):
        
        self.setHeaderLabel("Tree")
        topItem = QTreeWidgetItem()
        topItem.setText(0, "Root")
        child = QTreeWidgetItem()
        child.setText(0, "Branch")
        topItem.addChild(child)
        self.addTopLevelItem(topItem)
        

class TreeViewDock(QDockWidget):
    def __init__(self):
        super().__init__()
        self.tree = self.initTV
        
    def initTV(self):
        
        self.setWindowTitle("Tree view")
        treeWidget = TreeViewWidget()
        self.setWidget(treeWidget)
        treeWidget.setWindowTitle("Tree view")
        return treeWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initMenu()
        self.initTreeView()
        
    def initUI(self):
        self.glWidget = QOpenGLWidget(self)
        self.txtWidget = QTextEdit(self)
        self.setCentralWidget(self.glWidget)
        
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        
        self.setWindowTitle("eeDA 2017 Unprofessional Edition")
        self.statusBar().showMessage("Welcome!")
        
    def initTreeView(self):
        treeview = TreeViewDock()
        treeview.setWindowTitle("Tree View")
        self.addDockWidget(Qt.LeftDockWidgetArea, treeview)
        treeview.tree().resize(200, 0)
        
        
    def initMenu(self):
        exitAct = QAction("Exit", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("Exit the application.")
        exitAct.triggered.connect(self.close)
        
        mysteryAct = QAction("Mystery option", self, checkable = True)
        mysteryAct.setStatusTip("Not even I know what this does.")
        mysteryAct.setShortcut("Ctrl+Tab")
        mysteryAct.triggered.connect(self.toggleCentralWidget)
        
        mbar = self.menuBar()
        filemenu = mbar.addMenu("&File")
        filemenu.addAction(exitAct)
        filemenu.addAction(mysteryAct)
        
        moremenu = QMenu("More", self)
        aboutAct = QAction("About", self)
        aboutAct.setStatusTip("About this software.")
        moremenu.addAction(aboutAct)
        
        filemenu.addMenu(moremenu)
        
    def toggleCentralWidget(self):
        pass
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.showMaximized()

    sys.exit(app.exec_())