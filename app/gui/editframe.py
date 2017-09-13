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
        layout.setContentsMargins(0, 0, 2, 0)
        layout.setSpacing(2)
        layout.addWidget(self.glWidget, 1)
        
        self.tbBox = QtWidgets.QWidget()
        self.tbBox.setFixedWidth(32)
        
        layout.addWidget(self.tbBox, 0, QtCore.Qt.AlignRight)
        self.setLayout(layout)
        
    def initToolArea(self):
        layout2 = QtWidgets.QVBoxLayout()
        layout2.setSpacing(5)
        layout2.setContentsMargins(0, 5, 0, 0)
        self.tbBox.setLayout(layout2)
        
        icon = QtGui.QIcon('resources/icons/mystery.png')
        
        for i in range(10):
            button1 = QtWidgets.QToolButton()
            button1.setIcon(icon)
            button1.setToolTip("Dummy")
            button1.setIconSize(QtCore.QSize(32, 32))
            button1.setFixedSize(32, 32)
            layout2.addWidget(button1)
                
        layout2.addStretch()