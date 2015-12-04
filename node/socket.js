exports = module.exports = function(io) {
    io.on('connection', function(socket) {
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