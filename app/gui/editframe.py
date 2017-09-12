from PyQt5 import QtCore, QtWidgets, QtGui
from .glwidget import GLWidget
###### Doesn't do what I want it to. Yet. -- M
class EditFrame(QtWidgets.QWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.positionWidget = self.parent().positionWidget
        self.glWidget = GLWidget(self)
        self.initBox()
        self.initToolArea()
    
    def initBox(self):
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.glWidget, 1)
        
        self.tbBox = QtWidgets.QWidget()
        layout2 = QtWidgets.QVBoxLayout()
        self.tbBox.setLayout(layout2)
        self.tbBox.toolArea = QtWidgets.QGroupBox(self.tbBox)
        self.tbBox.toolArea.setTitle('Edit tools')
        layout2.addWidget(self.tbBox.toolArea)
        layout.addWidget(self.tbBox, 0, QtCore.Qt.AlignRight)
        layout2.addStretch()
        self.setLayout(layout)
        
    def initToolArea(self):
        self.toolArea = self.tbBox.toolArea
        layout = QtWidgets.QGridLayout()
        layout.setVerticalSpacing(0)
        
        #dummies
        icon = QtGui.QIcon('resources/icons/mystery.png')
        for i in range(0, 20):
            button = QtWidgets.QToolButton()
            button.setIcon(icon)
            button.setToolTip("Dummy")
            button.setIconSize(QtCore.QSize(16, 16))
            layout.addWidget(button, i, 0) # adds button at row i, column 0
            
        for i in range(0, 20):
            button = QtWidgets.QToolButton()
            button.setIcon(icon)
            button.setToolTip("Dummy")
            button.setIconSize(QtCore.QSize(16, 16))
            layout.addWidget(button, i, 1)
            
        self.toolArea.setLayout(layout)
        self.parent().setMinimumSize(100, 100) # some layout object constrains the window size to be >= the height of the QGroupBox, this is a workaround.
