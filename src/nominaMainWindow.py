import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic

Ui_nominaMainWindow, QtBaseClass = uic.loadUiType("../ui/widgets/nominaMainWindow.ui")

class NominaMainWindow(QMainWindow):
    def __init__(self):
        super(NominaMainWindow, self).__init__()
        self.ui = Ui_nominaMainWindow()
        self.ui.setupUi(self)
