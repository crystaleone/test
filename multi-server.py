import os, time, sys
from socket import *
from multiprocessing import Process
myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

def now():
	return time.ctime(time.time())

activeChildren = []
def reapChildren():
	while activeChildren:
		pid, stat = os.waitpid(0, os.WNOHANG)
		if not pid: break
		activeChildren.remove(pid)

def handleClient(connection):
	print('Child:', os.getpid())
	time.sleep(5)
	while True:
		data = connection.recv(1024)
		if not data: break
		reply = 'Echo=>%s at %s' % (data, now())
		connection.send(reply.encode())
	connection.close()
	os._exit(0)

def dispatcher():
	while True:
		connection, address = sockobj.accept()
		print('Server connected by', address, end=' ')
		print('at', now())
		Process(target=handleClient, args=(connection,)).start()

if __name__ == '__main__':
	print('Parent:', os.getpid())
	sockobj = socket(AF_INET, SOCK_STREAM)
	sockobj.bind((myHost, myPort))
	sockobj.listen(5)
	dispatcher()
