$(document).on('ready', main_discusiones);

function main_discusiones() {
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if(settings.type == "POST"){
        xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
      }
    }
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
var $sendRevision = $('#RevisionPaciente');

var $form    = $('#form'),
	$canalizacion               = $('#canalizacion'),
	$motivoConsulta             = $('#motivoConsulta'),
	$diagnosticoNosologico      = $('#diagnosticoNosologico');



//Funciones
function sendDataRevision() {
	$sendRevision.button('loading');
	var serviciostemp = getCheckedServicios();
	var programastemp = getCheckedProgramas();

	var datosRevision = {
		canalizacion : $canalizacion.val().toUpperCase(),
		motivoConsulta : $motivoConsulta.val().toUpperCase(),
		diagnosticoNosologico : $diagnosticoNosologico.val().toUpperCase(),		
		'servicios[]' : serviciostemp,
		'programas[]' : programastemp,
		curp : CURP,
	}
	console.log(datosRevision);
	$.post('/preconsulta/agregar-hoja-prevaloracion/', datosRevision , checkIsDataIsCorrect);
	//socket.emit('addHojaPrevaloracion', datosRevision);
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
		try {
			socket.emit('dataIsSaveSucces_revision_medica', data);
		} catch(err) {
			
		}
		window.location.replace("http://localhost:8000/preconsulta/");
	} else {
		alert(data.isOk);
		$sendRevision.button('reset');
	}
}

//Eventos

$sendRevision.click( sendDataRevision )

socket.on('addHojaPrevaloracion_Respuesta', checkIsDataIsCorrect );