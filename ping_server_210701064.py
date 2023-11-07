from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(("",8000))
s.listen(5)
while True:
	c,a = s.accept()
	print(f"listening to the addresss {a}")
	c.send(b"Successfully connected to the server")
c.close()