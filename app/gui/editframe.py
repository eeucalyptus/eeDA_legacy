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
        layout2.addWidget(self.tbBox.toolArea)
        layout.addWidget(self.tbBox, 0, QtCore.Qt.AlignRight)
        
        self.setLayout(layout)
        
        
    def initToolArea(self):
        self.toolArea = self.tbBox.toolArea
        layout = QtWidgets.QVBoxLayout()
        
        
        #dummies
        icon = QtGui.QIcon('resources/icons/mystery.png')
        for i in range(0, 10):
            button = QtWidgets.QToolButton()
            button.setIcon(icon)
            button.setToolTip("Dummy")
            button.setIconSize(QtCore.QSize(32, 32))
            layout.addWidget(button)
            
        layout.addStretch()
        self.toolArea.setLayout(layout)
