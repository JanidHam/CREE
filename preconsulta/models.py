from django.db import models
from userprofiles.models import UserProfile
from catalogos.models import *

# Create your models here.

class Paciente(models.Model):
	#Datos personales
	nombre = models.CharField(max_length=80)
	apellidoP = models.CharField(max_length=80)
	apellidoM = models.CharField(max_length=80, blank=True)
	curp = models.CharField(unique=True, max_length=50)
	edad = models.IntegerField()
	genero = models.IntegerField()
	fechanacimiento = models.DateField()
	telefonocasa = models.IntegerField(blank=True)
	telefonocelular = models.IntegerField(blank=True)
	#Relaciones con otras tablas	
	estadoprocedente = models.ForeignKey(Estado, related_name='paciente_estadoprocedente')
	municipio = models.ForeignKey(Municipio, related_name='paciente_municipio')
	referidopor = models.ForeignKey(Referidopor, related_name='paciente_referidopor')
	escolaridad = models.ForeignKey(Escolaridad, related_name='paciente_escolaridad')
	ocupacion = models.ForeignKey(Ocupacion, related_name='paciente_ocupacion')
	#Domicilio
	calle = models.CharField(max_length=200)
	entrecalles = models.CharField(max_length=200, blank=True)
	colonia = models.CharField(max_length=200)
	numerocasa = models.CharField(max_length=20, blank=True)
	codigopostal = models.IntegerField()
	#Otros datos
	#correspondio = models.BooleanField()
	correspondio = models.NullBooleanField()
	creadopor = models.CharField(max_length=255)
	fechacreacion = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.curp + " - " + self.nombre + " " + self.apellidoP

class Expediente(models.Model):
	claveexpediente = models.CharField(unique=True, max_length=50)
	paciente = models.ForeignKey(Paciente, related_name='expediente_paciente')
	is_active = models.BooleanField(default=True)
	fechacreacion = models.DateField(auto_now=True)
	fechaalta = models.DateField(blank=True)
	servicios = models.ManyToManyField(ServicioCree, through='ServicioExpediente')
	#fechaalta = models.DateField(auto_now=True)
	def __unicode__(self):
		return self.claveexpediente + " " + self.paciente.nombre + " " + self.paciente.apellidoP

#Aqui empiezan los modelos relacionados con los expedientes
class HojaPrevaloracion(models.Model):
	motivoconsulta = models.TextField()
	diagnosticonosologico = models.TextField()
	psicologia = models.TextField(blank=True)
	diagnosticonosologico2 = models.TextField(blank=True)
	canalizacion = models.TextField()
	fechacreacion = models.DateField(auto_now=True)
	edad = models.IntegerField()
	#Relaciones con otras tablas
	ocupacion = models.ForeignKey(Ocupacion, related_name='hojaprevaloracion_ocupacion')
	escolaridad = models.ForeignKey(Escolaridad, related_name='hojaprevaloracion_escolaridad')
	referidopor = models.ForeignKey(Referidopor, related_name='hojaprevaloracion_referidopor')
	doctor = models.ForeignKey(UserProfile, related_name='hojaprevaloracion_doctor')
	psicologo = models.ForeignKey(UserProfile, related_name='hojaprevaloracion_psicologo')
	expediente = models.ForeignKey(Expediente, related_name='hojaprevaloracion_expediente')

class ServicioExpediente(models.Model):
	expediente = models.ForeignKey(Expediente)
	servicio = models.ForeignKey(ServicioCree)
	is_active = models.BooleanField(default=True)
	hojaPrevaloracion = models.ForeignKey(HojaPrevaloracion)
	fechaBaja = models.DateField(blank=True)

	def __unicode__(self):
		return self.servicio.servicio + " - " + self.expediente.claveexpediente

class HojaFrontal(models.Model):
	edad = models.IntegerField()
	fechacreacion = models.DateField(auto_now=True)
	diagnosticonosologico = models.TextField()
	usuario = models.ForeignKey(UserProfile, related_name='hojafrontal_usuario')
	expediente = models.ForeignKey(Expediente, related_name='hojafrontal_expediente')

class HistoriaClinica(models.Model):
	edad = models.IntegerField()
	fechacreacion = models.DateTimeField(auto_now=True)
	interrogatorio = models.IntegerField()
	motivoconsulta = models.TextField()
	AHF = models.TextField()
	APNP = models.TextField()
	DPM = models.TextField()
	APP = models.TextField()
	PA = models.TextField()
	EF = models.TextField()
	estudiosdiagnostico = models.TextField()
	diagnosticonosologico = models.TextField()
	pronostico = models.TextField()
	plantratamiento = models.TextField()
	#Relaciones con otras tablas
	doctor = models.ForeignKey(UserProfile, related_name='historiaclinica_doctor')
	ocupacion = models.ForeignKey(ServicioCree, related_name='historiaclinica_servicio')
	expediente = models.ForeignKey(Expediente, related_name='historiaclinica_expediente')

class TarjetonTerapia(models.Model):
	edad = models.IntegerField()
	fechacreacion = models.DateTimeField(auto_now=True)
	doctor = models.ForeignKey(UserProfile, related_name='tarjetonterapia_doctor')
	fechaingresoterapias = models.DateField(auto_now=True)
	diagnostico = models.TextField()
	indicaciones = models.TextField()
	expediente = models.ForeignKey(Expediente, related_name='tarjetonterapia_expediente')

class CartaConsetimiento(models.Model):
	edad = models.IntegerField()
	fechacreacion = models.DateTimeField(auto_now=True)
	diagnostico = models.TextField()
	#Responsable del paciente
	nombreresponsable = models.CharField(max_length=150)
	apellidosponsable = models.CharField(max_length=150)
	edadresponsable = models.IntegerField()
	genero = models.IntegerField()
	parentesco = models.CharField(max_length=50)
	#Domicilio del responsable
	calleresponsable = models.CharField(max_length=200)
	entrecallesresponsable = models.CharField(max_length=200)
	coloniaresponsable = models.CharField(max_length=200)
	numerocasaresponsable = models.CharField(max_length=20)
	codigopostalresponsable = models.IntegerField()
	#Domicilio paciente
	calle = models.CharField(max_length=200)
	entrecalles = models.CharField(max_length=200)
	colonia = models.CharField(max_length=200)
	numerocasa = models.CharField(max_length=20)
	codigopostal = models.IntegerField()
	#Relaciones con otras tablas	
	estadoprocedente = models.ForeignKey(Estado, related_name='cartaconsentimiento_estadoprocedente')
	municipio = models.ForeignKey(Municipio, related_name='cartaconsentimiento_municipio')
	doctor = models.ForeignKey(UserProfile, related_name='cartaconsentimiento_doctor')
	expediente = models.ForeignKey(Expediente, related_name='cartaconsentimiento_expediente')

class EstudioSocioE1(models.Model):
	edad = models.IntegerField()
	estadocivil = models.CharField(max_length=20)
	fechaestudio = models.DateField(auto_now=True)
	consultorio = models.IntegerField()
	#Entrevistado
	nombreentevistado = models.CharField(max_length=200)
	apellidosentevistado = models.CharField(max_length=200)
	#Domicilio paciente
	calle = models.CharField(max_length=200)
	entrecalles = models.CharField(max_length=200)
	colonia = models.CharField(max_length=200)
	numerocasa = models.CharField(max_length=20)
	codigopostal = models.IntegerField()
	#Relaciones con otras tablas	
	clasificacion = models.ForeignKey(ClasificacionEconomica, related_name='estudiosocioe1_estadoprocedente')
	ocupacion = models.ForeignKey(Ocupacion, related_name='estudiosocioe1_ocupacion')
	escolaridad = models.ForeignKey(Escolaridad, related_name='estudiosocioe1_escolaridad')
	servicio = models.ForeignKey(ServicioCree, related_name='estudiosocioe1_escolaridad')
	motivoestudio = models.ForeignKey(MotivoEstudioSE, related_name='estudiosocioe1_escolaridad')
	expediente = models.ForeignKey(Expediente, related_name='estudiosocioe1_expediente')
	usuariocreacion = models.ForeignKey(UserProfile, related_name='estudiosocioe1_usuario')
	#Faltan las relaciones de los miembros de la familia

class EstructuraFamiliaESE1(models.Model):
	nombrefamiliar = models.CharField(max_length=200)
	apellidosfamiliar = models.CharField(max_length=200)
	parentesco = models.CharField(max_length=20)
	#Relaciones con otras tablas	
	estudiose = models.ForeignKey(EstudioSocioE1, related_name='estructurafamiliar_estadoprocedente')
	ocupacion = models.ForeignKey(Ocupacion, related_name='estructurafamiliar_ocupacion')
	escolaridad = models.ForeignKey(Escolaridad, related_name='estructurafamiliar_escolaridad')

class EstudioSocioE2(models.Model):
	deficit = models.IntegerField()
	excedente = models.IntegerField()
	datosignificativo = models.TextField()
	diagnosticoplansocial = models.TextField()
	#Relaciones con otras tablas	
	estudiose = models.ForeignKey(EstudioSocioE1, related_name='estudiosocioe2_estadoprocedente')
	usuariocreacion = models.ForeignKey(UserProfile, related_name='estudiosocioe2_usuario')
	vivienda = models.ForeignKey(TipoVivienda, related_name='estudiosocioe2_vivienda')
	componentevivienda = models.ManyToManyField(ComponenteVivienda, related_name='estudiosocioe2_componente')
	serviciovivienda = models.ManyToManyField(ServicioVivienda, related_name='estudiosocioe2_servicio')
	tenenciavivienda = models.ManyToManyField(TenenciaVivienda, related_name='estudiosocioe2_tenencia')
	construccionvivienda = models.ManyToManyField(ConstruccionVivienda, related_name='estudiosocioe2_construccion')
	barreravivienda = models.ManyToManyField(BarreraArquitectonicaVivienda, related_name='estudiosocioe2_barrera')
	ingresos_egresos = models.ManyToManyField(IngresosEgresos, through='EstudioSocioE2IngresosServicios')

class EstudioSocioE2IngresosServicios(models.Model):
	ingreso_egreso = models.ForeignKey(IngresosEgresos)
	estudio = models.ForeignKey(EstudioSocioE2)
	monto = models.IntegerField()	

	def __unicode__(self):
		return self.ingreso_egregso.tipo + ": " + self.ingreso_egregso.descripcion + str(monto)
#Fin de los modelos relacionados con los expedientes