import os, getpass
from urllib.request import urlopen

filename = '1.jpg'
password = getpass.getpass('Pswd?')

remoteaddr = 'ftp:/lutz:%s@ftp.rmi.net/%s;type=i' % (password, filename)
print('Downloading', remoteaddr)

remotefile = urlopen(remoteaddr)
localfile = open(filename, 'wb')
localfile.write(remote.read())
localfile.close()
remotefile.close()
