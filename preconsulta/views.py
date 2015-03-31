from django.db import IntegrityError, transaction
from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, Http404
from .models import Paciente, HojaPrevaloracion, Expediente, HojaFrontal, ServicioExpediente
from catalogos.models import Municipio, Estado, Ocupacion, Escolaridad, Referidopor, ServicioCree, ProgramaCree, MotivoEstudioSE, IngresosEgresos, TipoVivienda, ComponenteVivienda, ServicioVivienda, TenenciaVivienda, ConstruccionVivienda, BarreraArquitectonicaVivienda
from .utils import getUpdateConsecutiveExpendiete
from datetime import date
import sys
# Create your views here.
SERVICIO_ESTUDIO_SOCIOECONOMICO1 = "PRECONSULTA"
SERVICIO_PSICOLOGIA = "PSICOLOGIA"
INGRESO = "INGRESO"
EGRESO = "EGRESO"
EXTERNAS = "EXTERNAS"
INTERNAS = "INTERNAS"


def home(request):
	ocupaciones = Ocupacion.objects.all()
	escoliridades = Escolaridad.objects.all()
	referidospor = Referidopor.objects.all()
	municipios = Municipio.objects.all()
	estados = Estado.objects.all()
	pacientes = Paciente.objects.all().order_by('-id')
	contexto = {'ocupaciones' : ocupaciones, 'escolaridades' : escoliridades, 'referidospor' : referidospor,
	            'municipios' : municipios, 'estados' : estados, 'pacientes' : pacientes}
	return render_to_response('preconsulta/Prevaloracion.html', contexto, context_instance=RequestContext(request))

def revisionMedica(request, paciente):
	servicios = ServicioCree.objects.filter(is_active=True)
	programas = ProgramaCree.objects.filter(is_active=True)
	contexto = {'servicios' : servicios, 'programas' : programas, 'curp' : paciente}
	return render_to_response('preconsulta/PrevaloracionMedica.html', contexto, context_instance=RequestContext(request))

def psicologicaPrevaloracion(request, paciente):
	contexto = {'curp' : paciente}
	return render_to_response('preconsulta/PrevaloracionPsicologica.html', contexto, context_instance=RequestContext(request))

def estudioSPrevaloracion(request, paciente):
	ocupaciones = Ocupacion.objects.filter(is_active=True)
	motivosEstudio = MotivoEstudioSE.objects.filter(is_active=True)
	ingresos = IngresosEgresos.objects.filter(tipo=INGRESO, is_active=True)
	egresos = IngresosEgresos.objects.filter(tipo=EGRESO, is_active=True)
	tipoVivienda = TipoVivienda.objects.filter(is_active=True)
	componenteVivienda = ComponenteVivienda.objects.filter(is_active=True)
	servicioVivienda = ServicioVivienda.objects.filter(is_active=True)
	tenenciaVivienda = TenenciaVivienda.objects.filter(is_active=True)
	construccionVivienda = ConstruccionVivienda.objects.filter(is_active=True)
	barrerasInternasVivienda = BarreraArquitectonicaVivienda.objects.filter(tipo=INTERNAS,is_active=True)
	barrerasExternasVivienda = BarreraArquitectonicaVivienda.objects.filter(tipo=EXTERNAS,is_active=True)

	contexto = {'ocupaciones' : ocupaciones, 'motivosEsutdio' : motivosEstudio, 'egresos' : egresos,
	'ingresos' : ingresos, 'tipoVivienda' : tipoVivienda, 'componentesVivienda' : componenteVivienda, 
	'servicioVivienda' : servicioVivienda, 'tenenciaVivienda' : tenenciaVivienda, 
	'construccionVivienda' : construccionVivienda, 'barrerasInternasVivienda' : barrerasInternasVivienda,
	'barrerasExternasVivienda' : barrerasExternasVivienda, 'curp' : paciente}
	return render_to_response('preconsulta/PrevaloracionEstudioS.html', contexto, context_instance=RequestContext(request))

@csrf_exempt
def addPsicologiaHojaPrevaloracion(request):
	if request.POST:
		try:
			with transaction.atomic():
				mensaje = "Error al actualizar la hoja de prevaloracion"

				paciente = Paciente.objects.get(curp=request.POST['curp'])
				expediente = Expediente.objects.get(paciente__id=paciente.id, is_active=True)
				hojaPrev = HojaPrevaloracion.objects.get(expediente__id=expediente.id, fechacreacion=date.today())
				
				hojaPrev.diagnosticonosologico2 = request.POST['diagnosticoNosologicoBreve']
				hojaPrev.psicologia = request.POST['psicologia']
				hojaPrev.psicologo_id = request.POST['usuario']
				hojaPrev.save()

				mensaje = "ok"
		except Exception:
			print sys.exc_info()
			mensaje = "Error al actualizar la hoja de prevaloracion"
		print mensaje
		response = JsonResponse({'isOk' : mensaje})
		return HttpResponse(response.content)
	else:
		raise Http404

@csrf_exempt
def addEstudioSocioeconomico(request):
	if request.POST:
		try:
			with transaction.atomic():
				mensaje = "Error al los estudios socio economicos"

				paciente = Paciente.objects.get(curp=request.POST['curp'])
				expediente = Expediente.objects.get(paciente__id=paciente.id, is_active=True)
				hojaPrev = HojaPrevaloracion.objects.get(expediente__id=expediente.id, fechacreacion=date.today())
				
				hojaPrev.diagnosticonosologico2 = request.POST['diagnosticoNosologicoBreve']
				hojaPrev.psicologia = request.POST['psicologia']
				hojaPrev.psicologo_id = request.POST['usuario']
				hojaPrev.save()

				mensaje = "ok"
		except Exception:
			print sys.exc_info()
			mensaje = "Error al actualizar la hoja de prevaloracion"
		print mensaje
		response = JsonResponse({'isOk' : mensaje})
		return HttpResponse(response.content)
	else:
		raise Http404

@csrf_exempt
def addHojaPrevaloracion(request):
	if request.POST:
		try:
			correspondio = False
			with transaction.atomic():				
				mensaje = "Error al crear la hoja de prevaloracion"
				paciente = Paciente.objects.get(curp=request.POST['curp'])

				servicios = request.POST.getlist('servicios')
				programas = request.POST.getlist('programas')

				if len(servicios) > 0:
					paciente.correspondio = True
					paciente.save()
					
					claveExpediente = getUpdateConsecutiveExpendiete()
					expediente = Expediente.objects.create(
						claveexpediente = claveExpediente,
						paciente_id = paciente.id,
						fechaalta = "2015-03-30",
						)

					hojaPreValoracion = HojaPrevaloracion.objects.create(
						motivoconsulta = request.POST['motivoConsulta'],
						diagnosticonosologico = request.POST['diagnosticoNosologico'],						
						canalizacion = request.POST['canalizacion'],
						edad = paciente.edad,
						ocupacion_id = paciente.ocupacion.id,
						referidopor_id = paciente.referidopor.id,
						escolaridad_id = paciente.escolaridad.id,
						doctor_id = 1,
						psicologo_id = 1,
						expediente_id = expediente.id
						)

					for servicio in servicios:
						ServicioExpediente.objects.create(
							expediente_id = expediente.id,
							servicio_id = servicio,
							hojaPrevaloracion_id = hojaPreValoracion.id,
							fechaBaja = date.today()
							)

					hojaFrontal = HojaFrontal.objects.create(
						edad = paciente.edad,
						diagnosticonosologico = request.POST['diagnosticoNosologico'],
						usuario_id = 1,
						expediente_id = expediente.id
						)

					correspondio = True
					#for servicio in servicios:						
					#	encuesta.preguntas.add(t)
				else:
					print paciente.correspondio
					paciente.correspondio = False
					paciente.save()

				mensaje = "ok"

		except Exception:
			print sys.exc_info()
			mensaje = "Error al crear la hoja de prevaloracion"		
		
		response = JsonResponse({'curp' : request.POST['curp'], 'correspondio' : correspondio,
								'isOk' : mensaje})
		return HttpResponse(response.content)
	else:
		raise Http404

@csrf_exempt
def agregar_paciente(request):
	if request.POST:
		#paciente = Paciente.objects().filter(curp=request.POST['curp'])
		try:			
			mensaje = "Error al crear el parciente"			
			#municipio = Municipio.objects.get(descripcion=request.POST['localidad'])
			#estado = Estado.objects.get(descripcion=request.POST['estado'])			
			Paciente.objects.create(
				nombre = request.POST['nombre'],
				apellidoP = request.POST['apellidoP'],
				apellidoM = request.POST['apellidoM'],
				curp = request.POST['curp'],
				edad = request.POST['edad'],
				genero = request.POST['genero'],
				fechanacimiento = request.POST['fechaN'],
				telefonocasa = request.POST['telCasa'],
				telefonocelular = request.POST['celular'],
				estadoprocedente_id = request.POST['estado'],
				municipio_id = 1,#request.POST['localidad'],
				calle = request.POST['calle'],
				entrecalles = request.POST['entreCalles'],
				colonia = request.POST['colonia'],
				numerocasa = request.POST['numCasa'],
				codigopostal = request.POST['codigoPostal'],
				ocupacion_id = request.POST['ocupacion'],
				referidopor_id = request.POST['referidopor'],
				escolaridad_id = request.POST['escolaridad'],
				#correspondio = request.POST[''],
				creadopor = request.POST['usuario'],
				)
			#paciente = serializers.serialize('json', Paciente.objects.get(curp=request.POST['curp']))			
			#paciente = Paciente.objects.get(curp=request.POST['curp'])
			#json.dumps({'paciente' : paciente})
			#response = JsonResponse({'nombrePaciente': 'Nuevo',
			#						'apellidoP' : 'Paciente'})
			mensaje = "ok"
		except Exception:
			print sys.exc_info()
			mensaje = "Error al crear el parciente"
		#json.dumps({'paciente' : paciente, 'isOk' : mensaje})
		#response = JsonResponse(paciente)
		response = JsonResponse({'nombre' : request.POST['nombre'],'apellidoP' : request.POST['apellidoP'],
		 'curp' : request.POST['curp'], 'correspondio' : 'None', 'isOk' : mensaje})
		return HttpResponse(response.content)
	else:
		raise Http404