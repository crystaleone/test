bob = {'name': 'Bob Smith', 'age': 42, 'pay': 300, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 400, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
if __name__ == '__main__':
	for key in db:
		print(key, '=>\n ', db[key])
