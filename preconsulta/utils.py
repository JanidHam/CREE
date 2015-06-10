from catalogos.models import ConsecutivoExpendiente
from datetime import date

def getUpdateConsecutiveExpendiete():
	anio = date.today().year

	consecutivo = ConsecutivoExpendiente.objects.get(anio_actual=anio)

	consecutivoActual = consecutivo.consecutivo
	consecutivo.consecutivo += 1
	consecutivo.save()

	anioExpediente = str(anio)
	anioExpediente = anioExpediente[2:4]
	clave = "%04d" % (consecutivoActual,)
	clave += "-%s" % anioExpediente
	return clave

def getClueExpediente(localidad, lista, claveSeguridadSocial):

	if localidad in lista:
		return "%d-%s" %(1, claveSeguridadSocial)
	else:
		return "%d-%s" %(0, claveSeguridadSocial)
