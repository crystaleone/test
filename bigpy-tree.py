import sys, os, pprint
trace = False
if sys.platform.startswith('win'):
	dirname = '/root/.pyenv/versions/3.5.2/lib/python3.5/'
else:
	dirname = '/root/.pyenv/versions/3.5.2/lib/python3.5/'

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
	if trace: print(thisDir)
	for filename in filesHere:
		if filename.endswith('.py'):
			if trace: print('...', filename)
			fullname = os.path.join(thisDir, filename)
			fullsize = os.path.getsize(fullname)
			allsizes.append((fullsize, fullname))
allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
