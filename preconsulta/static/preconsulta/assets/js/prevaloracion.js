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

var $sendPaciente = $('#AgregarPaciente');

var $form    = $('#form'),
    $showForm          = $('#showForm'),
    $edadInput         = $('#edadPaciente'),
    $curpInput         = $('#curpPaciente'),
    $calleInput        = $('#callePaciente'),
    $nombreInput       = $('#nombrePaciente'),
    $estadoInput       = $('#estadoPaciente'),
    $generoInput       = $('#generoPaciente'),
    $coloniaInput      = $('#coloniaPaciente'),
    $telefonoInput     = $('#telCasaPaciente'),
    $celularInput      = $('#celularPaciente'),
    $numCasaInput      = $('#numCasaPaciente'),
    $ocupacionInput    = $('#ocupacionPaciente'),
    $localidadInput    = $('#localidadPaciente'),
    $apellidoPInput    = $('#apellidoPPaciente'),
    $apellidoMInput    = $('#apellidoMPaciente'),
    $fechaInput        = $('#nacimientoPaciente'),
    $escolaridadInput  = $('#escolaridadPaciente'),
    $referidoporInput  = $('#referidoporPaciente'),
    $entreCalleInput   = $('#entreCallesPaciente'),
    $codigoPostalInput = $('#codigoPostalPaciente');

var isHombre = "HOMBRE",
    isMujer  = "MUJER";

//Funciones
function addPaciente() {
  if (validForm()) {
    $sendPaciente.button('loading');
    var datosPaciente = {
      curp : $curpInput.val().toUpperCase(),
      nombre : $nombreInput.val().toUpperCase(),
      apellidoP : $apellidoPInput.val().toUpperCase(),
      apellidoM : $apellidoMInput.val().toUpperCase(),
      edad : $edadInput.val(),
      genero : getGeneroInt($generoInput.val()),//"1",//$generoInput.val(),
      fechaN : $fechaInput.val(),//"2015-03-19",//$fechaInput.val(),
      telCasa : $telefonoInput.val(),
      celular : $celularInput.val(),
      estado : $estadoInput.val(),
      localidad : $localidadInput.val(),
      calle : $calleInput.val().toUpperCase(),
      entreCalles : $entreCalleInput.val().toUpperCase(),
      colonia : $coloniaInput.val().toUpperCase(),
      numCasa : $numCasaInput.val().toUpperCase(),
      codigoPostal : $codigoPostalInput.val(),
      referidopor : $referidoporInput.val(),
      ocupacion : $ocupacionInput.val(),
      escolaridad : $escolaridadInput.val(),
      //usuario : user.toUpperCase(),
    }   
    cleanForm();
    $.post('/preconsulta/agregar-paciente/', datosPaciente , succesPaciente);
    show_hideForm();
    //console.log(datos);
    //socket.emit('nuevo_paciente', datosPaciente);
  }

  return false;
}

function succesPaciente(data) {
  //console.log(data);
  var data = JSON.parse(data);
  //console.log(data);
  if (data.isOk == "ok") {
    socket.emit('nuevo_paciente', data);
  }
  $sendPaciente.button('reset');
}

function showPaciente(data) {
  if (data.isOk == "ok") {
    var listapacientes = $('#listPacientes');    
    listapacientes.append('<a href="' + setURLByRol(data.curp) + 
      '/"> <div class="row showback None" data-correspondio="' + data.correspondio + '" data-curp="' + 
      data.curp + '" id="' + data.curp + '"> <div class="col-lg-6">' + data.nombre + ' ' + data.apellidoP + 
      '</div><div class="col-lg-6 goright">' + data.estadoProcendete + '</div></div></a>');
    $('.badge').text(parseInt($('.badge').text()) + 1);
    //alert("Paciente agregado con exito.");
  }
}

function setURLByRol(curp) {
  if (grupo === "informacion") {
    return "#";
  } else if(grupo === "revisionMedica") {
      return "revision-medica/" + curp;
  } else if (grupo === "revisionPsicologica") {
      return "revision-psicologica/" + curp;
  } else if (grupo === "trabajoSocial") {
      return "revision-estudio-socioeconomico/" + curp;
  } else {
      return "#";
  }
}

function updateEstatusPaciente(data) {
  //var data = JSON.parse(data);
  //console.log(data);  
  if (data.isOk == "ok") {
    
    var correspondio = "True";
    if (!data.correspondio)
      correspondio = "False";

    var $paciente = $('#' + data.curp).attr('class', 'row showback ' + correspondio);

    if (!data.correspondio) {    
      var $a = $paciente.parent();
      $a.attr('href', '#');
    }
    //console.log($paciente);
    //console.log($('#' + data.curp).attr('class'));
  } 
}

function show_hideForm() {
	$form.slideToggle();
	return false;
}

function validForm() {
  if ($curpInput.val() !== '') {
    if ($nombreInput.val() !== '') {
      if ($apellidoPInput.val() !== '') {
        if ($estadoInput.val() !== '') {
          if ($calleInput.val() !== '') {
            if ($coloniaInput.val() !== '') {
              if ($codigoPostalInput.val() !== '') {
                return true;
              } else 
                alert("El 'Codigo Postal' no puede ir vacio.");
            } else 
                alert("La 'Colonia' no puede ir vacio.");
          } else
              alert("La 'Calle' no puede ir vacio.");
        } else 
            alert("El 'Estado' no puede ir vacio.");
      } else
          alert("El 'Apellido Parterno' no puede ir vacio.");
    } else
        alert("El 'Nombre' no puede ir vacio.");
  } else
      alert("La 'CURP' no puede ir vacio.");
}

function cleanForm() {
  $curpInput.val('');
  $nombreInput.val('');
  $apellidoPInput.val('');
  $apellidoMInput.val('');
  $edadInput.val('');
  $generoInput.val('');
  $fechaInput.val('');
  $telefonoInput.val('');
  $celularInput.val('');
  $estadoInput.val('');
  $localidadInput.val('');
  $calleInput.val('');
  $entreCalleInput.val('');  
  $coloniaInput.val('');
  $numCasaInput.val('');
  $codigoPostalInput.val('');
}

function fillDataCurp() {
	//console.log($curpInput.val().length);
  if ($curpInput.val() !== '') {
    if ($curpInput.val().length > 17) {
      //var fechaNacimientoShort = $curpInput.val().substring(4,10);
      var fechaNacimiento = curp2date($curpInput.val(), true);
      var genero          = getGenero($curpInput.val().substring(10,11));
      var edad            = getEdad(curp2date($curpInput.val(), false));

      $curpInput.val($curpInput.val().toUpperCase());
      $generoInput.val(genero);
      $fechaInput.val(fechaNacimiento);
      $edadInput.val(edad);
      //console.log(genero);
    } else {
        cleanDataCurpInvalid();
    } 
  }
}

function cleanDataCurpInvalid() {
  $curpInput.val('');
  $edadInput.val('');
  $fechaInput.val('');
  $generoInput.val('');
  alert("La 'CURP' no tiene el formato correcto.");
}

function getGenero(letra) {
  if (letra.toUpperCase() === 'H')
    return isHombre;
  else if (letra.toUpperCase() === 'M')
    return isMujer;
}

function getGeneroInt(genero) {
  if (genero === isHombre)
    return 1;
  else if (genero === isMujer)
    return 0;
}

function curp2date(curp, isInput) {
  var m = curp.match( /^\w{4}(\w{2})(\w{2})(\w{2})/ );
  
  var anyo = parseInt(m[1],10)+1900;
  var mes = parseInt(m[2], 10);
  var dia = parseInt(m[3], 10);
  
  if( anyo < 1950 ) { anyo += 100; }
  if (dia < 10) { dia = '0' + dia };
  if (mes < 10) { mes = '0' + mes };
  if (isInput)
    return anyo + '-' + mes + '-' + dia;
  else
    return dia + '-' + mes + '-' + anyo;
}

function getEdad(fecha) {
  var fechaActual = new Date()
  var diaActual   = fechaActual.getDate();
  var mmActual    = fechaActual.getMonth() + 1;
  var yyyyActual  = fechaActual.getFullYear();
  var FechaNac    = fecha.split("-");
  var diaCumple   = FechaNac[0];
  var mmCumple    = FechaNac[1];
  var yyyyCumple  = FechaNac[2];
  //retiramos el primer cero de la izquierda
  if (mmCumple.substr(0,1) == 0) {
  mmCumple= mmCumple.substring(1, 2);
  }
  //retiramos el primer cero de la izquierda
  if (diaCumple.substr(0, 1) == 0) {
  diaCumple = diaCumple.substring(1, 2);
  }
  var edad = yyyyActual - yyyyCumple;

  //validamos si el mes de cumpleaños es menor al actual
  //o si el mes de cumpleaños es igual al actual
  //y el dia actual es menor al del nacimiento
  //De ser asi, se resta un año
  if ((mmActual < mmCumple) || (mmActual == mmCumple && diaActual < diaCumple)) {
    edad--;
  }

  return edad;
}

// Eventos

$showForm.click( show_hideForm )

$sendPaciente.click( addPaciente )

$curpInput.focusout( fillDataCurp )

socket.on('mostrar_paciente', showPaciente );

socket.on('correspondio_paciente', updateEstatusPaciente );