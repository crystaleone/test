#!/usr/bin/python

import cgi, sys
form = cgi.FieldStorage()
print("Content-type: text/html")

html = """
<title>tutor5.py</title>
<h1>Greetings</h1>
<hr>
<h4>your name is %(name)s</h4>
<h4>you wear rather %(shoesize)s shoes</h4>
<h4>your current job: %(job)s</h4>
<h4>you program in %(language)s</h4>
<h4>you also said:</h4>
<p>%(comment)s</p>
<hr>"""

data = {}
for field in ('name', 'shoesize', 'job', 'language', 'comment'):
	if not field in form:
		data[field] = '(unknown)'
	else:
		if not isinstance(form[field], list):
			data[field] = form[field].value
		else:
			values = [x.value for x in form[field]]
			data[field] = ' and '.join(values)
print(html % data)
