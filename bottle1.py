from bottle import route, run

@route('/')
def home():
	return "It isn't fancy, but it's my home page"

run(host="192.168.6.120",port=9999)
