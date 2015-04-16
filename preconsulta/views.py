from django.db import IntegrityError, transaction
from django.shortcuts import render, render_to_response, RequestContext, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse, HttpResponse, Http404
from .models import Paciente, HojaPrevaloracion, Expediente, HojaFrontal, ServicioExpediente, EstudioSocioE1, EstudioSocioE2, EstudioSocioE2IngresosEgresos, EstructuraFamiliaESE1
from catalogos.models import Municipio, Estado, Ocupacion, Escolaridad, Referidopor, ServicioCree, ProgramaCree, MotivoEstudioSE, IngresosEgresos, TipoVivienda, ComponenteVivienda, ServicioVivienda, TenenciaVivienda, ConstruccionVivienda, BarreraArquitectonicaVivienda, ClasificacionEconomica
from .utils import getUpdateConsecutiveExpendiete
from .decorators import redirect_view, validViewPermissionRevisionMedica, validViewPermissionRevisionPsicologica, validViewPermissionTrabajoSocial
from django.contrib.auth.models import User, Group
from datetime import date
import sys
import json
#import pdb

SERVICIO_ESTUDIO_SOCIOECONOMICO1 = "PRECONSULTA"
SERVICIO_PSICOLOGIA = "PSICOLOGIA"
CONSULTORIO = 1
INGRESO = "INGRESO"
EGRESO = "EGRESO"
EXTERNAS = "EXTERNAS"
INTERNAS = "INTERNAS"

@redirect_view
def home(request):
	#pdb.set_trace()
	ocupaciones = Ocupacion.objects.all()
	escoliridades = Escolaridad.objects.all()
	referidospor = Referidopor.objects.all()
	municipios = Municipio.objects.all()
	estados = Estado.objects.all()
	pacientes = Paciente.objects.all()
	grupo = ""
	try:
		request.user.groups.get(name='Informacion')
		grupo = "informacion"
	except Group.DoesNotExist:
		try:
			request.user.groups.get(name='RevisionMedica')
			grupo = "revisionMedica"
		except Group.DoesNotExist:
			try:
				request.user.groups.get(name='RevisionPsicologica')
				grupo = "revisionPsicologica"
			except Group.DoesNotExist:
				try:
					request.user.groups.get(name='TrabajoSocial')
					grupo = "trabajoSocial"
				except Group.DoesNotExist:
					grupo = ""
					
	contexto = {'ocupaciones' : ocupaciones, 'escolaridades' : escoliridades, 'referidospor' : referidospor,
	            'municipios' : municipios, 'estados' : estados, 'pacientes' : pacientes, 'grupo': grupo}
	return render_to_response('preconsulta/Prevaloracion.html', contexto, context_instance=RequestContext(request))

#@login_required(login_url='/login/')
@validViewPermissionRevisionMedica
def revisionMedica(request, paciente):
	tmppaciente = get_object_or_404(Paciente, curp=paciente)
	servicios = ServicioCree.objects.filter(is_active=True)
	programas = ProgramaCree.objects.filter(is_active=True)
	contexto = {'servicios' : servicios, 'programas' : programas, 'curp' : paciente}
	return render_to_response('preconsulta/PrevaloracionMedica.html', contexto, context_instance=RequestContext(request))

#@login_required(login_url='/login/')
@validViewPermissionRevisionPsicologica
def psicologicaPrevaloracion(request, paciente):
	tmppaciente = get_object_or_404(Paciente, curp=paciente)
	contexto = {'curp' : paciente}
	return render_to_response('preconsulta/PrevaloracionPsicologica.html', contexto, context_instance=RequestContext(request))

#@login_required(login_url='/login/')
@validViewPermissionTrabajoSocial
def estudioSPrevaloracion(request, paciente):
	tmppaciente = get_object_or_404(Paciente, curp=paciente)
	ocupaciones = Ocupacion.objects.filter(is_active=True)
	escolaridades = Escolaridad.objects.filter(is_active=True)
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
	clasificacionEconomica = ClasificacionEconomica.objects.filter(is_active=True)

	contexto = {'ocupaciones' : ocupaciones, 'motivosEsutdio' : motivosEstudio, 'egresos' : egresos,
	'ingresos' : ingresos, 'tipoVivienda' : tipoVivienda, 'componentesVivienda' : componenteVivienda, 
	'servicioVivienda' : servicioVivienda, 'tenenciaVivienda' : tenenciaVivienda, 
	'construccionVivienda' : construccionVivienda, 'barrerasInternasVivienda' : barrerasInternasVivienda,
	'barrerasExternasVivienda' : barrerasExternasVivienda, 'escolaridades' : escolaridades, 'curp' : paciente,
	'clasificacionEconomica' : clasificacionEconomica}
	return render_to_response('preconsulta/PrevaloracionEstudioS.html', contexto, context_instance=RequestContext(request))

@csrf_exempt
def addEstudioSocioeconomico(request):
	if request.POST:
		try:
			with transaction.atomic():
				mensaje = "Error al crear los estudios socio economicos"
				#pdb.set_trace()
				paciente   = Paciente.objects.get(curp=request.POST['curp'])
				expediente = Expediente.objects.get(paciente__id=paciente.id, is_active=True)
				
				estructuraFamiliar = request.POST.getlist('EstructuraF')				
				
				ingresos     = request.POST.getlist('ingresos')
				egresos      = request.POST.getlist('egresos')
				serviciosV   = request.POST.getlist('servicios')
				componentesV   = request.POST.getlist('componentes')
				construccionV = request.POST.getlist('construccion')
				tenenciasV    = request.POST.getlist('tenencias')
				barrerasIV    = request.POST.getlist('barrerasI')
				barrerasEV    = request.POST.getlist('barrerasE')						
				
				u = User.objects.get(username=request.user)
				estudio1 = EstudioSocioE1.objects.create(
					edad = paciente.edad,
					estadocivil = request.POST['estadoCivil'],
					consultorio = CONSULTORIO,#request.POST['consultorio'],
					nombreentevistado = request.POST['nombreEntrevistado'],
					apellidosentevistado = request.POST['apellidoEntrevistado'],
					calle = paciente.calle,
					entrecalles = paciente.entrecalles,
					colonia = paciente.colonia,
					numerocasa = paciente.numerocasa,
					codigopostal = paciente.codigopostal,
					clasificacion_id = 1,#request.POST['clasificacion'],
					ocupacion_id = paciente.ocupacion.id,
					escolaridad_id = paciente.escolaridad.id,
					servicio_id = 1,#request.POST['servicio'],
					motivoestudio_id = request.POST['motivoEstudio'],
					expediente_id = expediente.id,
					usuariocreacion_id = u.perfil_usuario.id,#request.POST['usuario'],
					)

				for i in estructuraFamiliar:
					estructura = json.loads(i)
					EstructuraFamiliaESE1.objects.create(
						nombrefamiliar = estructura['nombreF'],
						apellidosfamiliar = estructura['apellidosF'],
						parentesco = estructura['parentescoF'],
						estadocivil = estructura['estadoCivilF'],
						estudiose_id = estudio1.id,
						ocupacion_id = estructura['ocupacionF'],
						escolaridad_id = estructura['escolaridadF'],
						)
				
				estudio2 = EstudioSocioE2.objects.create(
					deficit = request.POST['deficit'],
					excedente = request.POST['excedente'],
					datosignificativo = request.POST['datosSignificativos'],
					diagnosticoplansocial = request.POST['diagnosticoPlanS'],
					cantidadbanios = request.POST['cantidadBanios'],
					cantidadrecamaras = request.POST['cantidadRecamaras'],
					estudiose_id = estudio1.id,
					#usuariocreacion_id = 1,
					vivienda_id = request.POST['tipoVivienda']					
					)				
				
				for i in ingresos:
					ingreso = json.loads(i)
					EstudioSocioE2IngresosEgresos.objects.create(ingreso_egreso_id=ingreso['id'], estudio_id=estudio2.id, monto=ingreso['valor'])

				for i in egresos:
					egreso = json.loads(i)
					EstudioSocioE2IngresosEgresos.objects.create(ingreso_egreso_id=egreso['id'], estudio_id=estudio2.id, monto=egreso['valor'])								
				for i in serviciosV:
					estudio2.serviciovivienda.add(i)
					#servicio = ServicioVivienda.objects.filter(id=i)				
				for i in componentesV:
					estudio2.componentevivienda.add(i)
					#componente = ComponenteVivienda.objects.filter(id=i)
				for i in construccionV:
					estudio2.construccionvivienda.add(i)
					#contruccion = ConstruccionVivienda.objects.filter(id=i)
				for i in tenenciasV:
					estudio2.tenenciavivienda.add(i)
					#tenencia = TenenciaVivienda.objects.filter(id=i)
				for i in barrerasIV:
					estudio2.barreravivienda.add(i)
					#barreraI = BarreraArquitectonicaVivienda.objects.filter(id=i)
				for i in barrerasEV:
					estudio2.barreravivienda.add(i)
					#barreraE = BarreraArquitectonicaVivienda.objects.filter(id=i)

				mensaje = "ok"
		except Exception:
			print sys.exc_info()
			mensaje = "Error al crear los estudios socio economicos"
		
		response = JsonResponse({'isOk' : mensaje})
		return HttpResponse(response.content)
	else:
		raise Http404

#@csrf_exempt
def addPsicologiaHojaPrevaloracion(request):
	if request.POST:
		try:
			with transaction.atomic():
				mensaje = "Error al actualizar la hoja de prevaloracion"

				paciente = Paciente.objects.get(curp=request.POST['curp'])
				expediente = Expediente.objects.get(paciente__id=paciente.id, is_active=True)
				hojaPrev = HojaPrevaloracion.objects.get(expediente__id=expediente.id, fechacreacion=date.today())
				u = User.objects.get(username=request.user)
				
				hojaPrev.diagnosticonosologico2 = request.POST['diagnosticoNosologicoBreve']
				hojaPrev.psicologia = request.POST['psicologia']
				hojaPrev.psicologo_id = u.perfil_usuario.id
				hojaPrev.save()

				mensaje = "ok"
		except Exception:
			print sys.exc_info()
			mensaje = "Error al actualizar la hoja de prevaloracion"
		
		response = JsonResponse({'isOk' : mensaje})
		return HttpResponse(response.content)
	else:
		raise Http404

#@csrf_exempt
def addHojaPrevaloracion(request):
	if request.POST:
		try:
			correspondio = False
			with transaction.atomic():				
				mensaje = "Error al crear la hoja de prevaloracion"
				
				paciente = Paciente.objects.get(curp=request.POST['curp'])				
				if str(paciente.correspondio) == "True" or str(paciente.correspondio) == "False":
					mensaje = "Ya cuenta con una hoja de prevaloracion hecha el dia de hoy."
					response = JsonResponse({'curp' : request.POST['curp'], 'correspondio' : correspondio,
								'isOk' : mensaje})
					return HttpResponse(response.content)
				
				servicios = request.POST.getlist('servicios[]')
				programas = request.POST.getlist('programas[]')
				
				if len(servicios) > 0:
					paciente.correspondio = True
					paciente.save()
					
					claveExpediente = getUpdateConsecutiveExpendiete()
					expediente = Expediente.objects.create(
						claveexpediente = claveExpediente,
						paciente_id = paciente.id,
						fechaalta = "2015-03-30",
						)					
					u = User.objects.get(username=request.user)
					hojaPreValoracion = HojaPrevaloracion.objects.create(
						motivoconsulta = request.POST['motivoConsulta'],
						diagnosticonosologico = request.POST['diagnosticoNosologico'],						
						canalizacion = request.POST['canalizacion'],
						edad = paciente.edad,
						ocupacion_id = paciente.ocupacion.id,
						referidopor_id = paciente.referidopor.id,
						escolaridad_id = paciente.escolaridad.id,
						doctor_id = u.perfil_usuario.id,
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
						usuario_id = u.perfil_usuario.id,
						expediente_id = expediente.id
						)

					correspondio = True
				else:
					paciente.correspondio = False
					paciente.save()

				mensaje = "ok"

		except:
			print sys.exc_info()
			mensaje = "Error al crear la hoja de prevaloracion"		
		
		response = JsonResponse({'curp' : request.POST['curp'], 'correspondio' : correspondio,
								'isOk' : mensaje})
		return HttpResponse(response.content)
	else:
		raise Http404

def agregar_paciente(request):
	if request.is_ajax():
		#paciente = Paciente.objects().filter(curp=request.POST['curp'])
		try:			
			mensaje = "Error al crear el parciente"
			u = User.objects.get(username=request.user)
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
				usuariocreacion_id = u.perfil_usuario.id,
				)
			
			mensaje = "ok"
		except Exception:
			print sys.exc_info()
			mensaje = "Error al crear el parciente"
		
		response = JsonResponse({'nombre' : request.POST['nombre'],'apellidoP' : request.POST['apellidoP'],
		 'curp' : request.POST['curp'], 'correspondio' : 'None', 'isOk' : mensaje})
		return HttpResponse(response.content)
	else:
		raise Http404

def my_custom_page_not_found_view(request):
	render('404.html')