from PyQt5 import QtCore, QtWidgets, QtGui
from glwidget import GLWidget
from treeview import TreeViewDock

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
        
        self.positionWidget = QtWidgets.QLabel()
        self.statusBar().addPermanentWidget(self.positionWidget)
        
        self.glWidget = GLWidget(self)
        #self.txtWidget = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.glWidget)
        
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        
        self.setWindowTitle("eeDA 2017 Unprofessional Edition")
        self.statusBar().showMessage("Welcome!")
        
        self.toolbar = self.addToolBar('File')
        iconNew = QtGui.QIcon('resources/icons/Test.png')
        self.toolbarActionNew = QtWidgets.QAction(iconNew, 'New')
        self.toolbar.addAction(self.toolbarActionNew)
        
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
        
        moremenu = QtWidgets.QMenu("&More", self)
        aboutAct = QtWidgets.QAction("About", self)
        aboutAct.setStatusTip("About this software.")
        moremenu.addAction(aboutAct)
        
        filemenu.addMenu(moremenu)
        
        viewMenu = mbar.addMenu('&View')
        zoomMenu = QtWidgets.QMenu('&Zoom', viewMenu)
        viewMenu.addMenu(zoomMenu)
        
        zoomLow = QtWidgets.QAction('50%', zoomMenu)
        zoomLow.triggered.connect(lambda: self.glWidget.changeZoom('low'))
        zoomMenu.addAction(zoomLow)
        
        zoomMid = QtWidgets.QAction('100%', zoomMenu)
        zoomMid.triggered.connect(lambda: self.glWidget.changeZoom('mid'))
        zoomMenu.addAction(zoomMid)
        
        zoomHi = QtWidgets.QAction('150%', zoomMenu)
        zoomHi.triggered.connect(lambda: self.glWidget.changeZoom('hi'))
        zoomMenu.addAction(zoomHi)
        
    def toggleCentralWidget(self):
        pass