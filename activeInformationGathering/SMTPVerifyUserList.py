#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 3:
    print "\n[*] Usage: " + sys.argv[0] + " <ip_address> <users_file>\n"
    sys.exit(0)

# Create a socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
connect=s.connect((sys.argv[1], 25))

# Receive the banner
banner=s.recv(1024)
print banner

with open(sys.argv[2]) as f:
    for username in f:
        # VRFY a user & print on success
        s.send('VRFY ' + username + '\r\n')
        result=s.recv(1024)
        if "250" in result:
            print result


# Close the socket
s.close()
