# socket, ssl -> low-level networking interface and SSL wrapper for socket object
import socket
import ssl

hostname = 'www.python.org'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())

# email -> email and MIME handling package
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

# json -> JSON encoder and decoder
import json

# JSON string
emp = '{"id":"09", "name": "Nitin", "department":"Finance"}'
print("This is JSON", type(emp))

print("\nNow convert from JSON to Python")

# Convert string to Python dict
d = json.loads(emp)
print("Converted to Python", type(d))
print(d)

# JSON string
d = {'id': '09', 'name': 'Nitin', 'department': 'Finance'}
print("This is Python", type(d))

print("\nNow Convert from Python to JSON")

# Convert Python dict to JSON
obj = json.dumps(d, indent=4)
print("Converted to JSON", type(obj))
print(obj)

# mailbox -> manipulate mailboxes in various formats
import mailbox

# mimetypes -> map filenames to MIME types
import mimetypes
mimetypes.init()
mimetypes.knownfiles
mimetypes.suffix_map['.tgz']
mimetypes.encodings_map['.gz']
mimetypes.types_map['.tgz']

# base64, binhex, binascii, quopri, uu -> encode/decode files or streams with various encodings

# html.parser, html.entities -> parse HTML and XHTML
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

# xml.parsers.expat, xml.dom, xml.sax, sml.etree.ElementTree - > various parser and tools for XMLs

# wsgiref -> WSGI utilities and reference implementation 

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]
    return ret

with make_server('', 8000, simple_app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()

# urllib.request, urllib.parse -> open and parse URLs

# ftplib, poplib, imaplib, nntplib, smtplib, telnetlib -> clients for various internet protocols

# socketserver -> framework for network serves 
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        pieces = [b'']
        total = 0
        while b'\n' not in pieces[-1] and total < 10_000:
            pieces.append(self.request.recv(2000))
            total += len(pieces[-1])
        self.data = b''.join(pieces)
        print(f"Received from {self.client_address[0]}:")
        print(self.data.decode("utf-8"))
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())
        # after we return, the socket will be closed.

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

# http.server -> HTTP servers
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

# xmlrpc.client, xmlrpc.server -> XML-RPC client and server