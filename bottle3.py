from bottle import route, run, static_file

@route('/')
def home():
	return static_file('index.html', root='.')

@route('/echo/<thing>')
def echo(thing):
	return "Say hello to my little friend: %s!" % thing

run(host='192.168.6.120', port=9999)
