#!/bin/bash

for file in "$@"; do
	for url in $(cat $file); do
		host $url | grep "has address" | cut -d" " -f4
	done
done
