#Method
Once per 1 second, client socket.io  test library send socket.io connections,which is about simulatneous conncurrencies numbers, to socket.io servers.  

##Tested Plaformed
[~/work2/chat/websocket-bench]$ system_profiler SPHardwareDataType                                                                                                     *[master]
Hardware:

    Hardware Overview:

      Model Name: MacBook Pro
      Model Identifier: MacBookPro11,5
      Processor Name: Intel Core i7
      Processor Speed: 2.5 GHz
      Number of Processors: 1
      Total Number of Cores: 4
      L2 Cache (per Core): 256 KB
      L3 Cache: 6 MB
      Memory: 16 GB
      Boot ROM Version: MBP114.0172.B00
      SMC Version (system): 2.30f1
      Serial Number (system): C17PR07VG8WP
      Hardware UUID: 34111C30-E887-5F06-8995-D9DBD79F8DC3
#Result
![socket.io benchmark](https://github.com/atyenoria/websocket-socket.io-benchmark/blob/master/socket.io.png)
![socket.io benchmark](https://github.com/atyenoria/websocket-socket.io-benchmark/blob/master/golang.png)

#Discussion


#Preparetion
##general
ulimit -n 65530
##golang socket.io
    cd go-socket.io/main.go && go build && ./go-socket.io/go-socket.io
    
Probably, Something wrong with go-socket.io. But, I couldn't figure out why. So, Help me....

##node.js socket.io
    cd node-socket.io && npm install && node bin.js
  
##test command
### node.js socket.io (need redis withou pass)
    ./run 3000
### golang socket.io
    ./run 5000




 

#References
https://github.com/M6Web/websocket-bench
https://github.com/googollee/go-socket.io

