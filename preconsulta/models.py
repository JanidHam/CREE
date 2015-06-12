
from django.db import models
from userprofiles.models import UserProfile
from catalogos.models import *

# Create your models here.

class Paciente(models.Model):
	#Datos personales
	nombre           = models.CharField(max_length=80)
	apellidoP        = models.CharField(max_length=80)
	apellidoM        = models.CharField(max_length=80, blank=True)
	curp             = models.CharField(unique=True, max_length=50)
	edad             = models.IntegerField()
	genero           = models.IntegerField()
	fechanacimiento  = models.DateField()
	telefonocasa     = models.CharField(max_length=20, blank=True)
	telefonocelular  = models.CharField(max_length=20, blank=True)
	localidad        = models.CharField(max_length=200, blank=True)
	foto_perfil      = models.ImageField(upload_to='pacientes/imagesProfiles', verbose_name='FotoPerfil', blank=True)
	#Relaciones con otras tablas	
	estadoprocedente = models.ForeignKey(Estado, related_name='paciente_estadoprocedente')
	municipio        = models.ForeignKey(Municipio, related_name='paciente_municipio')
	referidopor      = models.ForeignKey(Referidopor, related_name='paciente_referidopor')
	escolaridad      = models.ForeignKey(Escolaridad, related_name='paciente_escolaridad')
	ocupacion        = models.ForeignKey(Ocupacion, related_name='paciente_ocupacion')
	#Domicilio
	calle            = models.CharField(max_length=200)
	entrecalles      = models.CharField(max_length=200, blank=True)
	colonia          = models.CharField(max_length=200)
	numerocasa       = models.CharField(max_length=20, blank=True)
	codigopostal     = models.IntegerField()
	#Otros datos
	#correspondio    = models.BooleanField()
	correspondio     = models.NullBooleanField()
	usuariocreacion  = models.ForeignKey(UserProfile, related_name='paciente_usuario')
	#creadopor       = models.CharField(max_length=255)
	fechacreacion    = models.DateField(auto_now_add=True)#el auto_now_add sirve para poner la fecha de creacion sin el add se pone la fecha en la que se modifica
	fechavisita      = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.curp + " - " + self.nombre + " " + self.apellidoP

class Expediente(models.Model):
	claveexpediente = models.CharField(unique=True, max_length=50)
	paciente        = models.ForeignKey(Paciente, related_name='expediente_paciente')
	fechacreacion   = models.DateField(auto_now_add=True)
	fechaalta       = models.DateField(blank=True)
	clue            = models.CharField(blank=True, max_length=10)
	servicios       = models.ManyToManyField(ServicioCree, through='ServicioExpediente')
	programas       = models.ManyToManyField(ProgramaCree, through='ProgramaExpediente')
	is_active       = models.BooleanField(default=True)
	iscincomil      = models.BooleanField(default=False)
	#fechaalta = models.DateField(auto_now=True)
	def __unicode__(self):
		return self.claveexpediente + " " + self.paciente.nombre + " " + self.paciente.apellidoP

class PacienteDataEnfermeria(models.Model):
	paciente            = models.ForeignKey(Paciente, related_name='dataenfermeria_paciente')
	edad                = models.IntegerField()
	peso                = models.CharField(max_length=10)
	talla               = models.CharField(max_length=20)
	f_c                 = models.CharField(max_length=20)
	t_a                 = models.CharField(max_length=20)
	glucosa             = models.CharField(max_length=20)
	cintura             = models.CharField(max_length=20)
	enfermera           = models.ForeignKey(UserProfile, related_name='dataenfermeria_usuario')
	fechacreacion       = models.DateField(auto_now_add=True)
	mensaje_informativo = models.CharField(max_length=255)

	def __unicode__(self):
		return str(self.pk) + " " + self.paciente.nombre + " " + self.paciente.apellidoP

#Aqui empiezan los modelos relacionados con los expedientes
class HojaPrevaloracion(models.Model):
	motivoconsulta         = models.TextField()
	diagnosticonosologico  = models.TextField()
	psicologia             = models.TextField(blank=True)
	diagnosticonosologico2 = models.TextField(blank=True)
	canalizacion           = models.TextField()
	fechacreacion          = models.DateField(auto_now_add=True)
	edad                   = models.IntegerField()
	#Relaciones con otras tablas
	ocupacion              = models.ForeignKey(Ocupacion, related_name='hojaprevaloracion_ocupacion')
	escolaridad            = models.ForeignKey(Escolaridad, related_name='hojaprevaloracion_escolaridad')
	referidopor            = models.ForeignKey(Referidopor, related_name='hojaprevaloracion_referidopor')
	doctor                 = models.ForeignKey(UserProfile, related_name='hojaprevaloracion_doctor')
	psicologo              = models.ForeignKey(UserProfile, related_name='hojaprevaloracion_psicologo')
	expediente             = models.ForeignKey(Expediente, related_name='hojaprevaloracion_expediente')

	def __unicode__(self):
		return "ID: " + str(self.id) + " " + self.expediente.claveexpediente + " - " + self.expediente.paciente.nombre + " " + self.expediente.paciente.apellidoP

class ServicioExpediente(models.Model):
	expediente        = models.ForeignKey(Expediente)
	servicio          = models.ForeignKey(ServicioCree)
	hojaPrevaloracion = models.ForeignKey(HojaPrevaloracion)
	fechaBaja         = models.DateField(blank=True)
	is_active         = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.servicio.servicio + " - " + self.expediente.claveexpediente

class ProgramaExpediente(models.Model):
	expediente        = models.ForeignKey(Expediente)
	programa          = models.ForeignKey(ProgramaCree)
	is_active         = models.BooleanField(default=True)
	hojaPrevaloracion = models.ForeignKey(HojaPrevaloracion)
	fechaBaja         = models.DateField(blank=True)

	def __unicode__(self):
		return self.programa.programa + " - " + self.expediente.claveexpediente

class HojaFrontal(models.Model):
	edad                  = models.IntegerField()
	fechacreacion         = models.DateField(auto_now_add=True)
	diagnosticonosologico = models.TextField()
	usuario               = models.ForeignKey(UserProfile, related_name='hojafrontal_usuario')
	expediente            = models.ForeignKey(Expediente, related_name='hojafrontal_expediente')

	def __unicode__(self):
		return "ID: " + str(self.id) + " " + self.expediente.claveexpediente + " - " + self.expediente.paciente.nombre + " " + self.expediente.paciente.apellidoP

class HojaReferencia(models.Model):
	folio               = models.CharField(max_length=50)
	nombre              = models.CharField(max_length=80)
	apellidoP           = models.CharField(max_length=80)
	apellidoM           = models.CharField(max_length=80, blank=True)
	curp                = models.CharField(max_length=50)
	edad                = models.IntegerField()
	genero              = models.IntegerField()
	fechacreacion       = models.DateField(auto_now_add=True)
	diagnostico         = models.TextField()
	antecedentes        = models.TextField()
	padecimiento_actual = models.TextField()
	tratamientos        = models.TextField()
	estudios_realizados = models.TextField()
	usuario             = models.ForeignKey(UserProfile, related_name='hojareferencia_usuario')

	def __unicode__(self):
		return "ID: " + str(self.id) + " - " + self.nombre + " " + self.apellidoP

class HistoriaClinica(models.Model):
	edad                  = models.IntegerField()
	fechacreacion         = models.DateTimeField(auto_now_add=True)
	interrogatorio        = models.IntegerField()
	motivoconsulta        = models.TextField()
	AHF                   = models.TextField()
	APNP                  = models.TextField()
	DPM                   = models.TextField()
	APP                   = models.TextField()
	PA                    = models.TextField()
	EF                    = models.TextField()
	estudiosdiagnostico   = models.TextField()
	diagnosticonosologico = models.TextField()
	pronostico            = models.TextField()
	plantratamiento       = models.TextField()
	#Relaciones con otras tablas
	doctor                = models.ForeignKey(UserProfile, related_name='historiaclinica_doctor')
	ocupacion             = models.ForeignKey(ServicioCree, related_name='historiaclinica_servicio')
	expediente            = models.ForeignKey(Expediente, related_name='historiaclinica_expediente')

class TarjetonTerapia(models.Model):
	edad                 = models.IntegerField()
	fechacreacion        = models.DateTimeField(auto_now_add=True)
	doctor               = models.ForeignKey(UserProfile, related_name='tarjetonterapia_doctor')
	fechaingresoterapias = models.DateField(auto_now_add=True)
	diagnostico          = models.TextField()
	indicaciones         = models.TextField()
	expediente           = models.ForeignKey(Expediente, related_name='tarjetonterapia_expediente')

class CartaConsetimiento(models.Model):
	edad                    = models.IntegerField()
	fechacreacion           = models.DateField(auto_now_add=True)
	#diagnostico            = models.TextField() no lleva diagnostico
	#Responsable del paciente
	nombreresponsable       = models.CharField(blank=True,max_length=150)
	apellidosresponsable    = models.CharField(blank=True,max_length=150)
	edadresponsable         = models.CharField(blank=True, max_length=15)
	generoresponsable       = models.CharField(blank=True, max_length=15)
	telefonoresponsable     = models.CharField(blank=True, max_length=15)
	parentescoresponsable   = models.CharField(blank=True,max_length=50)
	#Domicilio del responsable
	#calleresponsable        = models.CharField(max_length=200)
	#entrecallesresponsable  = models.CharField(max_length=200)
	#numerocasaresponsable   = models.CharField(max_length=20)
	domicilioresponsable    = models.CharField(blank=True,max_length=255)
	coloniaresponsable      = models.CharField(blank=True,max_length=200)
	codigopostalresponsable = models.CharField(blank=True, max_length=15)
	#Domicilio paciente
	calle                   = models.CharField(max_length=200)
	entrecalles             = models.CharField(max_length=200)
	numerocasa              = models.CharField(max_length=20)
	colonia                 = models.CharField(max_length=200)
	codigopostal            = models.IntegerField()
	#Relaciones con otras tablas	
	estadoprocedente        = models.ForeignKey(Estado, related_name='cartaconsentimiento_estadoprocedente')
	municipio               = models.ForeignKey(Municipio, related_name='cartaconsentimiento_municipio')
	doctor                  = models.ForeignKey(UserProfile, related_name='cartaconsentimiento_doctor')
	expediente              = models.ForeignKey(Expediente, related_name='cartaconsentimiento_expediente')

	def __unicode__(self):
		return self.expediente.claveexpediente

class EstudioSocioE1(models.Model):
	edad                   = models.IntegerField()
	estadocivil            = models.CharField(max_length=20)
	fechaestudio           = models.DateField(auto_now_add=True)
	consultorio            = models.IntegerField()
	#Entrevistado
	nombreentevistado      = models.CharField(max_length=200)
	apellidosentevistado   = models.CharField(max_length=200)
	parentescoentrevistado = models.CharField(max_length=20)
	#Domicilio paciente
	calle                  = models.CharField(max_length=200)
	entrecalles            = models.CharField(max_length=200)
	colonia                = models.CharField(max_length=200)
	numerocasa             = models.CharField(max_length=20)
	codigopostal           = models.IntegerField()
	motivoclasificacion    = models.TextField(blank=True)
	#Relaciones con otras tablas	
	clasificacion          = models.ForeignKey(ClasificacionEconomica, related_name='estudiosocioe1_clasificacion')
	seguridad_social       = models.ForeignKey(SeguridadSocial, related_name='estudiosocioe1_seguridadsocial')
	ocupacion              = models.ForeignKey(Ocupacion, related_name='estudiosocioe1_ocupacion')
	escolaridad            = models.ForeignKey(Escolaridad, related_name='estudiosocioe1_escolaridad')
	servicio               = models.ForeignKey(ServicioCree, related_name='estudiosocioe1_escolaridad')
	motivoestudio          = models.ForeignKey(MotivoEstudioSE, related_name='estudiosocioe1_escolaridad')
	expediente             = models.ForeignKey(Expediente, related_name='estudiosocioe1_expediente')
	usuariocreacion        = models.ForeignKey(UserProfile, related_name='estudiosocioe1_usuario')

	def __unicode__(self):
		return str(self.pk) + " - " + self.expediente.claveexpediente

class EstructuraFamiliaESE1(models.Model):
	nombrefamiliar    = models.CharField(max_length=200)
	apellidosfamiliar = models.CharField(max_length=200)
	parentesco        = models.CharField(max_length=20)
	estadocivil       = models.CharField(max_length=20)
	edad              = models.IntegerField()
	#Relaciones con otras tablas	
	estudiose         = models.ForeignKey(EstudioSocioE1, related_name='estructurafamiliar_estudiosocioe1')
	ocupacion         = models.ForeignKey(Ocupacion, related_name='estructurafamiliar_ocupacion')
	escolaridad       = models.ForeignKey(Escolaridad, related_name='estructurafamiliar_escolaridad')

	def __unicode__(self):
		return str(self.estudiose.id) + " - " + self.estudiose.expediente.claveexpediente

class EstudioSocioE2(models.Model):
	deficit               = models.IntegerField(blank=True)
	excedente             = models.IntegerField(blank=True)
	datosignificativo     = models.TextField()
	diagnosticoplansocial = models.TextField()
	cantidadbanios        = models.IntegerField()
	cantidadrecamaras     = models.IntegerField()
	#Relaciones con otras tablas	
	estudiose             = models.ForeignKey(EstudioSocioE1, related_name='estudiosocioe2_estudiosocioe1')
	#usuariocreacion      = models.ForeignKey(UserProfile, related_name='estudiosocioe2_usuario')
	vivienda              = models.ForeignKey(TipoVivienda, related_name='estudiosocioe2_vivienda')
	componentevivienda    = models.ManyToManyField(ComponenteVivienda, related_name='estudiosocioe2_componente')
	serviciovivienda      = models.ManyToManyField(ServicioVivienda, related_name='estudiosocioe2_servicio')
	tenenciavivienda      = models.ManyToManyField(TenenciaVivienda, related_name='estudiosocioe2_tenencia')
	construccionvivienda  = models.ManyToManyField(ConstruccionVivienda, related_name='estudiosocioe2_construccion')
	barreravivienda       = models.ManyToManyField(BarreraArquitectonicaVivienda, related_name='estudiosocioe2_barrera')
	ingresos_egresos      = models.ManyToManyField(IngresosEgresos, through='EstudioSocioE2IngresosEgresos')

	def __unicode__(self):
		return str(self.pk) + " - " + self.estudiose.expediente.claveexpediente

class EstudioSocioE2IngresosEgresos(models.Model):
	ingreso_egreso = models.ForeignKey(IngresosEgresos)
	estudio        = models.ForeignKey(EstudioSocioE2)
	monto          = models.IntegerField()	

	def __unicode__(self):
		return str(self.estudio.id) + " " + self.ingreso_egreso.tipo + ": " + self.ingreso_egreso.descripcion + " " + str(self.monto)
#Fin de los modelos relacionados con los expedientes