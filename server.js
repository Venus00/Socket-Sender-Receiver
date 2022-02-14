const io = require("socket.io")({
    allowEIO3: true // false by default
  });
var middleware = require('socketio-wildcard')();
var fs = require('fs');

var index = 0 

io.use(middleware);

//decode frame
function base64_decode(base64Image , index ) {
    var imageBuffer = new Buffer.from(base64Image, 'base64'); //console = <Buffer 75 ab 5a 8a ...
    fs.writeFile("myfile.jpg", imageBuffer,function(err) { //... });
    });
  
  }
io.on('connection', function(socket) {
console.log("Camera Device is connected")
  socket.on('StreamEvent', function(frame){
    console.log("payload is received")
    console.log(frame)
    base64_decode(frame,index)
    index++

  });
});

console.log("server listen to port 5000");
io.listen(5000);


