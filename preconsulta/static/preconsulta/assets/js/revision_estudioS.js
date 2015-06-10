$(document).on('ready', main_configAjax);

function main_configAjax() {
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
	var socket = io.connect("http://" + urlServerNodeJS);
} catch(err) {
  socket = null;
  //Ya se maneja el error si no esta corriendo el servidor de nodeJS, falta mostrar un mensaje
  //de error para informar que no se guardaran los cambios
}

var $sendRevision   = $('#RevisionPaciente');
var $addEstructuraF = $('#addEstructuraFamiliar');


    var $deficit                = $('#deficit'),
    $excedente                  = $('#excedente'),
    $estadoCivil                = $('#estadoCivil'),
    //$consultorio              = $('#consultorio'),
    $tipoVivienda               = $('#tipoVivienda'),
    $claveEstudio               = $('#claveEstudio'),
    $motivoEstudio              = $('#motivoEstudio'),
    $cantidadBanios             = $('#cantidadBanios'),
    $clasificacionE             = $('#clasificacionE'),
    $seguridadSocial            = $('#seguridadSocial'),
    $diagnosticoPlanS           = $('#diagnosticoPlanS'),
    $cantidadRecamaras          = $('#cantidadRecamaras'),
    $nombreEntrevistado         = $('#nombreEntrevistado'),
    $textJustificacionC         = $('#textJustificacionC'),
    $datosSignificativos        = $('#datosSignificativos'),
    $apellidoEntrevistado       = $('#apellidoEntrevistado'),
    $parentescoEntrevistado     = $('#parentescoEntrevistado'),
    $egresos                    = $('input:text[name=egresos]'),
    $ingresos                   = $('input:text[name=ingresos]'),
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
    if (validEstudio()) {
        $sendRevision.button('loading');
        //getDeficitExcedente();
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
            parentescoEntrevistado : $parentescoEntrevistado.val(),
            seguridadSocial: $seguridadSocial.val(),
            claveEstudio: $claveEstudio.val(),
    	}
        //$.post('guardar-encuesta-contestada/', { 'fecha': idinput.val(), 'tasks[]': tasks, 'tasksP[]': tasksPreguntas }, actualizar_encuestas);
        $.post('/preconsulta/agregar-estudio-socio-economico/', datosRevision , checkIsDataIsCorrect);
	}
	
	return false;
}

function validEstudio() {
    if ($nombreEntrevistado.val() !== '') {
        if ($apellidoEntrevistado.val() !== '') {
            if ($cantidadBanios.val() !== '') {
                if ($cantidadRecamaras.val() !== '') {
                    return true;
                } else {
                    alert("La 'Cantidad de Recamaras' no puede ir vacia.");
                } 
            } else {
                    alert("La 'Cantidad de Baños' no puede ir vacia.");
            }
        } else {
            alert("El 'Apellido Entrevistado' no puede ir vacio.");
        }
    } else {
        alert("El 'Nombre Entrevistado' no puede ir vacio.");
    }
    return false;
}

function getTotalIngresos() {
    var tempTotal = 0
    for (var i = 0; i < $ingresos.length; i++) {
        if ($ingresos[i].value !== "")
            tempTotal += parseInt($ingresos[i].value)
        else
            console.log('no es numero')
    }
    $excedente.val(tempTotal)
    //console.log($excedente.val())
}

function getTotalEgresos() {
    var tempTotal = 0
    for (var i = 0; i < $egresos.length; i++) {
        if ($egresos[i].value !== "")
            tempTotal += parseInt($egresos[i].value)
        else
            console.log('no es numero')
    }
    $deficit.val(tempTotal)
    //console.log($deficit.val())
}

function getDeficitExcedente() {

    /*$ingresos = $('input:text[name=ingresos]');
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
    */
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
    		ingresos.push(JSON.stringify({'id' : $ingresos[i].attributes['id'].value, 'valor' : $ingresos[i].value }));
    };

    return ingresos;
}

function getEgresos() {
    var egresos = [];    
    $egresos = $('input:text[name=egresos]');

    for (var i = 0; i < $egresos.length; i++) {
    	if ($egresos[i].value !== "") 
    		egresos.push(JSON.stringify({'id': $egresos[i].attributes['id'].value, 'valor' : $egresos[i].value }));
    };

    return egresos;
}

function getComponentesVivienda() {
    var componentes = [];    
    
    $('input:checkbox[name=componentesVivienda]:checked').each(function() {
        componentes.push($(this).val());        
    });

    return componentes;
}

function getServiciosVivienda() {
    var servicios = [];    
    
    $('input:checkbox[name=serviciosVivienda]:checked').each(function() {
        servicios.push($(this).val());        
    });

    return servicios;
}

function getTenenciasVivienda() {
    var tenencias = [];    
    
    $('input:checkbox[name=tenenciasVivienda]:checked').each(function() {
        tenencias.push($(this).val());        
    });

    return tenencias;
}

function getConstruccionVivienda() {
    var construccion = [];    
    
    $('input:checkbox[name=construccionVivienda]:checked').each(function() {
        construccion.push($(this).val());        
    });

    return construccion;
}

function getBarrerasInternasVivienda() {
    var barrerasI = [];    
    
    $('input:checkbox[name=barrerasInternasVivienda]:checked').each(function() {
        barrerasI.push($(this).val());        
    });

    return barrerasI;
}

function getBarrerasExternasVivienda() {
    var barrerasE = [];    
    
    $('input:checkbox[name=barrerasExternasVivienda]:checked').each(function() {
        barrerasE.push($(this).val());        
    });

    return barrerasE;
}

function checkIsDataIsCorrect(data) {
    var data = JSON.parse(data);
    console.log(data);
    if (data.isOk == "ok") {  
        window.location.href = "/preconsulta/";
    } else {
        alert(data.isOk);
        $sendRevision.button('reset');
    }    
}

//Eventos

$sendRevision.click( sendDataRevision )

$addEstructuraF.click( addEstructuraFamiliar )

$ingresos.focusout( getTotalIngresos )

$egresos.focusout( getTotalEgresos )