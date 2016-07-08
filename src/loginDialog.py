from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic

Ui_loginDialog, QtBaseClass = uic.loadUiType("../ui/widgets/loginDialog.ui")

class LoginDialog(QDialog):
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.ui = Ui_loginDialog()
        self.ui.setupUi(self)
        self.ui.btn_iniciar_sesion.clicked.connect(self.valida)

    def valida(self, e):
        user=self.ui.txt_username.text()
        password=self.ui.txt_password.text()
        if not user and not password:
            QMessageBox.warning(self, "Inicio de sesión", "Faltan campos requeridos",QMessageBox.Ok)
        else:
            self.accept()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.reject()
