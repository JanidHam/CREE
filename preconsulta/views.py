#from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError, transaction
from django.shortcuts import render, render_to_response, RequestContext, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse, HttpResponse, Http404
from .models import Paciente, HojaPrevaloracion, Expediente, HojaFrontal, ServicioExpediente, EstudioSocioE1, EstudioSocioE2, EstudioSocioE2IngresosEgresos, EstructuraFamiliaESE1, ProgramaExpediente, PacienteDataEnfermeria, CartaConsetimiento
from catalogos.models import Municipio, Estado, Ocupacion, Escolaridad, Referidopor, ServicioCree, ProgramaCree, MotivoEstudioSE, IngresosEgresos, TipoVivienda, ComponenteVivienda, ServicioVivienda, TenenciaVivienda, ConstruccionVivienda, BarreraArquitectonicaVivienda, ClasificacionEconomica, MensajesEnfemeriaTicket, EstadoCivil, Parentesco, MensajesCartaConsentimiento
from .utils import getUpdateConsecutiveExpendiete
from .decorators import redirect_view, validViewPermissionRevisionMedica, validViewPermissionRevisionPsicologica, validViewPermissionTrabajoSocial, validViewPermissionImprimirDocumentos, validViewPermissionEnfemeria
from django.contrib.auth.models import User, Group
from datetime import date, datetime
from logs import logger
import sys
import json
#import pdb

SERVICIO_ESTUDIO_SOCIOECONOMICO1 = "PRECONSULTA"
SERVICIOS_EXCLUIDOS_MEDICO = ("PSICOLOGIA", "TRABAJO SOCIAL")
PROGRAMAS_EXCLUIDOS_MEDICO = ("INCLUSION EDUCATIVA", "ESCUELA PARA FAMILIAS CON HIJOS CON DISCAPACIDAD", "INCLUSION LABORAL")
CONSULTORIO = 1
INGRESO = "INGRESO"
EGRESO = "EGRESO"
EXTERNAS = "EXTERNAS"
INTERNAS = "INTERNAS"

@redirect_view
def home(request):
	ocupaciones   = Ocupacion.objects.filter(is_active=True)
	escoliridades = Escolaridad.objects.filter(is_active=True)
	referidospor  = Referidopor.objects.filter(is_active=True)
	municipios    = Municipio.objects.all()
	estados       = Estado.objects.filter(is_active=True)
	pacientes     = Paciente.objects.filter(fechacreacion=date.today())
	grupo         = getUserGroupByRequest(request)
	
	contexto = {'ocupaciones' : ocupaciones, 'escolaridades' : escoliridades, 'referidospor' : referidospor,
	            'municipios' : municipios, 'estados' : estados, 'pacientes' : pacientes, 'grupo': grupo}
	return render_to_response('preconsulta/Prevaloracion.html', contexto, context_instance=RequestContext(request))

@validViewPermissionRevisionMedica
def revisionMedica(request, paciente):
	tmppaciente          = get_object_or_404(Paciente, curp=paciente)
	servicios            = ServicioCree.objects.filter(is_active=True).exclude(servicio__in=[s for s in SERVICIOS_EXCLUIDOS_MEDICO])
	programas            = ProgramaCree.objects.filter(is_active=True).exclude(programa__in=[p for p in PROGRAMAS_EXCLUIDOS_MEDICO])
	tmpHojaPrevaloracion = HojaPrevaloracion
	expediente           = Expediente
	try:
		expediente           = Expediente.objects.get(paciente__id=tmppaciente.id,is_active=True)
		tmpHojaPrevaloracion = HojaPrevaloracion.objects.get(expediente__id=expediente.id,fechacreacion=date.today())
	except:
		pass
		#expediente = Expediente
	
	contexto = {'servicios' : servicios, 'programas' : programas, 'curp' : paciente, 
				'hojaPrevaloracion': tmpHojaPrevaloracion, 'expediente': expediente}
	return render_to_response('preconsulta/PrevaloracionMedica.html', contexto, context_instance=RequestContext(request))

@validViewPermissionRevisionPsicologica
def psicologicaPrevaloracion(request, paciente):
	tmppaciente          = get_object_or_404(Paciente, curp=paciente)
	servicios            = ServicioCree.objects.filter(is_active=True, servicio__in=[s for s in SERVICIOS_EXCLUIDOS_MEDICO])
	programas            = ProgramaCree.objects.filter(is_active=True, programa__in=[p for p in PROGRAMAS_EXCLUIDOS_MEDICO])
	tmpHojaPrevaloracion = HojaPrevaloracion
	expediente           = Expediente
	try:
		expediente           = Expediente.objects.get(paciente__id=tmppaciente.id,is_active=True)
		tmpHojaPrevaloracion = HojaPrevaloracion.objects.get(expediente__id=expediente.id,fechacreacion=date.today())
	except:
		pass
		#expediente = Expediente
	contexto = {'curp' : paciente, 'servicios': servicios, 'programas': programas,
				'hojaPrevaloracion': tmpHojaPrevaloracion, 'expediente': expediente}
	return render_to_response('preconsulta/PrevaloracionPsicologica.html', contexto, context_instance=RequestContext(request))

@validViewPermissionEnfemeria
def enfermeriaPrevaloracion(request, paciente):
	tmppaciente            = get_object_or_404(Paciente, curp=paciente)
	nombreCompletoPaciente = "%s %s %s" %(tmppaciente.nombre, tmppaciente.apellidoP, tmppaciente.apellidoM)
	fechaActual            = datetime.now() #date.today()
	mensajeInformativo     = MensajesEnfemeriaTicket.objects.get(is_active=True)
	dataEnfermeria         = PacienteDataEnfermeria
	try:
		dataEnfermeria = PacienteDataEnfermeria.objects.get(paciente__id=tmppaciente.id,fechacreacion=date.today())
	except:
		pass
		#dataEnfermeria = PacienteDataEnfermeria
	contexto = {'curp' : paciente, 'edad' : tmppaciente.edad, 'nombreCompletoPaciente' :  nombreCompletoPaciente,
	'fecha' : fechaActual, 'mensajeInformativo' : mensajeInformativo, 'dataEnfermeria': dataEnfermeria}
	return render_to_response('preconsulta/PrevaloracionEnfermeria.html', contexto, context_instance=RequestContext(request))

@validViewPermissionTrabajoSocial
def estudioSPrevaloracion(request, paciente):
	tmppaciente              = get_object_or_404(Paciente, curp=paciente)
	ocupaciones              = Ocupacion.objects.filter(is_active=True)
	escolaridades            = Escolaridad.objects.filter(is_active=True)
	motivosEstudio           = MotivoEstudioSE.objects.filter(is_active=True)
	ingresos                 = IngresosEgresos.objects.filter(tipo=INGRESO, is_active=True)
	egresos                  = IngresosEgresos.objects.filter(tipo=EGRESO, is_active=True)
	tipoVivienda             = TipoVivienda.objects.filter(is_active=True)
	componenteVivienda       = ComponenteVivienda.objects.filter(is_active=True)
	servicioVivienda         = ServicioVivienda.objects.filter(is_active=True)
	tenenciaVivienda         = TenenciaVivienda.objects.filter(is_active=True)
	construccionVivienda     = ConstruccionVivienda.objects.filter(is_active=True)
	barrerasInternasVivienda = BarreraArquitectonicaVivienda.objects.filter(tipo=INTERNAS,is_active=True)
	barrerasExternasVivienda = BarreraArquitectonicaVivienda.objects.filter(tipo=EXTERNAS,is_active=True)
	clasificacionEconomica   = ClasificacionEconomica.objects.filter(is_active=True)
	estadoCivil              = EstadoCivil.objects.filter(is_active=True)
	parentesco               = Parentesco.objects.filter(is_active=True)
	estudioSE1               = EstudioSocioE1
	estudioSE2               = EstudioSocioE2
	expediente               = Expediente
	estructuraFamiliar       = EstructuraFamiliaESE1.objects
	ingresos_egresosEstudio  = EstudioSocioE2IngresosEgresos
	ingresos_egresos         = IngresosEgresos
	barrerasViviendaEstudio  = BarreraArquitectonicaVivienda
	barrerasVivienda         = BarreraArquitectonicaVivienda
	try:
		expediente              = Expediente.objects.get(paciente__id=tmppaciente.id, is_active=True)
		estudioSE1              = EstudioSocioE1.objects.get(expediente__id=expediente.id, fechaestudio=date.today())
		estudioSE2              = EstudioSocioE2.objects.get(estudiose__id=estudioSE1.id)
		estructuraFamiliar      = EstructuraFamiliaESE1.objects.filter(estudiose__id=estudioSE1.id)
		ingresos_egresosEstudio = EstudioSocioE2IngresosEgresos.objects.filter(estudio__id=estudioSE2.id) #Son los ingresos/egresos del estudio socio economico
		ingresos_egresos        = IngresosEgresos.objects.filter(is_active=True).exclude(id__in=[ie.ingreso_egreso.id for ie in ingresos_egresosEstudio]) #Son los ingresos/egresos del catalogo pero excluyendo los que tiene el estudio
		barrerasViviendaEstudio = estudioSE2.barreravivienda.all()
		barrerasVivienda        = BarreraArquitectonicaVivienda.objects.filter(is_active=True).exclude(id__in=[b.id for b in barrerasViviendaEstudio])
	except:
		ingresos_egresos = IngresosEgresos.objects.filter(is_active=True)
		barrerasVivienda = BarreraArquitectonicaVivienda.objects.filter(is_active=True)
	
	contexto = {
		'ocupaciones' : ocupaciones, 'motivosEsutdio' : motivosEstudio, 'egresos' : egresos,
		'ingresos' : ingresos, 'tipoVivienda' : tipoVivienda, 'componentesVivienda' : componenteVivienda,
		'servicioVivienda' : servicioVivienda, 'tenenciaVivienda' : tenenciaVivienda,
		'construccionVivienda' : construccionVivienda, 'barrerasInternasVivienda' : barrerasInternasVivienda,
		'barrerasExternasVivienda' : barrerasExternasVivienda, 'escolaridades' : escolaridades, 'curp' : paciente,
		'clasificacionEconomica' : clasificacionEconomica, 'estudioSE1': estudioSE1, 'estudioSE2': estudioSE2,
		'estructuraFamiliar': estructuraFamiliar, 'estadoCivil': estadoCivil, 'parentesco': parentesco,
		'ingresos_egresosEstudio': ingresos_egresosEstudio, 'ingresos_egresos': ingresos_egresos, 'barrerasVivienda': barrerasVivienda,
		'barrerasViviendaEstudio': barrerasViviendaEstudio
	}

	return render_to_response('preconsulta/PrevaloracionEstudioS.html', contexto, context_instance=RequestContext(request))

@validViewPermissionImprimirDocumentos
def imprimirDocumentos(request, paciente):
	paciente = get_object_or_404(Paciente, curp=paciente)
	"""
	Primero se hace el query de los encabezados (El expediente, hojas de prevaloracion y frontal, estudios socioeconomicos), 
	si no cuenta con alguno de ellos y si no se hicieron el mismo dia respondera con un error 404
	"""
	try:
		expediente          = Expediente.objects.get(paciente__id=paciente.id, is_active=True)
		hojaPrevaloracion   = HojaPrevaloracion.objects.get(expediente__id=expediente.id)
		serviciosExpediente = ServicioExpediente.objects.filter(expediente__id=expediente.id) #Los servicios con los que cuenta este expediente
		programasExpediente = ProgramaExpediente.objects.filter(expediente__id=expediente.id) #Los programas con los que cuenta este expediente
		servicios           = ServicioCree.objects.filter(is_active=True).exclude(id__in=[s.servicio.id for s in serviciosExpediente]) #Los servicios que ofrece el 'CREE' excluyendo los que tiene el expediente solicitado
		programas           = ProgramaCree.objects.filter(is_active=True).exclude(id__in=[p.programa.id for p in programasExpediente]) #Los programas que ofrece el 'CREE' excluyendo los que tiene el expediente solicitado
		
		hojaFrontal         = HojaFrontal.objects.filter(expediente__id=expediente.id)
		
		estudioSE1          = EstudioSocioE1.objects.get(expediente__id=expediente.id)
		estructuraFamiliar  = EstructuraFamiliaESE1.objects.filter(estudiose__id=estudioSE1.id)
		
		estudioSE2          = EstudioSocioE2.objects.get(estudiose__id=estudioSE1.id)
	except:
		raise Http404
	#tempIE = estudioSE2.ingresos_egresos.all()
	ingresos_egresosEstudio = EstudioSocioE2IngresosEgresos.objects.filter(estudio__id=estudioSE2.id) #Son los ingresos/egresos del estudio socio economico
	ingresos_egresos        = IngresosEgresos.objects.filter(is_active=True).exclude(id__in=[ie.ingreso_egreso.id for ie in ingresos_egresosEstudio]) #Son los ingresos/egresos del catalogo pero excluyendo los que tiene el estudio
	componentesViviendaE    = estudioSE2.componentevivienda.all()
	serviciosViviendaE      = estudioSE2.serviciovivienda.all()
	tenenciasViviendaE      = estudioSE2.tenenciavivienda.all()
	construccionViviendaE   = estudioSE2.construccionvivienda.all()
	barrerasViviendaE       = estudioSE2.barreravivienda.all()
	
	componentesVivienda     = ComponenteVivienda.objects.filter(is_active=True).exclude(id__in=[c.id for c in componentesViviendaE])
	serviciosVivienda       = ServicioVivienda.objects.filter(is_active=True).exclude(id__in=[s.id for s in serviciosViviendaE])
	tenenciasVivienda       = TenenciaVivienda.objects.filter(is_active=True).exclude(id__in=[t.id for t in tenenciasViviendaE])
	construccionVivienda    = ConstruccionVivienda.objects.filter(is_active=True).exclude(id__in=[con.id for con in construccionViviendaE])
	barrerasVivienda        = BarreraArquitectonicaVivienda.objects.filter(is_active=True).exclude(id__in=[b.id for b in barrerasViviendaE])
	
	rowsVacios              = 20 - len(serviciosExpediente)
	rows                    = list()
	for i in range(rowsVacios):
		rows.append(i)
	contexto = {'curp' : paciente.curp, 'paciente' : paciente, 'expediente' : expediente,
	 'hojaPrevaloracion': hojaPrevaloracion, 'hojaFrontal' : hojaFrontal, 'estudioSE1' : estudioSE1,
	 'estructuraFamiliar' : estructuraFamiliar, 'estudioSE2' : estudioSE2, 'serviciosExpediente': serviciosExpediente,
     'servicios' : servicios, 'programas' : programas, 'programasExpediente' : programasExpediente,
     'ingresos_egresos' : ingresos_egresos, 'ingresos_egresosEstudio' : ingresos_egresosEstudio,
     'componentesVivienda' : componentesVivienda, 'serviciosVivienda' : serviciosVivienda,
     'tenenciasVivienda' : tenenciasVivienda, 'construccionVivienda' : construccionVivienda,
     'barrerasVivienda' : barrerasVivienda, 'componentesViviendaE' : componentesViviendaE, 
     'serviciosViviendaE' : serviciosViviendaE, 'tenenciasViviendaE' : tenenciasViviendaE, 
     'construccionViviendaE' : construccionViviendaE, 'barrerasViviendaE' : barrerasViviendaE, 'rows' : rows}

	return render_to_response('preconsulta/ImprimirDocumentos.html', contexto, context_instance=RequestContext(request))

@validViewPermissionImprimirDocumentos
def imprimirDocumentosCaratula(request, paciente):
	paciente   = get_object_or_404(Paciente, curp=paciente)
	expediente = Expediente.objects.get(paciente__id=paciente.id, is_active=True)
	
	estudioSE1 = EstudioSocioE1.objects.get(expediente__id=expediente.id)

	contexto = {'curp' : paciente.curp, 'paciente' : paciente, 'expediente' : expediente, 
	'estudioSE1' : estudioSE1,}

	return render_to_response('preconsulta/ImprimirCaratula.html', contexto, context_instance=RequestContext(request))

def update_paciente(request):
	if request.POST:
		paciente = get_object_or_404(Paciente, curp=request.POST['curpPaciente'])
		try:
			mensaje = "Error al crear el parciente."
			u       = User.objects.get(username=request.user)
			
			paciente.curp                 = request.POST['curp']
			paciente.nombre               = request.POST['nombre']
			paciente.apellidoP            = request.POST['apellidoP']
			paciente.apellidoM            = request.POST['apellidoM']
			paciente.edad                 = request.POST['edad']
			paciente.genero               = request.POST['genero']
			paciente.fechanacimiento      = request.POST['fechaN']
			paciente.telefonocasa         = request.POST['telCasa']
			paciente.telefonocelular      = request.POST['celular']
			paciente.localidad            = request.POST['localidad']
			paciente.estadoprocedente__id = request.POST['estado']
			paciente.municipio__id        = request.POST['municipio']
			paciente.referidopor__id      = request.POST['referidopor']
			paciente.escolaridad__id      = request.POST['escolaridad']
			paciente.ocupacion__id        = request.POST['ocupacion']
			paciente.calle                = request.POST['calle']
			paciente.entrecalles          = request.POST['entreCalles']
			paciente.colonia              = request.POST['colonia']
			paciente.numerocasa           = request.POST['numCasa']
			paciente.codigopostal         = request.POST['codigoPostal']
			#paciente.usuariocreacion__id = u.perfil_usuario.id
			paciente.save()
			mensaje = "ok"
		except IntegrityError as e:
			logger.error(str(e))
			mensaje = "La curp del paciente ya existe en la base de datos."
		except ValueError as e:
			logger.error(str(e))
			mensaje = "Valor no valido, revisar los valores que se ingresan."
		except:
			logger.error(sys.exc_info()[0])
			mensaje = "Error al crear el parciente."
		response = JsonResponse({'isOk': mensaje})
		return HttpResponse(response.content)
	else:
		raise Http404

def get_paciente(request):
	if request.POST:
		paciente = get_object_or_404(Paciente, curp=request.POST['curpPaciente'])
		response = JsonResponse({'nombre': paciente.nombre, 'apellidoP': paciente.apellidoP, 'apellidoM': paciente.apellidoM,
								'edad': paciente.edad, 'genero': paciente.genero, 'nacimiento':paciente.fechanacimiento,
								'telcasa': paciente.telefonocasa, 'telcelular': paciente.telefonocelular, 'localidad': paciente.localidad,
								'idEstado': paciente.estadoprocedente.id, 'idMunicipio': paciente.municipio.id, 'idReferidopor': paciente.referidopor.id,
								'idEscolaridad': paciente.escolaridad.id, 'idOcupacion': paciente.ocupacion.id, 'calle': paciente.calle,
								'entrecalles': paciente.entrecalles, 'colonia': paciente.colonia, 'numerocasa': paciente.numerocasa,
								'codigopostal': paciente.codigopostal})
		return HttpResponse(response.content)
	else:
		raise Http404

def addEstudioSocioeconomico(request):
	if request.POST:
		try:
			with transaction.atomic():
				mensaje    = "Error al crear los estudios socio economicos"
				
				paciente   = Paciente.objects.get(curp=request.POST['curp'])
				expediente = Expediente.objects.get(paciente__id=paciente.id, is_active=True)
				
				estuidoTemp = EstudioSocioE1.objects.filter(expediente__id=expediente.id, fechaestudio=date.today())
				if estuidoTemp:
					mensaje = "Ya cuenta con un estudio socioeconomico el dia de hoy"
					response = JsonResponse({'isOk' : mensaje})
					return HttpResponse(response.content)				

				estructuraFamiliar = request.POST.getlist('EstructuraF[]')

				ingresos      = request.POST.getlist('ingresos[]')
				egresos       = request.POST.getlist('egresos[]')
				serviciosV    = request.POST.getlist('servicios[]')
				componentesV  = request.POST.getlist('componentes[]')
				construccionV = request.POST.getlist('construccion[]')
				tenenciasV    = request.POST.getlist('tenencias[]')
				barrerasIV    = request.POST.getlist('barrerasI[]')
				barrerasEV    = request.POST.getlist('barrerasE[]')

				u = User.objects.get(username=request.user)
				
				estudio1 = EstudioSocioE1.objects.create(
					edad                   = paciente.edad,
					estadocivil            = request.POST['estadoCivil'],
					consultorio            = CONSULTORIO,#request.POST['consultorio'],
					nombreentevistado      = request.POST['nombreEntrevistado'],
					apellidosentevistado   = request.POST['apellidoEntrevistado'],
					calle                  = paciente.calle,
					entrecalles            = paciente.entrecalles,
					colonia                = paciente.colonia,
					numerocasa             = paciente.numerocasa,
					codigopostal           = paciente.codigopostal,
					clasificacion_id       = request.POST['clasifacionEconomica'],
					ocupacion_id           = paciente.ocupacion.id,
					escolaridad_id         = paciente.escolaridad.id,
					servicio_id            = 1,#request.POST['servicio'],
					motivoestudio_id       = request.POST['motivoEstudio'],
					expediente_id          = expediente.id,
					usuariocreacion_id     = u.perfil_usuario.id,#request.POST['usuario'],
					motivoclasificacion    = request.POST['justificacionClasf'],
					parentescoentrevistado = request.POST['parentescoEntrevistado'],
					)

				for i in estructuraFamiliar:
					estructura = json.loads(i)
					EstructuraFamiliaESE1.objects.create(
						nombrefamiliar    = estructura['nombreF'],
						apellidosfamiliar = estructura['apellidosF'],
						parentesco        = estructura['parentescoF'],
						estadocivil       = estructura['estadoCivilF'],
						estudiose_id      = estudio1.id,
						ocupacion_id      = estructura['ocupacionF'],
						escolaridad_id    = estructura['escolaridadF'],
						edad              = estructura['edadF'],
						)
				print "estudio 1 y estrcutura"
				estudio2 = EstudioSocioE2.objects.create(
					deficit               = request.POST['deficit'],
					excedente             = request.POST['excedente'],
					datosignificativo     = request.POST['datosSignificativos'],
					diagnosticoplansocial = request.POST['diagnosticoPlanS'],
					cantidadbanios        = request.POST['cantidadBanios'],
					cantidadrecamaras     = request.POST['cantidadRecamaras'],
					estudiose_id          = estudio1.id,
					#usuariocreacion_id   = 1,
					vivienda_id           = request.POST['tipoVivienda']
					)

				for i in ingresos:
					ingreso = json.loads(i)
					EstudioSocioE2IngresosEgresos.objects.create(ingreso_egreso_id=ingreso['id'], estudio_id=estudio2.id, monto=ingreso['valor'])
				for i in egresos:
					egreso = json.loads(i)
					EstudioSocioE2IngresosEgresos.objects.create(ingreso_egreso_id=egreso['id'], estudio_id=estudio2.id, monto=egreso['valor'])
				for i in serviciosV:
					estudio2.serviciovivienda.add(i)
				for i in componentesV:
					estudio2.componentevivienda.add(i)
				for i in construccionV:
					estudio2.construccionvivienda.add(i)
				for i in tenenciasV:
					estudio2.tenenciavivienda.add(i)
				for i in barrerasIV:
					estudio2.barreravivienda.add(i)
				for i in barrerasEV:
					estudio2.barreravivienda.add(i)

				mensaje = "ok"

		except ValueError as e:
			logger.error(str(e))
			mensaje = "Valor no valido, revisar los valores que se ingresan."
		except:
			logger.error(sys.exc_info()[0])
			mensaje = "Error al crear los estudios socio economicos."

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

				paciente   = Paciente.objects.get(curp=request.POST['curp'])
				expediente = Expediente.objects.get(paciente__id=paciente.id, is_active=True)
				hojaPrev   = HojaPrevaloracion.objects.get(expediente__id=expediente.id, fechacreacion=date.today())
				u          = User.objects.get(username=request.user)
				
				servicios = request.POST.getlist('servicios[]')
				programas = request.POST.getlist('programas[]')
				
				hojaPrev.diagnosticonosologico2 = request.POST['diagnosticoNosologicoBreve']
				hojaPrev.psicologia             = request.POST['psicologia']
				hojaPrev.psicologo_id           = u.perfil_usuario.id
				hojaPrev.save()
				
				#tmpVarS = expediente.servicios.filter(servicio__in=[s for s in SERVICIOS_EXCLUIDOS_MEDICO])
				#tmpVarP = expediente.programas.filter(programa__in=[p for p in PROGRAMAS_EXCLUIDOS_MEDICO])
				tmpVarS = ServicioExpediente.objects.filter(expediente__id=expediente.id).filter(servicio__servicio__in=[s for s in SERVICIOS_EXCLUIDOS_MEDICO])
				tmpVarP = ProgramaExpediente.objects.filter(expediente__id=expediente.id).filter(programa__programa__in=[p for p in PROGRAMAS_EXCLUIDOS_MEDICO])
				tmpVarS.delete()
				tmpVarP.delete()
				
				for servicio in servicios:
					ServicioExpediente.objects.create(
						expediente_id        = expediente.id,
						servicio_id          = servicio,
						hojaPrevaloracion_id = hojaPrev.id,
						fechaBaja            = date.today()
						)
				for programa in programas:
					ProgramaExpediente.objects.create(
						expediente_id        = expediente.id,
						programa_id          = programa,
						hojaPrevaloracion_id = hojaPrev.id,
						fechaBaja            = date.today()
						)
				try:
					hojaFront                       = HojaFrontal.objects.get(expediente__id=expediente.id, fechacreacion=date.today(), usuario__id=hojaPrev.psicologo.id)
					hojaFront.diagnosticonosologico = request.POST['psicologia']
					hojaFront.save()
				except:
					HojaFrontal.objects.create(
						edad                  = paciente.edad,
						diagnosticonosologico = request.POST['psicologia'],
						usuario_id            = u.perfil_usuario.id,
						expediente_id         = expediente.id
					)

				mensaje = "ok"

		except ValueError as e:
			logger.error(str(e))
			mensaje = "Valor no valido, revisar los valores que se ingresan."
		except:
			logger.error(sys.exc_info()[0])
			mensaje = "Error al actualizar la hoja de prevaloracion."

		response = JsonResponse({'isOk' : mensaje})
		return HttpResponse(response.content)
	else:
		raise Http404

#@csrf_exempt
def addHojaPrevaloracion(request):
	if request.POST:
		clave = RepresentsInt(request.POST['clave'])
		if clave > 0:
			try:
				with transaction.atomic():
					servicios = request.POST.getlist('servicios[]')
					programas = request.POST.getlist('programas[]')
					
					paciente          = Paciente.objects.get(curp=request.POST['curp'])
					hojaPrevaloracion = HojaPrevaloracion.objects.get(id=request.POST['clave'])
					expediente        = Expediente.objects.get(id=hojaPrevaloracion.expediente.id)
					hojaFrontal       = HojaFrontal.objects.get(expediente__id=expediente.id, fechacreacion=date.today(), usuario__id=hojaPrevaloracion.doctor.id)
					
					if len(servicios) > 0:
						paciente.correspondio = True
						paciente.save()
					else:
						paciente.correspondio = False
						paciente.save()
					correspondio = paciente.correspondio

					hojaPrevaloracion.motivoconsulta        = request.POST['motivoConsulta']
					hojaPrevaloracion.diagnosticonosologico = request.POST['diagnosticoNosologico']
					hojaPrevaloracion.canalizacion          = request.POST['canalizacion']
					hojaPrevaloracion.edad                  = paciente.edad
					hojaPrevaloracion.ocupacion_id          = paciente.ocupacion.id
					hojaPrevaloracion.referidopor_id        = paciente.referidopor.id
					hojaPrevaloracion.escolaridad_id        = paciente.escolaridad.id
					hojaPrevaloracion.save()
					
					tmpVarS = ServicioExpediente.objects.filter(expediente__id=expediente.id).exclude(servicio__servicio__in=[s for s in SERVICIOS_EXCLUIDOS_MEDICO])
					tmpVarP = ProgramaExpediente.objects.filter(expediente__id=expediente.id).exclude(programa__programa__in=[p for p in PROGRAMAS_EXCLUIDOS_MEDICO])
					tmpVarS.delete()
					tmpVarP.delete()

					for servicio in servicios:
						ServicioExpediente.objects.create(
							expediente_id        = expediente.id,
							servicio_id          = servicio,
							hojaPrevaloracion_id = hojaPrevaloracion.id,
							fechaBaja            = date.today()
						)

					for programa in programas:
						ProgramaExpediente.objects.create(
							expediente_id        = expediente.id,
							programa_id          = programa,
							hojaPrevaloracion_id = hojaPrevaloracion.id,
							fechaBaja            = date.today()
						)
					
					hojaFrontal.diagnosticonosologico = request.POST['diagnosticoNosologico']
					hojaFrontal.save()

					mensaje = "ok"
			except ValueError as e:
				logger.error(str(e))
				mensaje = "Valor no valido, revisar los valores que se ingresan."
			except:
				logger.error(sys.exc_info()[0])
				mensaje = "Error al crear la hoja de prevaloracion."
		else:
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
							paciente_id     = paciente.id,
							fechaalta       = "2015-03-30",
							)
						
						u = User.objects.get(username=request.user)
						
						hojaPreValoracion = HojaPrevaloracion.objects.create(
							motivoconsulta        = request.POST['motivoConsulta'],
							diagnosticonosologico = request.POST['diagnosticoNosologico'],
							canalizacion          = request.POST['canalizacion'],
							edad                  = paciente.edad,
							ocupacion_id          = paciente.ocupacion.id,
							referidopor_id        = paciente.referidopor.id,
							escolaridad_id        = paciente.escolaridad.id,
							doctor_id             = u.perfil_usuario.id,
							psicologo_id          = 1,
							expediente_id         = expediente.id
							)
						
						for servicio in servicios:
							ServicioExpediente.objects.create(
								expediente_id        = expediente.id,
								servicio_id          = servicio,
								hojaPrevaloracion_id = hojaPreValoracion.id,
								fechaBaja            = date.today()
								)
						for programa in programas:
							ProgramaExpediente.objects.create(
								expediente_id        = expediente.id,
								programa_id          = programa,
								hojaPrevaloracion_id = hojaPreValoracion.id,
								fechaBaja            = date.today()
								)

						hojaFrontal = HojaFrontal.objects.create(
							edad                  = paciente.edad,
							diagnosticonosologico = request.POST['diagnosticoNosologico'],
							usuario_id            = u.perfil_usuario.id,
							expediente_id         = expediente.id
							)
						"""
						if paciente.edad > 18:
							print request.POST['nombreResponsable']       #= ""
							print request.POST['apellidosResponsable']    #= ""
							print request.POST['edadResponsable']         #= ""
							print request.POST['parentescoResponsable']   #= ""
							print request.POST['domicilioResponsable']    #= ""
							print request.POST['coloniaResponsable']      #= ""
							print request.POST['codigopostalResponsable'] #= ""
						"""
						cartaConsentimiento = CartaConsetimiento.objects.create(
							edad                    = paciente.edad,
							calle                   = paciente.calle,
							entrecalles             = paciente.entrecalles,
							numerocasa              = paciente.numerocasa,
							colonia                 = paciente.colonia,
							codigopostal            = paciente.codigopostal,
							estadoprocedente_id     = paciente.estadoprocedente.id,
							municipio_id            = paciente.municipio.id,
							nombreresponsable       = request.POST['nombreResponsable'],
							apellidosresponsable    = request.POST['apellidosResponsable'],
							edadresponsable         = request.POST['edadResponsable'],
							generoresponsable       = request.POST['generoResponsable'],
							parentescoresponsable   = request.POST['parentescoResponsable'],
							domicilioresponsable    = request.POST['domicilioResponsable'],
							coloniaresponsable      = request.POST['coloniaResponsable'],
							codigopostalresponsable = request.POST['codigopostalResponsable'],
							telefonoresponsable     = request.POST['telefonoResponsable'],
							doctor_id               = u.perfil_usuario.id,
							expediente_id           = expediente.id
							)

						correspondio = True
					else:
						paciente.correspondio = False
						paciente.save()

					mensaje = "ok"
			except ValueError as e:
				logger.error(str(e))
				mensaje = "Valor no valido, revisar los valores que se ingresan."
			except:
				logger.error(sys.exc_info()[0])
				mensaje = "Error al crear la hoja de prevaloracion."

		response = JsonResponse({'curp' : request.POST['curp'], 'correspondio' : correspondio,
								'isOk' : mensaje})
		return HttpResponse(response.content)
	else:
		raise Http404

def addDataEnfermeria(request):
	if request.POST:
		clave = RepresentsInt(request.POST['clave'])
		if clave > 0:
			try:
				mensaje = "Error al actualizar datos de enfermeria."

				paciente       = Paciente.objects.get(curp=request.POST['curp'])
				dataEnfermeria = PacienteDataEnfermeria.objects.get(id=request.POST['clave'])
				
				dataEnfermeria.peso    = request.POST['peso']
				dataEnfermeria.talla   = request.POST['talla']
				dataEnfermeria.f_c     = request.POST['fc']
				dataEnfermeria.t_a     = request.POST['ta']
				dataEnfermeria.glucosa = request.POST['gluc']
				dataEnfermeria.cintura = request.POST['cintura']

				dataEnfermeria.save()
				
				mensaje = "ok"
			except ValueError as e:
				logger.error(str(e))
				mensaje = "Valor no valido, revisar los valores que se ingresan."
			except:
				logger.error(sys.exc_info()[0])
				mensaje = "Error al actualizar datos de enfermeria."
		else:
			try:
				mensaje = "Error al guardar datos de enfermeria."

				paciente = Paciente.objects.get(curp=request.POST['curp'])
				u        = User.objects.get(username=request.user)
				
				dataEnfermeriaPaciente = PacienteDataEnfermeria.objects.create(
					paciente_id         = paciente.id,
					edad                = paciente.edad,
					peso                = request.POST['peso'],
					talla               = request.POST['talla'],
					f_c                 = request.POST['fc'],
					t_a                 = request.POST['ta'],
					glucosa             = request.POST['gluc'],
					cintura             = request.POST['cintura'],
					enfermera_id        = u.perfil_usuario.id,
					mensaje_informativo = request.POST['mensajeInformativo'],
					)

				mensaje = "ok"
			except ValueError as e:
				logger.error(str(e))
				mensaje = "Valor no valido, revisar los valores que se ingresan."
			except:
				logger.error(sys.exc_info()[0])
				mensaje = "Error al guardar datos de enfermeria."

		response = JsonResponse({'isOk' : mensaje})
		return HttpResponse(response.content)
	else:
		raise Http404

def agregar_paciente(request):
	if request.is_ajax():
		#paciente = Paciente.objects().filter(curp=request.POST['curp'])
		try:
			mensaje   = "Error al crear el parciente"
			municipio = "Generico"
			u         = User.objects.get(username=request.user)
			#municipio = Municipio.objects.get(descripcion=request.POST['localidad'])
			#estado = Estado.objects.get(descripcion=request.POST['estado'])
			pacienteTemp = Paciente.objects.create(
				nombre              = request.POST['nombre'],
				apellidoP           = request.POST['apellidoP'],
				apellidoM           = request.POST['apellidoM'],
				curp                = request.POST['curp'],
				edad                = request.POST['edad'],
				genero              = request.POST['genero'],
				fechanacimiento     = request.POST['fechaN'],
				telefonocasa        = request.POST['telCasa'],
				telefonocelular     = request.POST['celular'],
				estadoprocedente_id = request.POST['estado'],
				municipio_id        = request.POST['municipio'],
				localidad           = request.POST['localidad'],
				calle               = request.POST['calle'],
				entrecalles         = request.POST['entreCalles'],
				colonia             = request.POST['colonia'],
				numerocasa          = request.POST['numCasa'],
				codigopostal        = request.POST['codigoPostal'],
				ocupacion_id        = request.POST['ocupacion'],
				referidopor_id      = request.POST['referidopor'],
				escolaridad_id      = request.POST['escolaridad'],
				#correspondio       = request.POST[''],
				usuariocreacion_id  = u.perfil_usuario.id,
				)
			municipio = pacienteTemp.municipio.descripcion
			mensaje = "ok"
		except IntegrityError as e:
			logger.error(str(e))
			mensaje = "La curp del paciente ya existe en la base de datos."
		except ValueError as e:
			logger.error(str(e))
			mensaje = "Valor no valido, revisar los valores que se ingresan."
		except:
			logger.error(sys.exc_info()[0])
			mensaje = "Error al crear el parciente."
		
		response = JsonResponse({'nombre' : request.POST['nombre'],'apellidoP' : request.POST['apellidoP'],
		 'curp' : request.POST['curp'], 'correspondio' : 'None', 'municipio' : municipio, 'isOk' : mensaje})
		
		return HttpResponse(response.content)
	else:
		raise Http404

def my_custom_page_not_found_view(request):
	render('404.html')

def getUserGroupByRequest(request):
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
					try:
						request.user.groups.get(name='Imprimir')
						grupo = "imprimir"
					except Group.DoesNotExist:
						try:
							request.user.groups.get(name='Enfermeria')
							grupo = "enfermeria"
						except Group.DoesNotExist:
							grupo = ""
	return grupo

def RepresentsInt(valor):
    try: 
        value = int(valor)
        return value
    except ValueError:
        return -1