$( document ).ready(function() {
    var $input = $('input');

    $input.attr('class', 'form-control');
    $('#id_username').attr('placeholder', 'USUARIO');
    $('#id_password').attr('placeholder', 'CONTRASEÑA');
    $('#id_password').attr('type', 'password');
});