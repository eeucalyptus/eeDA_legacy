from PyQt5 import QtCore, QtWidgets, QtGui
from .glwidget import GLWidget
###### Doesn't do what I want it to. Yet. -- M
class EditFrame(QtWidgets.QWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.positionWidget = self.parent().positionWidget
        self.glWidget = GLWidget(self)
        self.initBox()
        
        self.decideStack()
    
    def initBox(self):
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 2, 0)
        layout.setSpacing(2)
        layout.addWidget(self.glWidget, 1)
        
        # ----- big box ----- #
        self.tbBox1 = QtWidgets.QWidget()
        self.tbBox1.setFixedWidth(32)
        
        layout2 = QtWidgets.QVBoxLayout()
        layout2.setSpacing(5)
        layout2.setContentsMargins(0, 5, 0, 0)
        
        icon = QtGui.QIcon('resources/icons/mystery.png')
        
        for i in range(10):
            button1 = QtWidgets.QToolButton()
            button1.setIcon(icon)
            button1.setToolTip("Dummy")
            button1.setIconSize(QtCore.QSize(32, 32))
            button1.setFixedSize(32, 32)
            layout2.addWidget(button1)
            
        layout2.addStretch()
        self.tbBox1.setLayout(layout2)
        
        # ----- small box ----- #
        self.tbBox2 = QtWidgets.QWidget()
        
        
        layout3 = QtWidgets.QGridLayout()
        layout3.setSpacing(2)
        layout3.setContentsMargins(1, 1, 1 , 1)
        
        icon = QtGui.QIcon('resources/icons/mystery.png')
        
        for i in range(5):
            button1 = QtWidgets.QToolButton()
            button1.setIcon(icon)
            button1.setToolTip("Dummy")
            button1.setIconSize(QtCore.QSize(16, 16))
            button1.setFixedSize(16, 16)
            layout3.addWidget(button1, i, 0)
            
            button1 = QtWidgets.QToolButton()
            button1.setIcon(icon)
            button1.setToolTip("Dummy")
            button1.setIconSize(QtCore.QSize(16, 16))
            button1.setFixedSize(16, 16)
            layout3.addWidget(button1, i, 1)
            
            
        outerLayout = QtWidgets.QVBoxLayout()
        outerLayout.addLayout(layout3)
        outerLayout.addStretch(1)
        
        self.tbBox2.setLayout(outerLayout)
        
        # ----- layout stack ----- #
        self.tbBox = QtWidgets.QWidget()
        self.stack = QtWidgets.QStackedLayout()
        self.stack.addWidget(self.tbBox1)
        self.stack.addWidget(self.tbBox2)
        
        self.tbBox.setLayout(self.stack)
        
        # ----- #
        layout.addWidget(self.tbBox, 0, QtCore.Qt.AlignRight)
        self.setLayout(layout)
        
        
    def decideStack(self):
        height = self.parent().frameGeometry().height()
        if height > 600:
            self.stack.setCurrentIndex(0)
            self.tbBox.setFixedWidth(32)
        else:
            self.stack.setCurrentIndex(1)
            self.tbBox.setFixedWidth(48)