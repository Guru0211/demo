from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('',12000))
while True:
	msg, addr = s.recvfrom(1024)
	s.sendto(msg, addr)