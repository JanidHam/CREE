$(document).on('ready', main_discusiones);

function main_discusiones() {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if(settings.type == "POST"){
                xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
            }
        }
    });
$('#clasificacionNueva').change(function() {
    
    show_hideJusticacion();
        if($(this).is(":checked")) {
            $clasificacionE.removeAttr('disabled');
            return false;
        }
        $clasificacionE.attr('disabled', 'true');
    });
}
//Variables globales
try {
	var socket = io.connect("http://localhost:3000");
} catch(err) {
  socket = null;
  //Ya se maneja el error si no esta corriendo el servidor de nodeJS, falta mostrar un mensaje
  //de error para informar que no se guardaran los cambios
}

var $sendRevision   = $('#RevisionPaciente');
var $addEstructuraF = $('#addEstructuraFamiliar');


var $deficit                    = $('#deficit'),
    $excedente                  = $('#excedente'),
    $estadoCivil                = $('#estadoCivil'),
    //$consultorio              = $('#consultorio'),
    $tipoVivienda               = $('#tipoVivienda'),
    $motivoEstudio              = $('#motivoEstudio'),
    $cantidadBanios             = $('#cantidadBanios'),
    $clasificacionE             = $('#clasificacionE'),
    $diagnosticoPlanS           = $('#diagnosticoPlanS'),
    $cantidadRecamaras          = $('#cantidadRecamaras'),
    $nombreEntrevistado         = $('#nombreEntrevistado'),
    $textJustificacionC         = $('#textJustificacionC'),
    $datosSignificativos        = $('#datosSignificativos'),
    $apellidoEntrevistado       = $('#apellidoEntrevistado'),
    $justificacionClasificacion = $('#justificacionClasificacion');


//Funciones

function addEstructuraFamiliar() {

	$('#form-estructura').clone().prependTo('#estructura-familiar');	

    //$estructuraFNombre = $('input:text[name=nombreFamiliar]');

    //$estructuraFNombre[$estructuraFNombre.length - 1].value = "";
	return false;
}

function show_hideJusticacion() {
    $justificacionClasificacion.slideToggle();
    return false;
}

function sendDataRevision() {
    $sendRevision.button('loading');
    getDeficitExcedente();
	var datosRevision = {
		//consultorio : $consultorio.val(),        
		nombreEntrevistado : $nombreEntrevistado.val().toUpperCase(),
		apellidoEntrevistado : $apellidoEntrevistado.val().toUpperCase(),
		motivoEstudio : $motivoEstudio.val(),
		estadoCivil : $estadoCivil.val(),
		deficit : $deficit.val(),
		excedente : $excedente.val(),
		tipoVivienda : $tipoVivienda.val(),
		ingresos : getIngresos(),
		egresos : getEgresos(),
		servicios : getServiciosVivienda(),
		construccion : getConstruccionVivienda(),
		tenencias : getTenenciasVivienda(),
		barrerasE : getBarrerasExternasVivienda(),
		barrerasI : getBarrerasInternasVivienda(),
        componentes : getComponentesVivienda(),
		curp : CURP,
        EstructuraF : getEstructuraFamiliar(),
        diagnosticoPlanS : $diagnosticoPlanS.val().toUpperCase(),
        datosSignificativos : $datosSignificativos.val().toUpperCase(),
        cantidadBanios: $cantidadBanios.val(),
        cantidadRecamaras: $cantidadRecamaras.val(),
        clasifacionEconomica: $clasificacionE.val(),
        justificacionClasf: $textJustificacionC.val().toUpperCase(),
	}
    //$.post('guardar-encuesta-contestada/', { 'fecha': idinput.val(), 'tasks[]': tasks, 'tasksP[]': tasksPreguntas }, actualizar_encuestas);
    $.post('/preconsulta/agregar-estudio-socio-economico/', datosRevision , checkIsDataIsCorrect);
	/*try {
		socket.emit('addEstudioSEconomico', datosRevision);
	} catch(err) {
	  alert("No se encuentra disponible el servicio.");
	}*/
	
	
	return false;
}

function getDeficitExcedente() {
    $ingresos = $('input:text[name=ingresos]');
    $egresos = $('input:text[name=egresos]');
    var Total = 0;
    for (var i = 0; i < $ingresos.length; i++) {
        if ($ingresos[i].value !== "")
            Total += parseInt($ingresos[i].value);
    };
    for (var i = 0; i < $egresos.length; i++) {
        if ($egresos[i].value !== "")
            Total -= parseInt($egresos[i].value)
    };
    if (Total >= 0)
        $excedente.val(Total);
    else
        $deficit.val(Total);
}

function getEstructuraFamiliar() {
    var estructura = [];
    $estructuraFNombre = $('input:text[name=nombreFamiliar]');
    $estructuraFApellidos = $('input:text[name=apellidosFamiliar]');
    $estructuraFParentesco = $('select[name=parentescoFamiliar]');
    $estructuraFEdad = $('input:text[name=edadFamiliar]');
    $estructuraFEstadoCivil = $('select[name=estadoCivilFamiliar]');
    $estructuraFOcupacion = $('select[name=ocupacionFamiliar]');
    $estructuraFEscolaridad = $('select[name=escolaridadFamiliar]');

    for (var i = 0; i < $estructuraFNombre.length; i++) {
        if ($estructuraFNombre[i].value !== "") {
            estructura.push(JSON.stringify({'nombreF': $estructuraFNombre[i].value.toUpperCase(), 'apellidosF': $estructuraFApellidos[i].value.toUpperCase(),
                             'parentescoF': $estructuraFParentesco[i].value, 'edadF': $estructuraFEdad[i].value,
                             'estadoCivilF': $estructuraFEstadoCivil[i].value,'ocupacionF': $estructuraFOcupacion[i].value,
                             'escolaridadF': $estructuraFEscolaridad[i].value }));
        }
    }
    //console.log(estructura);
    return estructura;
}

function getIngresos() {
    var ingresos = [];    
    $ingresos = $('input:text[name=ingresos]');

    for (var i = 0; i < $ingresos.length; i++) {
    	if ($ingresos[i].value !== "")
            //ingresos.push([$ingresos[i].attributes.item(2).value, $ingresos[i].value]);
            //ingresos.push($ingresos[i].attributes.item(2).value);
            //ingresos.push($ingresos[i].value);
    		ingresos.push(JSON.stringify({'id' : $ingresos[i].attributes.item(2).value, 'valor' : $ingresos[i].value }));
    };
    //console.log(ingresos);
    return ingresos;
}

function getEgresos() {
    var egresos = [];    
    $egresos = $('input:text[name=egresos]');

    for (var i = 0; i < $egresos.length; i++) {
    	if ($egresos[i].value !== "") 
    		egresos.push(JSON.stringify({'id': $egresos[i].attributes.item(2).value, 'valor' : $egresos[i].value }));
    };
    //console.log(egresos);
    return egresos;
}

function getComponentesVivienda() {
    var componentes = [];    
    
    $('input:checkbox[name=componentesVivienda]:checked').each(function() {
        componentes.push($(this).val());        
    });
	//console.log(componentes);
    return componentes;
}

function getServiciosVivienda() {
    var servicios = [];    
    
    $('input:checkbox[name=serviciosVivienda]:checked').each(function() {
        servicios.push($(this).val());        
    });
    //console.log(servicios);
    return servicios;
}

function getTenenciasVivienda() {
    var tenencias = [];    
    
    $('input:checkbox[name=tenenciasVivienda]:checked').each(function() {
        tenencias.push($(this).val());        
    });
    //console.log(tenencias);
    return tenencias;
}

function getConstruccionVivienda() {
    var construccion = [];    
    
    $('input:checkbox[name=construccionVivienda]:checked').each(function() {
        construccion.push($(this).val());        
    });
    //console.log(construccion);
    return construccion;
}

function getBarrerasInternasVivienda() {
    var barrerasI = [];    
    
    $('input:checkbox[name=barrerasInternasVivienda]:checked').each(function() {
        barrerasI.push($(this).val());        
    });
    //console.log(barrerasI);
    return barrerasI;
}

function getBarrerasExternasVivienda() {
    var barrerasE = [];    
    
    $('input:checkbox[name=barrerasExternasVivienda]:checked').each(function() {
        barrerasE.push($(this).val());        
    });
    //console.log(barrerasE);
    return barrerasE;
}

function checkIsDataIsCorrect(data) {
    var data = JSON.parse(data);
    console.log(data);
    if (data.isOk == "ok") {        
        window.location.replace("http://localhost:8000/preconsulta/");
    } else {
        alert(data.isOk);
        $sendRevision.button('reset');
    }    
}

//Eventos

$sendRevision.click( sendDataRevision )

$addEstructuraF.click( addEstructuraFamiliar )

//socket.on('addEstudioSEconomico_respuesta', checkIsDataIsCorrect );