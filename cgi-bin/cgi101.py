#!/root/.pyenv/versions/3.5.2/bin/python
import cgi
form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if not 'user' in form:
	print('<h1>who are you?</h1>')
else:
	print('<h1>hello <i>%s</i>!</h1>' % cgi.escape(form['user'].value))
