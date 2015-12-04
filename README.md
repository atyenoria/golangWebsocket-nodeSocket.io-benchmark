#Result
![socket.io benchmark](https://github.com/atyenoria/master/websocket-socket.io-benchmark/graph1.png)




#test command
##node-socket.io
websocket-bench -a 20 -c 10 ws://localhost:3000
websocket-bench -a 2000 -c 30 ws://localhost:3000
websocket-bench -a 2000 -c 40 ws://localhost:3000
websocket-bench -a 2000 -c 60 ws://localhost:3000

##go-socket.io

websocket-bench -a 200 -c 20 ws://localhost:5000



 
#References
https://github.com/M6Web/websocket-bench



