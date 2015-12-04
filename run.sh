#!/usr/bin/env bash

A=20
C=20

pushd websocket-bench > /dev/null
echo "Concurrency,Number,Connections,Errors, Message Send,Message Fail,Duration(ms)" > result.txt
for (( n = 1; n < 10; n++ )); do # A
for (( i = 1; i < 10; i++ )); do # C

AA=`expr $A \* $n`
CC=`expr $C \* $i`

echo -n "${CC}," >> result.txt

node  bin/websocket-bench -a ${AA} -c ${CC} ws://localhost:3000


done
done
popd  > /dev/null