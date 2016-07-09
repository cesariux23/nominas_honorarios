from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic
import bcrypt

from database import *

Ui_loginDialog, QtBaseClass = uic.loadUiType("../ui/dialogs/loginDialog.ui")

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
            passwordHash=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))
            print(passwordHash)
            #se busca en la base de datos
            try:
                usuario=User.select().where(User.username==user).get()
                if(usuario):
                    #se compara la contraseña
                    if(bcrypt.checkpw(password.encode('utf-8'),usuario.password.replace('$2y','$2b').encode('utf-8'))):
                        self.accept()
                    else:
                        QMessageBox.warning(self, "Inicio de sesión", "Usuario y contraseña no validos",QMessageBox.Ok)
            except User.DoesNotExist:
                QMessageBox.warning(self, "Inicio de sesión", "Usuario y contraseña no validos",QMessageBox.Ok)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.reject()
