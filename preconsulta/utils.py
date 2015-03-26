from catalogos.models import ConsecutivoExpendiente
from datetime import date

def getUpdateConsecutiveExpendiete():
	anio = date.today().year
	print "aqui ando"
	consecutivo = ConsecutivoExpendiente.objects.get(anio_actual=anio)
	print consecutivo
	consecutivoActual = consecutivo.consecutivo
	consecutivo.consecutivo += 1
	consecutivo.save()

	anioExpediente = str(anio)
	anioExpediente = anioExpediente[2:4]
	clave = "%04d" % (consecutivoActual,)
	clave += "-%s" % anioExpediente
	return clave