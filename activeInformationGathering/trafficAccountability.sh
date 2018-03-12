#!/bin/bash

if [ $# -eq 1 ]; then
	# reset all counter and iptables rules
	iptables -Z && iptables -F

	# measure incoming traffic to <ip_address>
	iptables -I INPUT 1 -s $1 -j ACCEPT

	# measure outgoing traffic to <ip_address>
	iptables -I OUTPUT 1 -d $1 -j ACCEPT

	# run nmap against 1000 most popular ports
	nmap $1

	iptables -vn -L
else
	echo -e "\n[*] Usage: $0 <ip_address>\n"
fi

