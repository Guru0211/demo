from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('',12000))
while True:
	msg, addr = s.recvfrom(1024)
	data = msg.decode('utf-8')
	a, b, o = data.split(',')
	a1 = float(a)
	b1 = float(b)
	if o=='+':
		ans = a1+b1
	elif o=='-':
		ans = a1-b1
	elif o=='*':
		ans = a1*b1
	elif o=='/':
		ans = a1/b1
	ans1 = str(ans)
	s.sendto(ans1.encode('utf-8'), addr)

