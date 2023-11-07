from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('',12000))
while True:
	msg, addr = s.recvfrom(1024)
	file = msg.decode('utf-8')
	filename = file + ".txt"
	f = open(filename, "r")
	data = f.read()
	s.sendto(data.encode('utf-8'), addr)

