from socket import *

BUFSIZ = 1024
print('Input "exit" to quit')
while True:
	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(('localhost', 21567))
	data =input('> ')
	if not data:
		break
	tcpCliSock.send(data.encode())
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print(data.decode().strip())
	tcpCliSock.close()

