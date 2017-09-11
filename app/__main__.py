import sys

from PyQt5 import QtWidgets, QtGui
from gui import MyWindow

if __name__=='__main__':
    print('''Running eeDA!''')
    
    app = QtWidgets.QApplication(sys.argv)
    
    # load the stylesheet
    try:
        with open('resources\interface\style.css') as stylesheet:
            app.setStyleSheet(stylesheet.read())
    except FileNotFoundError:
        print("Stylesheet not found!")
    
    app.setWindowIcon(QtGui.QIcon('resources\icons\logo64.png'))
    w = MyWindow()
    w.setGeometry(300, 300, 300, 300)
    w.showMaximized()
    
    if (sys.flags.interactive == False):
        sys.exit(app.exec_())