#!/usr/bin/python
debugme = False
inputkey = 'language'

hellos = {
	'Python': r"print('hello world')",
	'Python2': r"print 'hello wolrd'",
	'Perl': r' print "hello world\n";',
	'Tcl': r'puts "hello world"',
	'Scheme': r'(display "hello world") (newline)',
	'SmallTalk': r" 'hello world' print.",
	'Java': r'System.out.println("hello world");',
	'C': r'printf("hello world\n");',
	'C++': r'cout << "hello world" << endl;',
	'Basic': r'10 PRINT "hello world"',
	'Fortran': r"print *, 'hello world'",
	'Pascal': r"writeLn('hello world');"
}

class dummy:
	def __init__(self, str): self.value = str

import cgi, sys
if debugme:
	form = {inputkey: dummy(sys.argv[1])}
else:
	form = cgi.FieldStorage()

print('Content-type: text/html\n')
print('<title>Languages</title>')
print('<h1>Syntax</h1><hr>')

def showHello(form):
	choice = form[inputkey].value
	print('<h3>%s</h3><p><pre>' % choice)
	try:
		print(cgi.escape(hellos[choice]))
	except KeyError:
		print('soor--i donot know that language')
	print('</pre></p><br>')

if not inputkey in form or form[inputkey].value == 'All':
	for lang in hellos.keys():
		mock = {inputkey: dummy(lang)}
		showHello(mock)
else:
	showHello(form)
print('<hr>')
