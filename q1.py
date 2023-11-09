from socketserver

class MyRequestHandler(socketsever.StreamRequestHandler):
    def handle(self):
        self.wfile.write("%s" % self.rfile.read().decode().encode())

sever = socketsever.TCPServer(("",8888), MyRequestHandler)
sever.close()
