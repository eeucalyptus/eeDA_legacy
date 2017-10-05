from PyQt5 import QtCore, QtWidgets, QtGui

class TreeViewWidget(QtWidgets.QTreeWidget):
    def __init__(self):
        super().__init__()
        self.initTree()
    
    def initTree(self):
        
        self.setHeaderLabel(_('Tree'))
        topItem = QtWidgets.QTreeWidgetItem()
        topItem.setText(0, _('Root'))
        child = QtWidgets.QTreeWidgetItem()
        child.setText(0, _('Branch'))
        topItem.addChild(child)
        self.addTopLevelItem(topItem)
        

class TreeViewDock(QtWidgets.QDockWidget):
    def __init__(self):
        super().__init__()
        self.tree = self.initTV
        self.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable | QtWidgets.QDockWidget.DockWidgetFloatable | QtWidgets.QDockWidget.DockWidgetClosable)
        
    def initTV(self):
        
        self.setWindowTitle(_('Tree View'))
        treeWidget = TreeViewWidget()
        self.setWidget(treeWidget)
        treeWidget.setWindowTitle(_('Tree View'))
        return treeWidget