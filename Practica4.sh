#!/bin/bash

IFS='.' read -ra first <<<$1
if [ -z "$1" ]; then
IFS='.' read -ra last <<< $1
else; then
IFS='.' read -ra last <<< $2
fi
host=0
function isTop1000TcpPortsAlive {
for ((port=1; port<1001; port++))
    do
        if (nc -zv $host $port 2>&1 | grep succeeded > /dev/null 2>&1); then
            echo "$host have port: $port Open"
        fi
    done
}
function isHostAlive {
if (ping -c 1 $host > /dev/null 2>&1); then
        isTop1000TcpPortsAlive
fi
}
function dinamicIp {
for oct1 in $(seq ${first[0]} ${last[0]})
do
    for oct2 in $(seq ${first[1]} ${last[1]})
    do
        for oct3 in $(seq ${first[2]} ${last[2]})
        do
            for oct4 in $(seq ${first[3]} ${last[3]})
            do
                host=$(echo "$oct1.$oct2.$oct3.$oct4")
                isHostAlive
            done
        done
    done
done

}
dinamicIp