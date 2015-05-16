$(document).on('ready', main_configAjax);

function main_configAjax() {
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if(settings.type == "POST"){
        xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
      }
    }
  });
  $sendRevision.button('loading');
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
var $sendRevision = $('#sendDataEnfermeriaPaciente');

var $printAndSetData = $('#printAndSetData');

var $form    = $('#form'),
	$pesoPaciente = $('#pesoPaciente'),
	$tallaPaciente = $('#tallaPaciente'),
	$fcPaciente = $('#fcPaciente'),
	$taPaciente = $('#taPaciente'),
	$glucosaPaciente = $('#glucosaPaciente'),
	$cinturaPaciente = $('#cinturaPaciente'),
	$printPeso = $('#printPeso'),
	$printTalla = $('#printTalla'),
	$printFC = $('#printFC'),
	$printTA = $('#printTA'),
	$printGlucosa = $('#printGlucosa'),
	$printCintura = $('#printCintura'),
	$printMedico = $('#printMedico'),
	$printMensaje = $('#printMensaje');

//Funciones
function sendDataRevision() {
	$sendRevision.button('loading');
	var datosRevision = {
		peso : $pesoPaciente.val(),
		talla : $tallaPaciente.val(),
		fc : $fcPaciente.val(),
		ta : $taPaciente.val(),
		gluc : $glucosaPaciente.val(),
		cintura : $cinturaPaciente.val(),
		curp : CURP,
	}
	$.post('/preconsulta/agregar-enfermeria/', datosRevision , checkIsDataIsCorrect);
	
	return false;
}

function checkIsDataIsCorrect(data) {
	var data = JSON.parse(data);
	//console.log(data);
	if (data.isOk == "ok") {
		//window.location.replace("http://localhost:8000/preconsulta/");
	} else {
		alert(data.isOk);
		$sendRevision.button('reset');
	}
}

function setDataToPrint(){
	$printPeso.append("  " + $pesoPaciente.val());
	$printTalla.append("  " + $tallaPaciente.val());
	$printFC.append("  " + $fcPaciente.val());
	$printTA.append("  " + $taPaciente.val());
	$printGlucosa.append("  " + $glucosaPaciente.val());
	$printCintura.append("  " + $cinturaPaciente.val());
	$printMedico.append("DR. Eduardo Espadas Pinzon");
	//$printMensaje.append("28 de mayo dia internacional de accion por la salud de la mujer")
	$sendRevision.button('reset');

	return false;
}

//Eventos

$printAndSetData.click( setDataToPrint );

$sendRevision.click( sendDataRevision );

//socket.on('addPsicologiaHojaPrevaloracion_respuesta', checkIsDataIsCorrect );