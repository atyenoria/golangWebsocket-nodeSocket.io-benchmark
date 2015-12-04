#test command
##node-socket.io
websocket-bench -a 2000 -c 10 ws://localhost:3000
websocket-bench -a 2000 -c 30 ws://localhost:3000
websocket-bench -a 2000 -c 40 ws://localhost:3000
websocket-bench -a 2000 -c 60 ws://localhost:3000

##go-socket.io
websocket-bench -a 200 -c 10 -g bench.js ws://localhost:5000
websocket-bench -a 2000 -c 30 -g bench.js ws://localhost:5000
websocket-bench -a 2000 -c 40 -g bench.js ws://localhost:5000
websocket-bench -a 2000 -c 60 -g bench.js ws://localhost:5000