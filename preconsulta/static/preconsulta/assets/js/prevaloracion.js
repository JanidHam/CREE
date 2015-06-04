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

var $sendPaciente = $('#AgregarPaciente'),
    $nodeAlert = $('#nodeAlert');

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
    $municipioInput    = $('#municipioPaciente'),
    $apellidoPInput    = $('#apellidoPPaciente'),
    $apellidoMInput    = $('#apellidoMPaciente'),
    $fechaInput        = $('#nacimientoPaciente'),
    $escolaridadInput  = $('#escolaridadPaciente'),
    $referidoporInput  = $('#referidoporPaciente'),
    $entreCalleInput   = $('#entreCallesPaciente'),
    $codigoPostalInput = $('#codigoPostalPaciente');

//Variables globales
try {
  //$nodeAlert.hide();
  var socket = io.connect("http://" + urlServerNodeJS);
} catch(err) {
  socket = null;
  $nodeAlert.show();
  //Ya se maneja el error si no esta corriendo el servidor de nodeJS, falta mostrar un mensaje
  //de error para informar que no se guardaran los cambios
}    

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
      municipio : $municipioInput.val(),
      localidad : $localidadInput.val().toUpperCase(),
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
    $.post('/preconsulta/agregar-paciente/', datosPaciente , succesPaciente);
    cleanForm();
    show_hideForm();
    //console.log(datos);
    //socket.emit('nuevo_paciente', datosPaciente);
  }

  return false;
}

function succesPaciente(data) {
  var data = JSON.parse(data);
  //Nota: agregar la funcion showPaciente aqui cuando fue correcto el agregar paciente.
  //Cambiar el emit por un broadcast para que no lo emita al mismo cliente.
  if (data.isOk == "ok") {
    try {
      socket.emit('nuevo_paciente', data);
    } catch(err) {
      showPaciente(data);
    }
  } else {
    alert(data.isOk);
  }
  $sendPaciente.button('reset');
}

function showPaciente(data) {
  if (data.isOk == "ok") {
    var listapacientes = $('#listPacientes');    
    listapacientes.append('<a href="' + setURLByRol(data.curp) + 
      '/"' + setClassToEditPaciente() + '><div class="row showback None" data-correspondio="' + data.correspondio + '" data-curp="' + 
      data.curp + '" id="' + data.curp + '"> <div class="col-lg-6">' + data.nombre + ' ' + data.apellidoP + 
      '</div><div class="col-lg-6 goright">' + data.municipio + '</div></div></a>');
    $('.badge').text(parseInt($('.badge').text()) + 1);
  }
}

function setClassToEditPaciente() {
  if (grupo === "informacion")
    return 'data-toggle="modal" data-target="#modalEditPaciente"';
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
  } else if (grupo === "imprimir") {
      return "imprimir-documentos/" + curp;
  } else if (grupo === "enfermeria") {
      return "enfermeria/" + curp;
  } else {
      return "#";
  }
}

function updateEstatusPaciente(data) {
  if (data.isOk == "ok") {
    
    var correspondio = "True";
    if (!data.correspondio)
      correspondio = "False";

    var $paciente = $('#' + data.curp).attr('class', 'row showback ' + correspondio);

    if (!data.correspondio) {    
      var $a = $paciente.parent();
      $a.attr('href', '#');
    }
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
  
  var m    = curp.match( /^\w{4}(\w{2})(\w{2})(\w{2})(\w{6})(\w{1})/ )
  var anyo = parseInt(m[1],10) + 1900
  var mes  = parseInt(m[2], 10)
  var dia  = parseInt(m[3], 10)

  if (validIsLetterInCurp(m[5]))
    anyo = parseInt(m[1],10) + 2000
  
  if( anyo < 1950 ) { anyo += 100; }
  if (dia < 10) { dia = '0' + dia };
  if (mes < 10) { mes = '0' + mes };
  if (isInput)//Este valor determina si desea regresarlo en el formato año/mes/dia (en casa de ser true)
    return anyo + '-' + mes + '-' + dia;
  
  return dia + '-' + mes + '-' + anyo;
}

function validIsLetterInCurp(value) {
  var pattern = /[a-zA-Z]/
  return pattern.test(value)
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

function isUpdateCorrect(data) {
  var data = JSON.parse(data)
  if (data.isOk === "ok") {
    socket.emit('update_paciente_succes');
  } else {
    alert(data.isOk);
  }
}

function pacienteUpdateCorrectReloadPage() {
  location.reload();
}

function fillDataCurpToEditPaciente() {
  if ($('#paciente-curp').val() !== '') {
    if ($('#paciente-curp').val().length > 17) {
      //var fechaNacimientoShort = $curpInput.val().substring(4,10);
      var fechaNacimiento = curp2date($('#paciente-curp').val(), true);
      var genero          = getGenero($('#paciente-curp').val().substring(10,11));
      var edad            = getEdad(curp2date($('#paciente-curp').val(), false));

      $('#paciente-curp').val().toUpperCase();
      $('#paciente-genero').val(genero);
      $('#paciente-nacimiento').val(fechaNacimiento);
      $('#paciente-edad').val(edad);
      //console.log(genero);
    } else {
        cleanDataCurpEditPacienteInvalid();
    } 
  }
}

function cleanDataCurpEditPacienteInvalid() {
  $('#paciente-curp').val('');
  $('#paciente-edad').val('');
  $('#paciente-nacimiento').val('');
  $('#paciente-genero').val('');
  alert("La 'CURP' no tiene el formato correcto.");
}

// Eventos

$('#modalEditPaciente').on('show.bs.modal', function (event) {
  var itemPaciente = $(event.relatedTarget) // Element that triggered the modal
  var curpPaciente = itemPaciente.children().attr('id')
  var modal = $(this)
  
  $.post('/preconsulta/get-paciente/', {curpPaciente : curpPaciente} , function(data){
    var dataPaciente = JSON.parse(data)
    modal.find('.modal-title').text(dataPaciente.nombre + " " + dataPaciente.apellidoP + " - " + curpPaciente)
    modal.find('#paciente-curp').val(curpPaciente)
    modal.find('#paciente-nombre').val(dataPaciente.nombre)
    modal.find('#paciente-apellidoP').val(dataPaciente.apellidoP)
    modal.find('#paciente-apellidoM').val(dataPaciente.apellidoM)
    fillDataCurpToEditPaciente();
    //modal.find('#paciente-edad').val(dataPaciente.edad)
    //modal.find('#paciente-genero').val(dataPaciente.genero)
    //modal.find('#paciente-nacimiento').val(dataPaciente.nacimiento)
    modal.find('#paciente-telcasa').val(dataPaciente.telcasa)
    modal.find('#paciente-telcelular').val(dataPaciente.telcelular)
    modal.find('#paciente-localidad').val(dataPaciente.localidad)
    modal.find('#paciente-estadoprocedente').val(dataPaciente.idEstado)
    modal.find('#paciente-municipio').val(dataPaciente.idMunicipio)
    modal.find('#paciente-calle').val(dataPaciente.calle)
    modal.find('#paciente-entrecalles').val(dataPaciente.entrecalles)
    modal.find('#paciente-ocupacion').val(dataPaciente.idOcupacion)
    modal.find('#paciente-referidopor').val(dataPaciente.idReferidopor)
    modal.find('#paciente-colonia').val(dataPaciente.colonia)
    modal.find('#paciente-numcasa').val(dataPaciente.numerocasa)
    modal.find('#paciente-codigopostal').val(dataPaciente.codigopostal)
    modal.find('#paciente-escolaridad').val(dataPaciente.idEscolaridad)
  })

})

$('#modalEditPaciente').on('click', '#updatePacienteModal', function(){
  var modal = $('#modalEditPaciente') // Element that triggered the modal
  var titulo = modal.find('.modal-title').text()
  var curpPaciente = titulo.split(" - ")
  
  var newDataPaciente = {
        curpPaciente : curpPaciente[1],
        curp : modal.find('#paciente-curp').val(),
        nombre : modal.find('#paciente-nombre').val().toUpperCase(),
        apellidoP : modal.find('#paciente-apellidoP').val().toUpperCase(),
        apellidoM : modal.find('#paciente-apellidoM').val().toUpperCase(),
        edad : modal.find('#paciente-edad').val(),
        genero : getGeneroInt(modal.find('#paciente-genero').val()),
        fechaN : modal.find('#paciente-nacimiento').val(),
        telCasa : modal.find('#paciente-telcasa').val(),
        celular : modal.find('#paciente-telcelular').val(),
        localidad : modal.find('#paciente-localidad').val().toUpperCase(),
        calle : modal.find('#paciente-calle').val().toUpperCase(),
        entreCalles : modal.find('#paciente-entrecalles').val().toUpperCase(),
        colonia : modal.find('#paciente-colonia').val().toUpperCase(),
        numCasa : modal.find('#paciente-numcasa').val().toUpperCase(),
        codigoPostal : modal.find('#paciente-codigopostal').val(),
        referidopor : modal.find('#paciente-referidopor').val(),
        estado : modal.find('#paciente-estadoprocedente').val(),
        municipio : modal.find('#paciente-municipio').val(),
        ocupacion : modal.find('#paciente-ocupacion').val(),
        escolaridad : modal.find('#paciente-escolaridad').val(),
  }
  $.post('/preconsulta/update-paciente/', newDataPaciente , isUpdateCorrect )
})

$showForm.click( show_hideForm )

$sendPaciente.click( addPaciente )

$curpInput.focusout( fillDataCurp )

$('#paciente-curp').focusout( fillDataCurpToEditPaciente )

socket.on('mostrar_paciente', showPaciente );

socket.on('correspondio_paciente', updateEstatusPaciente );

socket.on('update_paciente_reloadpage', pacienteUpdateCorrectReloadPage)