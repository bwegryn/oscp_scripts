#!/bin/bash

if [ $# -eq 0 ]; then
	echo -e "\n[*] Usage: $0 <host(s)>\n"
	exit 0
fi

for host in "$@"; do
	for name in $(cat list.txt); do
		host $name.$host | grep "has address" | cut -d " " -f1,4
	done
done
