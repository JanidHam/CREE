from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, Http404
from .models import Paciente, HojaPrevaloracion
from catalogos.models import Municipio, Estado, Ocupacion, Escolaridad, Referidopor, ServicioCree, ProgramaCree
import sys
# Create your views here.
def home(request):
	ocupaciones = Ocupacion.objects.all()
	escoliridades = Escolaridad.objects.all()
	referidospor = Referidopor.objects.all()
	municipios = Municipio.objects.all()
	estados = Estado.objects.all()
	pacientes = Paciente.objects.all().order_by('-id')
	contexto = {'ocupaciones' : ocupaciones, 'escolaridades' : escoliridades, 'referidospor' : referidospor,
	            'municipios' : municipios, 'estados' : estados, 'pacientes' : pacientes}
	return render_to_response('preconsulta/BasePrevaloracion.html', contexto, context_instance=RequestContext(request))

def revisionMedica(request, paciente):
	servicios = ServicioCree.objects.filter(is_active=True)
	programas = ProgramaCree.objects.filter(is_active=True)
	contexto = {'servicios' : servicios, 'programas' : programas}
	return render_to_response('preconsulta/BasePrevaloracionMedica.html', contexto, context_instance=RequestContext(request))

def addHojaPrevaloracion(request, curp):
	if request.POST:
		try:			
			mensaje = "Error al crear la hoja de prevaloracion"			
			paciente = Paciente.objects.get(curp=curp)
			
			servicios = request.POST.getlist('servicios[]')
			if len(servicios) > 0:
				HojaPrevaloracion.objects.create(
					motivoconsulta = request.POST['movitoConsulta'],
					diagnosticonosologico = request.POST['diagnosticoNosologico'],
					diagnosticonosologico2 = request.POST['diagnosticoNosologico2'],
					canalizacion = request.POST['canalizacion'],
					edad = request.POST['edad'],
					ocupacion_id = paciente.ocupacion.id,
					referidopor_id = paciente.referidopor.id,
					escolaridad_id = paciente.escolaridad.id,
					doctor = request.POST['doctor'],
					psicologo = 1,

					)

				#for t in tasks:
				#	encuesta.preguntas.add(t)

			mensaje = "ok"

		except Exception:
			print sys.exc_info()
			mensaje = "Error al crear la hoja de prevaloracion"		
		response = JsonResponse({'nombre' : request.POST['nombre'],'apellidoP' : request.POST['apellidoP'],
		 'curp' : request.POST['curp'], 'correspondio' : 'None', 'isOk' : mensaje})
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