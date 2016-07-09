import sys
import locale

from PyQt5.QtWidgets import QApplication, QDialog
from loginDialog import *
from nominaMainWindow import *
from database import *

# Establecemos el locale de nuestro sistema
locale.setlocale(locale.LC_ALL, "")

#Se crea la conexion a la base de datos de forma global
database.connect()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login=LoginDialog()
    w=NominaMainWindow()
    if login.exec_() == QDialog.Accepted:
        print ("login")
        w.show()
        sys.exit(app.exec_())
    else:
        print("termina!!")
