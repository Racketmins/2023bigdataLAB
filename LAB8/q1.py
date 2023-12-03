from socket import *

with socket(AF_INET, SOCK_STREAM) as s:
	s.bind(('', 21567))
	while True:
		s.listen(1)

		conn, addr = s.accept()
		data = conn.recv(1024)
	
		if data.decode() == "exit":
			break
		conn.sendall((data.decode()).encode())
	conn.close()
