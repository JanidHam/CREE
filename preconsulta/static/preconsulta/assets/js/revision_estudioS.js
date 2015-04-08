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

var $form    = $('#form'),
	$deficit              = $('#deficit'),
	$excedente            = $('#excedente'),
	$estadoCivil          = $('#estadoCivil'),
	//$consultorio          = $('#consultorio'),
	$tipoVivienda         = $('#tipoVivienda'),
	$motivoEstudio        = $('#motivoEstudio'),
	$nombreEntrevistado   = $('#nombreEntrevistado'),
	$apellidoEntrevistado = $('#apellidoEntrevistado');


//Funciones

function addEstructuraFamiliar() {

	$('#form-estructura').clone().prependTo('#estructura-familiar');	

    //$estructuraFNombre = $('input:text[name=nombreFamiliar]');

    //$estructuraFNombre[$estructuraFNombre.length - 1].value = "";
	return false;
}

function sendDataRevision() {

	var datosRevision = {
		//consultorio : $consultorio.val(),
		nombreEntrevistado : $nombreEntrevistado.val(),
		apellidoEntrevistado : $apellidoEntrevistado.val(),
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
		curp : CURP,
        EstructuraF : getEstructuraFamiliar(),
	}

	try {
		socket.emit('addEstudioSEconomico', datosRevision);
	} catch(err) {
	  alert("No se encuentra disponible el servicio.");
	}
	
	
	return false;
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
            estructura.push({'nombreF': $estructuraFNombre[i].value, 'apellidosF': $estructuraFApellidos[i].value,
                             'parentescoF': $estructuraFParentesco[i].value, 'edadF': $estructuraFEdad[i].value,
                             'estadoCivilF': $estructuraFEstadoCivil[i].value,'ocupacionF': $estructuraFOcupacion[i].value,
                             'escolaridadF': $estructuraFEscolaridad[i].value});
        }
    }
    console.log(estructura);
    return estructura;
}

function getIngresos() {
    var ingresos = [];    
    $ingresos = $('input:text[name=ingresos]');

    for (var i = 0; i < $ingresos.length; i++) {
    	if ($ingresos[i].value !== "") 
    		ingresos.push({'id': $ingresos[i].attributes.item(2).value, 'valor' : $ingresos[i].value });    	
    };
    //console.log(ingresos);
    return ingresos;
}

function getEgresos() {
    var egresos = [];    
    $egresos = $('input:text[name=egresos]');

    for (var i = 0; i < $egresos.length; i++) {
    	if ($egresos[i].value !== "") 
    		egresos.push({'id': $egresos[i].attributes.item(2).value, 'valor' : $egresos[i].value });    	
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

//Eventos

$sendRevision.click( sendDataRevision )

$addEstructuraF.click( addEstructuraFamiliar )

socket.on('addHojaPrevaloracion_Respuesta', checkIsDataIsCorrect );