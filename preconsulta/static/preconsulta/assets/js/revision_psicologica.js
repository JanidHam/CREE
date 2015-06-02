$(document).on('ready', main_configAjax);

function main_configAjax() {
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if(settings.type == "POST"){
        xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
      }
    }
  });
}
//Variables globales
/*try {
var socket = io.connect("http://localhost:3000");
} catch(err) {
  socket = null;
  //Ya se maneja el error si no esta corriendo el servidor de nodeJS, falta mostrar un mensaje
  //de error para informar que no se guardaran los cambios
}
*/
var $sendRevision = $('#RevisionPaciente');

var $form    = $('#form'),
	$psicologia = $('#psicologia'),
	$diagnosticoNosologicoBreve = $('#diagnosticoNosologicoBreve');

//Funciones
function sendDataRevision() {
	$sendRevision.button('loading');
	var serviciostemp = getCheckedServicios();
	var programastemp = getCheckedProgramas();
	var datosRevision = {
		psicologia : $psicologia.val().toUpperCase(),
		diagnosticoNosologicoBreve : $diagnosticoNosologicoBreve.val().toUpperCase(),
		'servicios[]' : serviciostemp,
		'programas[]' : programastemp,
		curp : CURP,
		//usuario : 2,
	}
	$.post('/preconsulta/agregar-hoja-prevaloracion-psicologia/', datosRevision , checkIsDataIsCorrect);
	
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
	//console.log(data);
	if (data.isOk == "ok") {
		window.location.href = "/preconsulta/";
	} else {
		alert(data.isOk);
		$sendRevision.button('reset');
	}
}

//Eventos

$sendRevision.click( sendDataRevision )

//socket.on('addPsicologiaHojaPrevaloracion_respuesta', checkIsDataIsCorrect );