from bottle import route, run, static_file

@route('/')
def main():
	return static_file('index.html', root='.')

run(host='192.168.6.120', port=9999)
