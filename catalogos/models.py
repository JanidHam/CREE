from django.db import models

# Create your models here.
#Modelos de los catalogos relacionados con el proceso de prevaloracion
class ServicioCree(models.Model):
	servicio = models.CharField(max_length=150)
	is_active = models.BooleanField(default=True)
	#usuariobaja = models.ForeignKey(UserProfile, related_name='serivicio_usuario', blank=True)
	fechabaja = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.servicio

class ProgramaCree(models.Model):
	programa = models.CharField(max_length=150)
	is_active = models.BooleanField(default=True)
	#usuariobaja = models.ForeignKey(UserProfile, related_name='programa_usuario')
	fechabaja = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.programa

class ClasificacionEconomica(models.Model):
	clasificacion = models.CharField(max_length=20)
	is_active = models.BooleanField(default=True)

class MotivoEstudioSE(models.Model):
	motivoestudio = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)

class TipoVivienda(models.Model):
	vivienda = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)

class ComponenteVivienda(models.Model):
	componente = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)

class ServicioVivienda(models.Model):
	servicio = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)

class TenenciaVivienda(models.Model):
	tenencia = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)

class ConstruccionVivienda(models.Model):
	componente = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)

class BarreraArquitectonicaVivienda(models.Model):
	barrera = models.CharField(max_length=255)
	tipo = models.CharField(max_length=15)
	is_active = models.BooleanField(default=True)
#Fin de los catalogos del proceso de prevaloracion

"""
Apartir de aqui empieza la seccion donde iran todos los modelos de los catalogos 
de la app preconsulta.
"""
#Estos catalogos pertenecen a los pacientes
class Estado(models.Model):
	descripcion = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.descripcion

class Municipio(models.Model):
	descripcion = models.CharField(max_length=255)
	estado = models.ForeignKey(Estado, related_name='estado_municipio')

	def __unicode__(self):
		return self.descripcion + " - " + self.estado.descripcion
#Fin de los catalogos para pacientes

#Estos catalogos pertenecen a los expedientes
class Ocupacion(models.Model):
	descripcion = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.descripcion

class Escolaridad(models.Model):
	descripcion = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.descripcion

class Referidopor(models.Model):
	descripcion = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.descripcion
#Fin de los catalogos para expedientes