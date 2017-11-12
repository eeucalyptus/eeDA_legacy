from PyQt5 import QtWidgets, QtGui, QtCore

def UserMessage(text, caption):
    msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, caption,
        text, QtWidgets.QMessageBox.Ok)
    msg.exec()
