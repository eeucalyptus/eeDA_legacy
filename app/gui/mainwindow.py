from PyQt5 import QtCore, QtWidgets, QtGui
from .glwidget import GLWidget
from .editframe import EditFrame
from .treeview import TreeViewDock

#=====
# debug only
from data.schematics import Wire, Symbol, WireConnector, Junction
from data.util import *
from graphics import WireRenderer, SymbolRenderer, JunctionRenderer
#=====
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initMenu()
        self.initTreeView()
        
        self.runDebug() # placeholder for misc debug scripts
        
    def initUI(self):
        # ----- Display format ----- #
        fmt = QtGui.QSurfaceFormat.defaultFormat()
        fmt.setSamples(4)
        QtGui.QSurfaceFormat.setDefaultFormat(fmt)
        
        # ----- Position widget ----- #
        self.positionWidget = QtWidgets.QLabel()
        self.statusBar().addPermanentWidget(self.positionWidget)
        
        # ----- OpenGL widget ----- #
        #self.glWidget = GLWidget(self)
        #self.txtWidget = QtWidgets.QTextEdit(self)
        #self.setCentralWidget(self.glWidget)
        
        # ----- Edit frame, containing OpenGL widget and edit toolbar ----- #
        self.editFrame = EditFrame(self)
        self.glWidget = self.editFrame.glWidget
        self.setCentralWidget(self.editFrame)
        
        # ----- Window geometry ----- #
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(screen.width()/4, screen.height()/4, screen.width()/2, screen.height()/2)
        
        # ----- Window title bar ----- #
        self.setWindowTitle("eeDA 2017 Unprofessional Edition")
        self.statusBar().showMessage("Welcome!")
        
        # ----- Toolbar ----- #
        self.toolbar = self.addToolBar('File')
        
        iconSave = QtGui.QIcon('resources/icons/save.png')
        self.toolbarActionSave = QtWidgets.QAction(iconSave, 'Save')
        self.toolbar.addAction(self.toolbarActionSave)
        
        iconNew = QtGui.QIcon('resources/icons/new.png')
        self.toolbarActionNew = QtWidgets.QAction(iconNew, 'New...')
        self.toolbar.addAction(self.toolbarActionNew)
        
        iconDelete = QtGui.QIcon('resources/icons/delete.png')
        self.toolbarActionDelete = QtWidgets.QAction(iconDelete, 'Delete')
        self.toolbar.addAction(self.toolbarActionDelete)
        
        iconOpen = QtGui.QIcon('resources/icons/open.png')
        self.toolbarActionOpen = QtWidgets.QAction(iconOpen, 'Open...')
        self.toolbar.addAction(self.toolbarActionOpen)
        
        self.toolbar.addSeparator()
        
        iconUndo = QtGui.QIcon('resources/icons/undo.png')
        self.toolbarActionUndo = QtWidgets.QAction(iconUndo, 'Undo')
        self.toolbar.addAction(self.toolbarActionUndo)
        
        iconRedo = QtGui.QIcon('resources/icons/redo.png')
        self.toolbarActionRedo = QtWidgets.QAction(iconRedo, 'Redo')
        self.toolbar.addAction(self.toolbarActionRedo)
        
        self.toolbar.addSeparator()
        
        iconLeft = QtGui.QIcon('resources/icons/leftarrow.png')
        self.toolbarActionLeft = QtWidgets.QAction(iconLeft, 'Left')
        self.toolbar.addAction(self.toolbarActionLeft)
        
        iconRight = QtGui.QIcon('resources/icons/rightarrow.png')
        self.toolbarActionRight = QtWidgets.QAction(iconRight, 'Right')
        self.toolbar.addAction(self.toolbarActionRight)
        
    def initTreeView(self):
        treeview = TreeViewDock()
        treeview.setWindowTitle("Tree View")
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, treeview)
        treeview.tree().resize(200, 0)
        
        
    def initMenu(self):
        exitAct = QtWidgets.QAction("Exit", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("Exit the application.")
        exitAct.setIcon(QtGui.QIcon('resources\icons\exit.png'))
        exitAct.triggered.connect(self.close)
        
        mysteryAct = QtWidgets.QAction("Mystery option", self, checkable = True)
        mysteryAct.setStatusTip("Not even I know what this does.")
        mysteryAct.setShortcut("Ctrl+Tab")
        mysteryAct.setIcon(QtGui.QIcon('resources\icons\mystery.png'))
        mysteryAct.triggered.connect(self.toggleCentralWidget)
        
        mbar = self.menuBar()
        fileMenu = mbar.addMenu("&File")
        fileMenu.addAction(exitAct)
        
        # add some of the toolbar actions to the file menu
        fileMenu.addAction (self.toolbarActionOpen)
        fileMenu.addAction (self.toolbarActionNew)
        fileMenu.addAction (self.toolbarActionSave)
        
        fileMenu.addAction(mysteryAct)
        
        moremenu = QtWidgets.QMenu("&More", self)
        aboutAct = QtWidgets.QAction("About", self)
        aboutAct.setStatusTip("About this software.")
        moremenu.addAction(aboutAct)
        
        fileMenu.addMenu(moremenu)
        
        # ----- Edit menu ----- #
        editMenu = mbar.addMenu('&Edit')
        editMenu.addAction(self.toolbarActionUndo)
        editMenu.addAction(self.toolbarActionRedo)
        
        # ----- View menu ----- #
        viewMenu = mbar.addMenu('&View')
        
        # --- Zoom options --- #
        zoomMenu = QtWidgets.QMenu('&Zoom', viewMenu)
        viewMenu.addMenu(zoomMenu)
        
        zoomPlus = QtWidgets.QAction('+', zoomMenu)
        zoomPlus.setShortcut("Ctrl++")
        zoomPlus.triggered.connect(lambda: self.glWidget.multZoom(1.1))
        zoomMenu.addAction(zoomPlus)
        
        zoomMinus = QtWidgets.QAction('-', zoomMenu)
        zoomMinus.setShortcut("Ctrl+-")
        zoomMinus.triggered.connect(lambda: self.glWidget.multZoom(0.9))
        zoomMenu.addAction(zoomMinus)
        
        zoomMenu.addSeparator()
        zoomLow = QtWidgets.QAction('50%', zoomMenu)
        zoomLow.triggered.connect(lambda: self.glWidget.changeZoom('low')) # as far as I understand the matter, :connect() doesn't pass arguments, hence the
                                                                           # lambda -- Musicted (WTF is functional programming?)
        zoomMenu.addAction(zoomLow)
        
        zoomMid = QtWidgets.QAction('100%', zoomMenu)
        zoomMid.triggered.connect(lambda: self.glWidget.changeZoom('mid'))
        zoomMenu.addAction(zoomMid)
        
        zoomHi = QtWidgets.QAction('150%', zoomMenu)
        zoomHi.triggered.connect(lambda: self.glWidget.changeZoom('hi'))
        zoomMenu.addAction(zoomHi)
        
    def resizeEvent(self, event):
        self.editFrame.decideStack()
        
    def toggleCentralWidget(self):
        pass
    
    def runDebug(self):
        # -- wire
        testWire = Wire(None)
        testWire.setPoints([\
        Vector2i(-50, 0),\
        Vector2i(0, 200),\
        Vector2i(50, 100),\
        Vector2i(100, 200),\
        Vector2i(150, 0)])
        testWire.setConnectors(WireConnector(None, Vector2i(-100, 0)), None)
        
        debugAct = self.menuBar().addAction('Wire')
        debugAct.triggered.connect(lambda: self.debugWire(testWire))
        
        
        # -- symbol
        testSymbol = Symbol(None)
        testSymbol.addPolygon(Polygon.fromPoints(\
        Vector2i(-100, -100),\
        Vector2i(-100, 0),\
        Vector2i(0, 0),\
        Vector2i(0, -50),\
        Vector2i(-75, -150),\
        ))
        debugAct2 = self.menuBar().addAction('Symbol')
        debugAct2.triggered.connect(lambda: self.debugSymbol(testSymbol))
        
        # -- junction
        testJunction = Junction(None)
        testJunction.setPos(Vector2i(500, 500))
        
        debugAct3 = self.menuBar().addAction('Junction')
        debugAct3.triggered.connect(lambda: self.debugJunction(testJunction))
    def debugWire(self, wire):
        wire.setRenderer(WireRenderer(wire, self.glWidget.gl))
        self.glWidget.setInject(wire.renderer.genSymbolCallList())
        self.glWidget.repaint()
        print("Success: wire rendering")
        
    def debugSymbol(self, symbol):
        symbol.setRenderer(SymbolRenderer(symbol, self.glWidget.gl))
        self.glWidget.setInject(symbol.renderer.genSymbolCallList())
        self.glWidget.repaint()
        print("Success: symbol rendering")
        
    def debugJunction(self, junction):
        junction.setRenderer(JunctionRenderer(junction, self.glWidget.gl))
        self.glWidget.setInject(junction.renderer.genSymbolCallList())
        self.glWidget.repaint()
        print("Success: junction rendering")