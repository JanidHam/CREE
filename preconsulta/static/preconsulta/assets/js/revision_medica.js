//Variables globales
try {
var socket = io.connect("http://localhost:3000");
} catch(err) {
  socket = null;
  //Ya se maneja el error si no esta corriendo el servidor de nodeJS, falta mostrar un mensaje
  //de error para informar que no se guardaran los cambios
}
var $sendRevision = $('#RevisionPaciente');

var $form    = $('#form'),
	$canalizacion               = $('#canalizacion'),
	$motivoConsulta             = $('#motivoConsulta'),
	$diagnosticoNosologico      = $('#diagnosticoNosologico');



//Funciones
function sendDataRevision() {
	var serviciostemp = getCheckedServicios();
	var programastemp = getCheckedProgramas();

	var datosRevision = {
		canalizacion : $canalizacion.val(),
		motivoConsulta : $motivoConsulta.val(),
		diagnosticoNosologico : $diagnosticoNosologico.val(),		
		servicios : serviciostemp,
		programas : programastemp,
		curp : CURP,
	}
	
	socket.emit('addHojaPrevaloracion', datosRevision);
	//window.location.replace("http://localhost:8000/preconsulta/");
	return false;
}

function getCheckedServicios() {
    var servicios = [];    
    $('input:checkbox[name=servicios]:checked').each(function() {
        servicios.push($(this).val());        
    });

    return servicios;
}

function getCheckedProgramas() {
    var programas = [];
    $('input:checkbox[name=programas]:checked').each(function() {
        programas.push($(this).val());
    });

    return programas;
}

function checkIsDataIsCorrect(data) {
	var data = JSON.parse(data);
	if (data.isOk == "ok") {
		socket.emit('dataIsSaveSucces_revision_medica', data);
		window.location.replace("http://localhost:8000/preconsulta/");
	} else {
		alert(data.isOk);
	}
}

//Eventos

$sendRevision.click( sendDataRevision )

socket.on('addHojaPrevaloracion_Respuesta', checkIsDataIsCorrect );