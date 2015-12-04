exports = module.exports = function(io) {
    var count = 0
    io.on('connection', function(socket) {
        console.log("connect" , count++)
        socket.on('disconnect', function() {
            console.info('SOCKET [%s] DISCONNECTED', socket.id);
        });
        socket.emit('test', {
            test: "server ok"
        })
        socket.on('test', function(msg) {
            console.log(msg)
        });
    })
};