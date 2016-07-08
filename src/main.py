import sys
import locale

from PyQt5.QtWidgets import QApplication, QDialog
from loginDialog import *
from nominaMainWindow import *

# Establecemos el locale de nuestro sistema
locale.setlocale(locale.LC_ALL, "")

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
