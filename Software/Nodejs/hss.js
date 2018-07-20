
var app = require('http').createServer(handler);
var io  = require('/usr/local/lib/node_modules/bonescript/node_modules/socket.io').listen(app);
var fs  = require('fs');
var bb  = require('bonescript');
const spawn = require('child_process').spawn;

var htmlPage = '/home/debian/HSS/hss.html'; // use this for Debian

var pinStates = {};
var soc;

app.listen(9090);

function handler (req, res) {
  fs.readFile(htmlPage,
    function (err, data) {
      if (err) {
        res.writeHead(500);
        return res.end('Error loading file: ' + htmlPage);
      }
      res.writeHead(200);
      res.end(data);
    });
}

function onConnect(socket) {
    socket.on('digitalWrite', handleDigitalWrite);
    socket.on('monitor', handleMonitorRequest);
    soc = socket;
}

function handleMonitorRequest(pin) {
    bb.pinMode(pin, bb.INPUT);
    pinStates[pin] = 0;
}

function handleDigitalWrite(message) {
    var data = JSON.parse(message);
    bb.pinMode(data.pin, bb.OUTPUT);
    bb.digitalWrite(data.pin, data.value);
    if (data.pin == "P8_11")
    {
       bb.pinMode("P8_17", bb.OUTPUT);
       bb.digitalWrite("P8_17", 1);
       pause(500);
       bb.digitalWrite("P8_17", 0);
    }
}

function checkInputs() {
    for (var pin in pinStates) {
        var oldValue = pinStates[pin];
        var newValue = bb.digitalRead(pin);
        if (oldValue != newValue) {
            soc.emit("pinUpdate", '{"pin":"' + pin + '", "value":' + newValue + '}');

            pinStates[pin] = newValue;
        }
    }
}

function pause(milliseconds) {
        var dt = new Date();
        while ((new Date()) - dt <= milliseconds) { /* Do nothing */ }
}
io.sockets.on('connection', onConnect);

setInterval(checkInputs, 500);
