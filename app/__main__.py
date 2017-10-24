import sys
import gettext
import os
import locale

from PyQt5 import QtWidgets, QtGui
from gui import MyWindow

if __name__=='__main__':

    language = gettext.translation('eeDA', 'resources/locale', ['de_DE'], fallback = True)
    # language = gettext.translation('eeDA', 'resources/locale', [locale.getdefaultlocale()[0]], fallback = True)
    language.install()

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
    w.showMaximized()

    if len(sys.argv) > 1:
        if '--debug' in sys.argv:
            w.runDebug()
        else:
            w.openFile(sys.argv[1])

    if (sys.flags.interactive == False):
        sys.exit(app.exec_())
