def interact():
	print('hello stream world')
	while True:
		try:
			reply = input('enter a number>')
		except EOFError:
			break
		else:
			num = int(reply)
			print('%d squared is %d' % (num, num ** 2))
	print('bye')
if __name__ == '__main__':
	interact()
