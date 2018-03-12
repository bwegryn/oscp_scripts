#!/bin/bash

for network in $(hostname -I | cut -d "." -f1-3 | uniq); do
	for host in $(seq 0 254); do
		ping -c 1 $network.$host | grep "bytes from" | cut -d" " -f4 | cut -d ":" -f1 &
	done
done
