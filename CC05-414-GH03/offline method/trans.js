var aqia=0,aqib=0,aqic=0;

var http = require('http');

var express = require('express');
var app = express();
var http2 = require('http').Server(app);
var io = require('socket.io')(http2);


http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end(aqia.toString()+" "+aqib.toString()+" "+aqic.toString());
}).listen(8080);


app.use(express.static('public'));
io.on('connection', function(socket){
  console.log('user connected');
  socket.on('roada', function(msg){
    console.log(msg);
	aqia = msg;
  });
  socket.on('roadb', function(msg){
    console.log(msg);
	aqib = msg;
  });
  socket.on('roadc', function(msg){
    console.log(aqia,aqib,aqic);
	aqic = msg;
  });
});

http2.listen(8081);






console.log("listening on",require("ip").address()+":8080");