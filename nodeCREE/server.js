var http = require('http');
var server = http.createServer().listen(3000);
var io = require('socket.io').listen(server);
var querystring = require('querystring');

io.on('connection', function(socket) {
	socket.on('nuevo_paciente', function(data) {
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
				io.emit('correspondio_paciente', data);
			});
		});
		request.write(values);
		request.end();
	});
});