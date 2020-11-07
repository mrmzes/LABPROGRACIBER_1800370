#!/bin/bash

ippr=$(ip route get 8.8.8.8 | awk '{print $NF; exit}')
ippu=$(curl ifconfig.me | grep ".")
IFS='.' read -ra mask <<< "$ippr"

echo '\n\n'
$(nmap -Pn -p 1,100 $ippr)

echo 'Private IP: '$ippr
echo 'Public IP: '$ippu
