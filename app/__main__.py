import sys

from .mainwindow import MyWindow
from PyQt5 import QtWidgets

if __name__=='__main__':
    print('''Running eeDA!''')
    
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    w.setGeometry(300, 300, 300, 300)
    w.showMaximized()
    
    if (sys.flags.interactive == False):
        sys.exit(app.exec_())