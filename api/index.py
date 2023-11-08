
from http.server import BaseHTTPRequestHandler

class CustomHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

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

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), CustomHandler)
    print('Servidor web en ejecución...')
    server.serve_forever()
