import sys

from mainwindow import MyWindow
from PyQt5 import QtWidgets, QtGui

if __name__=='__main__':
    print('''Running eeDA!''')
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QAbstractButton{background: #ffffff} QAbstractButton:hover{background: #cce6ff;border: none}")
    app.setWindowIcon(QtGui.QIcon('resources\icons\logo64.png'))
    w = MyWindow()
    w.setGeometry(300, 300, 300, 300)
    w.showMaximized()
    
    if (sys.flags.interactive == False):
        sys.exit(app.exec_())