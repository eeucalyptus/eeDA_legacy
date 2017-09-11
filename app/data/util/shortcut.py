# ----- implements shortcut-only QActions ----- #
# I'm really fucking proud of me. Sheer elegance. - M
from PyQt5 import QtWidgets

class Shortcut:
    def __init__(self, parentWidget, keys, action):
        self.act = QtWidgets.QAction(parent = parentWidget)
        self.act.setShortcut(keys)
        self.act.triggered.connect(action)