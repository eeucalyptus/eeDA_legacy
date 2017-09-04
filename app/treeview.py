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