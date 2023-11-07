from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(("",8001))
s.listen(5)

c,a = s.accept()

while True:
	msg = c.recv(100).decode()
	print(msg)
	server_chat = input()
	c.send(server_chat.encode('utf-8'))
c.close()

