from peewee import *
import env
database = MySQLDatabase(env._DATABASE, **{'password': env._PASSWORD, 'user': env._USER, 'host': env._HOST})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Adscripcion(BaseModel):
    activa = IntegerField(null=True)
    clave = CharField(primary_key=True)
    created_at = DateTimeField(null=True)
    descripcion = CharField(null=True)
    pertenece = CharField(null=True)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'adscripcion'

class Banco(BaseModel):
    clave = CharField(primary_key=True)
    nombre = CharField(null=True, unique=True)

    class Meta:
        db_table = 'banco'

class Tipocontrato(BaseModel):
    clave = CharField(primary_key=True)
    descripcion = CharField(null=True)

    class Meta:
        db_table = 'tipoContrato'

class Cargo(BaseModel):
    activo = IntegerField(null=True)
    clave = CharField(primary_key=True)
    created_at = DateTimeField(null=True)
    descripcion = CharField(null=True)
    tipocontrato = ForeignKeyField(db_column='tipoContrato', null=True, rel_model=Tipocontrato, to_field='clave')
    updated_at = DateTimeField(null=True)
    zonaeco = CharField(db_column='zonaEco', null=True)

    class Meta:
        db_table = 'cargo'

class Concepto(BaseModel):
    activo = IntegerField(null=True)
    clave = CharField(null=True)
    clavesat = CharField(db_column='claveSat', null=True)
    concepto = CharField(null=True)
    created_at = DateTimeField(null=True)
    grabable = IntegerField(null=True)
    periodo = CharField(null=True)
    quincenaaplica = CharField(db_column='quincenaAplica', null=True)
    tipo = CharField(null=True)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'concepto'

class Quincena(BaseModel):
    anio = IntegerField(null=True)
    descripcion = CharField(null=True)
    id = CharField(primary_key=True)
    mes = IntegerField(null=True)
    ordinal = CharField(null=True)
    quincena = IntegerField(null=True)

    class Meta:
        db_table = 'quincena'

class Nomina(BaseModel):
    activo = IntegerField(null=True)
    created_at = DateTimeField(null=True)
    descripcion = CharField(null=True)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'nomina'

class Nominaquincena(BaseModel):
    cierre = DateTimeField(null=True)
    comentario = CharField(null=True)
    created_at = DateTimeField(null=True)
    estado = CharField(null=True)
    fin = DateField(null=True)
    inicio = DateField(null=True)
    nomina = ForeignKeyField(db_column='nomina', null=True, rel_model=Nomina, to_field='id')
    quincena = ForeignKeyField(db_column='quincena', null=True, rel_model=Quincena, to_field='id')
    tipo = CharField(null=True)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'nominaQuincena'

class Persona(BaseModel):
    curp = CharField(null=True)
    fechanacimiento = DateField(null=True)
    homoclave = CharField(null=True)
    nombre = CharField(null=True)
    primerapellido = CharField(db_column='primerApellido', null=True)
    rfc = CharField(primary_key=True)
    segundoapellido = CharField(db_column='segundoApellido', null=True)
    sexo = CharField(null=True)

    class Meta:
        db_table = 'persona'

class Variantecontrato(BaseModel):
    activo = CharField(null=True)
    created_at = DateTimeField(null=True)
    tipocontrato = ForeignKeyField(db_column='tipoContrato', null=True, rel_model=Tipocontrato, to_field='clave')
    updated_at = DateTimeField(null=True)
    variante = CharField(null=True)

    class Meta:
        db_table = 'varianteContrato'

class Empleado(BaseModel):
    variante = ForeignKeyField(db_column='Variante', null=True, rel_model=Variantecontrato, to_field='id')
    activo = IntegerField(null=True)
    adscripcion = ForeignKeyField(db_column='adscripcion', null=True, rel_model=Adscripcion, to_field='clave')
    cargo = ForeignKeyField(db_column='cargo', null=True, rel_model=Cargo, to_field='clave')
    created_at = DateTimeField(null=True)
    fin = DateField(null=True)
    inicio = DateField(null=True)
    numero = CharField(null=True)
    rfc = CharField(null=True)
    tipocontrato = ForeignKeyField(db_column='tipoContrato', null=True, rel_model=Tipocontrato, to_field='clave')
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'empleado'

class Datosnomina(BaseModel):
    adscripcion = CharField(null=True)
    banco = CharField(null=True)
    correo = CharField(null=True)
    created_at = DateTimeField(null=True)
    cuenta = CharField(null=True)
    empleado = ForeignKeyField(db_column='empleado', null=True, rel_model=Empleado, to_field='id')
    nominaquincena = ForeignKeyField(db_column='nominaQuincena', null=True, rel_model=Nominaquincena, to_field='id')
    rfc = ForeignKeyField(db_column='rfc', null=True, rel_model=Persona, to_field='rfc')
    tipopago = CharField(db_column='tipoPago', null=True)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'datosNomina'

class Conceptosnomina(BaseModel):
    comentario = CharField(null=True)
    concepto = ForeignKeyField(db_column='concepto', null=True, rel_model=Concepto, to_field='id')
    datosnomina = ForeignKeyField(db_column='datosNomina', null=True, rel_model=Datosnomina, to_field='id')
    tipo = CharField(null=True)

    class Meta:
        db_table = 'conceptosNomina'

class Contacto(BaseModel):
    predeterminado = IntegerField(null=True)
    rfc = ForeignKeyField(db_column='rfc', null=True, rel_model=Persona, to_field='rfc')
    tipoacceso = IntegerField(db_column='tipoAcceso', null=True)
    tipovalor = CharField(db_column='tipoValor', null=True)
    valor = CharField(null=True)

    class Meta:
        db_table = 'contacto'

class Contratonomina(BaseModel):
    activo = IntegerField(null=True)
    nomina = ForeignKeyField(db_column='nomina', null=True, rel_model=Nomina, to_field='id')
    tipocontrato = ForeignKeyField(db_column='tipoContrato', null=True, rel_model=Tipocontrato, to_field='clave')
    variante = ForeignKeyField(db_column='variante', null=True, rel_model=Variantecontrato, to_field='id')

    class Meta:
        db_table = 'contratoNomina'

class Datospersonales(BaseModel):
    created_at = DateTimeField(null=True)
    direccion = CharField(null=True)
    fechanacimiento = DateField(db_column='fechaNacimiento', null=True)
    rfc = ForeignKeyField(db_column='rfc', null=True, rel_model=Persona, to_field='rfc')
    sexo = CharField(null=True)
    tiposangre = CharField(db_column='tipoSangre', null=True)
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'datosPersonales'

class Empleadoconcepto(BaseModel):
    activo = IntegerField(null=True)
    comentario = CharField(null=True)
    concepto = ForeignKeyField(db_column='concepto', null=True, rel_model=Concepto, to_field='id')
    created_at = DateTimeField(null=True)
    empleado = ForeignKeyField(db_column='empleado', null=True, rel_model=Empleado, to_field='id')
    repetir = IntegerField(null=True)
    updated_at = DateTimeField(null=True)
    valor = IntegerField(null=True)

    class Meta:
        db_table = 'empleadoConcepto'

class Pago(BaseModel):
    banco = ForeignKeyField(db_column='banco', null=True, rel_model=Banco, to_field='clave')
    cuenta = CharField(null=True)
    rfc = ForeignKeyField(db_column='rfc', null=True, rel_model=Persona, to_field='rfc')
    tipo = IntegerField(null=True)

    class Meta:
        db_table = 'pago'

class User(BaseModel):
    created_at = DateTimeField(null=True)
    password = CharField()
    updated_at = DateTimeField(null=True)
    username = CharField(primary_key=True)

    class Meta:
        db_table = 'user'

