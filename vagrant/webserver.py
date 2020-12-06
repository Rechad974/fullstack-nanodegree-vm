from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

class webserverHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    try:
      if self.path.endswith("/hello"):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        output = ""
        output += "<html><body>Hello!"
        output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>"
        output += "</body></html>"

        self.wfile.write(output)
        print(output)
        return
      if self.path.endswith("/hola"):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        output = ""
        output += "<html><body>Hola! <a href='/hello'>Go back</a>"
        output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>"
        output += "</body></html>"

        self.wfile.write(output)
        print(output)
        return

    except IOError:
      self.send_error(404, "File not found {}".format(self.path))

  def do_POST(self):
    try:
      self.send_response(301)
      self.end_headers()

      ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
      ## Check if data received is part of a form
      if ctype == 'multipart/form-data':
        ## Collect fields in the form
        fields = cgi.parse_multipart(self.rfile, pdict)
        messagecontent = fields.get('message')
    
        output = ""
        output += "<html><body>"
        output += "<h2>Okay, how about this: </h2>"
        output += "<h2>{}</h2>".format(messagecontent[0])

        output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>"
        output += "</body></html>"
        self.wfile.write(output)
        print(output)
    except:
      pass

def main():
  try:
    port = 8080
    server = HTTPServer(('', port), webserverHandler)
    print("Webserver is running on port %s", port)
    server.serve_forever()
  except KeyboardInterrupt:
    print("^C entered, stopping web server ...")
    server.socket.close()

if __name__ == '__main__':
  main()