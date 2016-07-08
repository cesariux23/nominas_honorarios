import sys
from datetime import date
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PyQt5 import uic
from idQuincena import *

Ui_nominaMainWindow, QtBaseClass = uic.loadUiType("../ui/widgets/nominaMainWindow.ui")

class NominaMainWindow(QMainWindow):
    def __init__(self):
        super(NominaMainWindow, self).__init__()
        self.ui = Ui_nominaMainWindow()
        self.ui.setupUi(self)

        #se oculta el grupo de nominas
        self.ui.gp_nominas.hide()
        #establece la fecha actual del sistema
        self.set_fecha_actual()
        self.set_quincena()
        self.carga_quincena(self.quincena_actual)

    #muestra la fecha en el statusBar
    def set_fecha_actual(self):
        self.hoy=date.today()
        lb_fecha=QLabel(self)
        lb_fecha.setText(self.hoy.strftime("%A %d de %B de %Y"))
        self.statusBar().addPermanentWidget(lb_fecha)

    #establece la quincena actual
    def set_quincena(self, fecha=date.today()):
        self.quincena_actual=IdQuincena(fecha)
        self.ui.lb_quincena_actual.setText("<h1>{} -- {}</h1>".format(self.quincena_actual.id,self.quincena_actual.nombre))

    #recupera el valor de la nomina en la base de datos
    def carga_quincena(self,qna):
        #self.ui.gp_nominas.show()
        pass
