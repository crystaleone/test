import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler
webdir = '/root/workspace3.5.2'
port = 8081
os.chdir(webdir)
srvraddr = ('', port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
