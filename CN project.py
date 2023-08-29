#Computer Networks Project
#SWIFT SHARE APP
#EB 13
#By Tarush , Priyanshu and Sarthak
#ENROLLMENT: E21CSEU0974  ---- TARUSH SINGH
#ENROLLMENT: E21CSEU0955  ---- PRIYANSHU SHARMA
#ENROLLMENT: E21CSEU0785  ---- SARTHAK AGRAWAL

# importing necessary modules

import http.server  # implementing the HTTP Web servers
import socket         # provides access to the BSD socket interface
import socketserver # a framework for network servers
import webbrowser  # to display a Web-based documents to users
import pyqrcode    # to generate qrcode
import os        # to access operating system control

PORT = 8010


desktop = os.path.join(os.path.expanduser("~"), "Desktop") # changing the directory to access the files on the desktop with the help of os module

os.chdir(desktop) #now changing the pwd to Desktop of the User

Handler = http.server.SimpleHTTPRequestHandler       # creating a http request

# returns, host name of the system under
# which Python interpreter is executed
hostname = socket.gethostname()

# finding the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = ip


# converting the IP address into the form of a QRcode
# with the help of pyqrcode module
# converts the IP address into a Qrcode
url = pyqrcode.create(link)

# saves the Qrcode inform of svg
url.svg("QRCode.svg", scale=8)

# opens the Qrcode image in the web browser
webbrowser.open('QRCode.svg')

# Creating the HTTP request and serving the
# folder in the PORT 8010,and the pyqrcode is generated
# continuous stream of data between client and server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
   print("serving at port", PORT)
   print("Type this in your Browser", ip)
   print("or Use the QRCode")
   httpd.serve_forever()