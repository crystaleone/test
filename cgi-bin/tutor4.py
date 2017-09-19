#!/usr/bin/python

import cgi, sys
sys.stderr = sys.stdout
form = cgi.FieldStorage()
print('Content-type: text/html\n')

html = """
<TITLE>tutor4.py</TITLE>
<H1>Greetings</H1>
<HR>
<H4>%s</H4>
<H4>%s</H4>
<H4>%s</H4>
<HR>"""

if not 'user' in form:
	line1 = 'who are you?'
else:
	line1 = 'hello, %s.' % form['user'].value

line2 = "you're talking to a %s server." % sys.platform

line3 = ""
if 'age' in form:
	try:
		line3 = "your age squared is %d!" % (int(form['age'].value) ** 2)
	except:
		line3 = "sorry, i can't compute %s ** 2." % form['age'].value

print(html % (line1, line2, line3))


