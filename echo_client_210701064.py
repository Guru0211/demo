from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1",8000))
data = input()
s.send(data.encode('utf-8'))
msg = s.recv(100).decode()
print(msg)
s.close()