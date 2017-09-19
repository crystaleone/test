import threading, _thread
def action(i):
	print(i ** 32)

class Mythread(threading.Thread):
	def __init__(self, i):
		self.i = i
		threading.Thread.__init__(self)
	def run(self):
		print(self.i ** 322)
Mythread(2).start()

thread = threading.Thread(target=(lambda: action(2)))
thread.start()

threading.Thread(target=action, args=(2,)).start()

_thread.start_new_thread(action, (2,))

#class Power:
#	def __init__(self, i):
#		self.i = i
#	def action(self):
#		print(self.i ** 32)
#obj = Power(2)
#threading.Thread(target=obj.action).start()
#
#def action(i):
#	def power():
#		print(i ** 32)
#	return power
#threading.Thread(target=action(2)).start()
#
#_thread.start_new_thread(obj.action, ())
#_thread.start_new_thread(action(2), ())
