

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('404'.encode('utf-8'))
        





        # HTML que muestra una imagen centrada y un encabezado h1
        response_content = """
        <html>
        <head>
            <title>Under Construction</title>
        </head>
        <body style="text-align: center;">
            <h1 style="color: #333;">This site is under construction</h1>
            <img src="404.png" alt="404" style="display: block; margin: 0 auto;">
        </body>
        </html>
        """

        self.wfile.write(response_content.encode('utf-8'))
        return
