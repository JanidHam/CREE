from django.contrib import admin
from .models import *

class pacienteAdmin(admin.ModelAdmin):
	list_display = ('curp', 'nombre', 'apellidoP', 'apellidoM', 'edad', 'fechacreacion', 'correspondio')
	search_fields = ['curp', 'nombre', 'apellidoP', 'edad', 'fechacreacion']

class hojaPrevaloracionAdmin(admin.ModelAdmin):
	list_display = ('expediente', 'fechacreacion', 'doctor', 'psicologo')

# Register your models here.
admin.site.register(Paciente, pacienteAdmin)
admin.site.register(Expediente)
admin.site.register(EstudioSocioE2)
admin.site.register(EstudioSocioE1)
admin.site.register(HojaFrontal)
admin.site.register(HojaPrevaloracion, hojaPrevaloracionAdmin)
admin.site.register(ServicioExpediente)
admin.site.register(ProgramaExpediente)
admin.site.register(EstructuraFamiliaESE1)
admin.site.register(EstudioSocioE2IngresosEgresos)
admin.site.register(PacienteDataEnfermeria)
admin.site.register(HojaReferencia)
"""
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Ocupacion)
admin.site.register(Escolaridad)
admin.site.register(Referidopor)
admin.site.register(ServicioCree)
admin.site.register(ProgramaCree)
"""