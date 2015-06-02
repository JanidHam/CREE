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

var $sendRevision = $('#sendDataEnfermeriaPaciente');

var $printAndSetData = $('#printAndSetData');

var $form    = $('#form'),
	$pesoPaciente = $('#pesoPaciente'),
	$tallaPaciente = $('#tallaPaciente'),
	$fcPaciente = $('#fcPaciente'),
	$taPaciente = $('#taPaciente'),
	$glucosaPaciente = $('#glucosaPaciente'),
	$cinturaPaciente = $('#cinturaPaciente'),
	$clave = $('#clave'),
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
		mensajeInformativo : $printMensaje.val(),
		clave : $clave.val(),
		curp : CURP,
	}
	$.post('/preconsulta/agregar-enfermeria/', datosRevision , checkIsDataIsCorrect);
	
	return false;
}

function checkIsDataIsCorrect(data) {
	var data = JSON.parse(data);
	if (data.isOk == "ok") {
		window.location.href = "/preconsulta/";
	} else {
		alert(data.isOk);
		$sendRevision.button('reset');
	}
}

function setDataToPrint(){
	$printPeso.text("  " + $pesoPaciente.val());
	$printTalla.text("  " + $tallaPaciente.val());
	$printFC.text("  " + $fcPaciente.val());
	$printTA.text("  " + $taPaciente.val());
	$printGlucosa.text("  " + $glucosaPaciente.val());
	$printCintura.text("  " + $cinturaPaciente.val());
	$printMedico.text("DR. Eduardo Espadas Pinzon");
	//$printMensaje.append("28 de mayo dia internacional de accion por la salud de la mujer")
	$sendRevision.button('reset');
	window.print();
	return false;
}

//Eventos

$printAndSetData.click( setDataToPrint );

$sendRevision.click( sendDataRevision );