import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',8080))
s.listen(1)

while 1:
	conn, addr = s.accept()
	data = conn.recv(1024).decode('utf-8')
	request = data.split()
	cal = request[1].split('/')

	a = int(cal[1])
	b = int(cal[3])
	op = cal[2]
	
	if op == '+':
		result = a + b
	elif op == '-':
		result = a - b
	elif op == '%':
		result = a // b
	elif op == '*':
		result = a * b
	else:
		result = "invalid request"

	conn.sendall(str(result).encode())

	conn.close()
