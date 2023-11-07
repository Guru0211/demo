from socket import *
s = socket(AF_INET, SOCK_DGRAM)
addr = ("127.0.0.1", 12000)
while True:
	a = float(input("Enter value 1: "))
	b = float(input("Enter value 2: "))
	o = input("Enter +, -, *, /: ")
	data = f"{a},{b},{o}"
	s.sendto(data.encode('utf-8'), addr)
	data, server = s.recvfrom(1024)
	print(data.decode('utf-8'))