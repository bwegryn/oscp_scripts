#!/bin/bash

if [ $# -eq 1 ]; then
	for server in $(host -t ns $1 | cut -d " " -f4); do
		host -l $1 $server | grep "has address"
	done
else
	echo -e "\n[*] Usage: $0 <domain>\n"
fi
