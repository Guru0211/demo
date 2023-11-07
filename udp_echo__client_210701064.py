from socket import *
s = socket(AF_INET, SOCK_DGRAM)
msg = input()
addr = ("127.0.0.1", 12000)
s.sendto(msg.encode('utf-8'), addr)
data, server = s.recvfrom(1024)
print(data.decode('utf-8'))