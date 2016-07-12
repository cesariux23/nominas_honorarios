from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic
from database import Quincena
Ui_aperturaQuincenaDialog, QtBaseClass = uic.loadUiType("../ui/dialogs/aperturaQuincenaDialog.ui")

class AperturaQuincenaDialog(QDialog):
    def __init__(self):
        super(AperturaQuincenaDialog, self).__init__()
        self.ui = Ui_aperturaQuincenaDialog()
        self.ui.setupUi(self)

    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_Escape:
    #         self.reject()
