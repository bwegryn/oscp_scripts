#!/bin/bash

if [ $# -eq 3 ]; then
	for host in $(seq $2 $3); do
		host $1.$host | grep -v "not found" | cut -d " " -f1,5
	done
else 
	echo -e "\n[*] Usage: $0 <network> <host_min> <host_max>\n"
fi
