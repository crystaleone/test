#!/usr/bin/python

import cgi
form = cgi.FieldStorage()
print('Content-type: text/html')

html = """
<TITLE>tutor3.py</TITLE>
<H1>Greetings</H1>
<HR>
<P>%s</P>
<HR>"""

if not 'user' in form:
	print(html % 'who are you?')
else:
	print(html % ('hello, %s.' % form['user'].value))
