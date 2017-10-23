from PyQt5 import QtWidgets, QtGui, QtCore

def UserMessage(text, caption="", icon=None, buttons=None)
    msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, caption,
        text, QtWidgets.QMessageBox.Ok)
