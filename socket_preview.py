from socket import socket, AF_INET, SOCK_STREAM
import time
port = 50008
host = '192.168.6.120'
def server():
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(('', port))
	sock.listen(5)
	while True:
		conn, addr = sock.accept()
		data = conn.recv(1024)
		reply = 'server got: [%s]' % data
		conn.send(reply.encode())
def client(name):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((host, port))
	sock.send(name.encode())
	reply = sock.recv(1024)
	sock.close()
	print('client got: [%s]' % reply)
if __name__ == '__main__':
	from threading import Thread
	sthread = Thread(target=server)
	sthread.daemon = True
	sthread.start()
	time.sleep(5)
	for i in range(5):
		Thread(target=client, args=('client%s' % i,)).start()
