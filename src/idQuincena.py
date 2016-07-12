from datetime import date

class IdQuincena():
    def __init__(self,fecha = date.today()):
        #Se desglosa la fecha recibida para calcular la quincena
        self.fecha_inicio=fecha
        self.mes=fecha.month
        self.anio=fecha.year
        self.quincena_del_mes(fecha.day)
        self.quincena_del_anio()
        self.calcula_nombre_quincena()
        self.calcula_id()

    #
    #Metodo que determina si es la primer quincena o la segunda del mes
    #asi como el dia inicial del periodo
    #Devuelve 1 o 2, para primer o segunda quincena segun corresponda
    #
    def quincena_del_mes(self,dia=1):
        self.quincena_mes=1
        if(dia > 15):
            self.quincena_mes=2
            dia=16
        #calcula las fechas iniciales y finales
        self.fecha_inicio.replace(self.anio, self.mes,dia)

    #
    #Metodo que determina el numero ordinal de la quincena dentro de un año
    #
    def quincena_del_anio(self):
        self.quincena=self.mes*2;
        if(self.quincena_mes==1):
            self.quincena-=1
        print(self.quincena)

    #
    #Metodo que calcula el nombre de la quincena
    #
    def calcula_nombre_quincena(self):
        if (self.quincena_mes==1):
            nombre="1ra. "
        else:
            nombre="2da. "
        self.nombre=nombre+"quincena de " + self.fecha_inicio.strftime("%B de %Y")

    #
    #calcula el id representativo del periodo
    #
    def calcula_id(self):
        self.id=str(self.anio)+str(self.quincena).zfill(2)
