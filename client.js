//client.js
var io = require('socket.io-client');
var socket = io.connect('http://localhost:5000', {reconnect: true});

// Add a connect listener
socket.on('connect', function (socket) {
    console.log('Connected!');
});
socket.emit('StreamEvent', 'me', 'test msg');

