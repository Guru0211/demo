from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(("",8000))
s.listen(5)
while True:
	c,a = s.accept()
	msg = c.recv(100).decode()
	print(msg)
	c.send(msg.encode('utf-8'))
	c.close()
