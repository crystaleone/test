import getfile
from getpass import getpass
filename = '1.jpg'

getfile.getfile(file=filename, 
				sit='ftp.rmi.net',
				dir = '.'
				user=('lutz', getpass('Pswd?')),
				refetch=True)

if input('Open file?') in ['Y', 'y']:
	from PP4E.System.Media.playfile import playfile
	playfile(filename)
