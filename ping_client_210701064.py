from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 8000))
msg = s.recv(1024)
print(msg)
s.close()