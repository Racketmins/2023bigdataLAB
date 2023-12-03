import socket
import datetime

def main():
	listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listen_sock.bind(('', 8080))
	listen_sock.listen(1)

	while 1:
		conn, addr = listen_sock.accept()
		data = conn.recv(1024)
		t = datetime.datetime.now()
		t_massage = "This time is " + t.strftime("%a %b %d %H:%M:%S %Y")
		conn.send(t_massage.encode())
		conn.close()
	
main()
