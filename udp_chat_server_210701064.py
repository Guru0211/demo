# from socket import *
# s = socket(AF_INET, SOCK_DGRAM)
# s.bind(('',12000))
# while True:
# 	msg, addr = s.recvfrom(1024)
# 	print(msg)
# 	data = input()
# 	s.sendto(b'data')


from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 12000))
while True:
    msg, addr = s.recvfrom(1024)
    print(msg.decode('utf-8'))
    data = input("Enter a response: ")
    s.sendto(data.encode('utf-8'), addr)
