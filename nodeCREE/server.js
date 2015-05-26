var http = require('http');
var server = http.createServer().listen(3000);
var io = require('socket.io').listen(server);
var querystring = require('querystring');

io.on('connection', function(socket) {
	/*socket.on('nuevo_paciente', function(data) {
		var values = querystring.stringify(data);
		var options = {
			hostname : 'localhost',
			port : '8000',
			path : '/preconsulta/agregar-paciente/',
			method : 'POST',
			headers : {
				'Content-Type' : 'application/x-www-form-urlencoded',
				'Content-Length' : values.length
			}
		}

		var request = http.request(options, function(response){
			response.setEncoding('utf8');
			response.on('data', function(data){
				// aqui viene los datos django
				io.emit('mostrar_paciente', data);
			});
		});
		request.write(values);
		request.end();
	});
	*/
	socket.on('nuevo_paciente', function(data) {
		io.emit('mostrar_paciente', data);		
	});

	socket.on('update_paciente_succes', function() {
		io.emit('update_paciente_reloadpage');		
	});

	socket.on('addHojaPrevaloracion', function(data) {
		var values = querystring.stringify(data);
		var options = {
			hostname : 'localhost',
			port : '8000',
			path : '/preconsulta/agregar-hoja-prevaloracion/',
			method : 'POST',
			headers : {
				'Content-Type' : 'application/x-www-form-urlencoded',
				'Content-Length' : values.length
			}
		}

		var request = http.request(options, function(response){
			response.setEncoding('utf8');
			response.on('data', function(data){
				// aqui viene los datos django
				io.emit('addHojaPrevaloracion_Respuesta', data);
			});
		});
		request.write(values);
		request.end();
	});

	socket.on('dataIsSaveSucces_revision_medica', function(data) {
		if (data.isOk == "ok") {
			io.emit('correspondio_paciente', data);
		}		
	});

	socket.on('addPsicologiaHojaPrevaloracion', function(data) {
		var values = querystring.stringify(data);
		var options = {
			hostname : 'localhost',
			port : '8000',
			path : '/preconsulta/agregar-hoja-prevaloracion-psicologia/',
			method : 'POST',
			headers : {
				'Content-Type' : 'application/x-www-form-urlencoded',
				'Content-Length' : values.length
			}
		}

		var request = http.request(options, function(response){
			response.setEncoding('utf8');
			response.on('data', function(data){
				// aqui viene los datos django
				io.emit('addPsicologiaHojaPrevaloracion_respuesta', data);
			});
		});
		request.write(values);
		request.end();
	});

	socket.on('addEstudioSEconomico', function(data) {
		var values = querystring.stringify(data);		
		var options = {
			hostname : 'localhost',
			port : '8000',
			path : '/preconsulta/agregar-estudio-socio-economico/',
			method : 'POST',
			headers : {
				'Content-Type' : 'application/x-www-form-urlencoded',
				'Content-Length' : values.length
			}
		}

		var request = http.request(options, function(response){
			response.setEncoding('utf8');
			response.on('data', function(data){
				// aqui viene los datos django
				io.emit('addEstudioSEconomico_respuesta', data);
			});
		});
		request.write(values);
		request.end();
	});
});