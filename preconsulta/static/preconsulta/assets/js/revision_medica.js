//Variables globales
var socket = io.connect("http://localhost:3000");

var $sendRevision = $('#RevisionPaciente');

var $form    = $('#form'),
	$canalizacion               = $('#canalizacion'),
	$motivoConsulta             = $('#motivoConsulta'),
	$diagnosticoNosologico      = $('#diagnosticoNosologico'),
	$diagnosticoNosologicoBreve = $('#diagnosticoNosologicoBreve');



//Funciones
function sendDataRevision() {
	var serviciostemp = getCheckedServicios();
	var programastemp = getCheckedProgramas();

	var datosRevision = {
		canalizacion : $canalizacion.val(),
		motivoConsulta : $motivoConsulta.val(),
		diagnosticoNosologico : $diagnosticoNosologico.val(),
		diagnosticoNosologicoBreve : $diagnosticoNosologicoBreve.val(),
		servicios : serviciostemp,
		programas : programastemp,
		curp : CURP,
	}
	
	socket.emit('addHojaPrevaloracion', datosRevision);
	window.location.replace("http://localhost:8000/preconsulta/");
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

//Eventos

$sendRevision.click( sendDataRevision )