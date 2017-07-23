''' Server script, enabling an http server in a directory '''
import http.server
import socketserver
import sys
import threading
from ..console import colors

class ConColors:
    Blue = "\033[94m"
    Yellow = "\033[93m"
    Green = "\033[92m"
    Red = "\033[91m"
    Default = "\033[0m"

class Handler(http.server.SimpleHTTPRequestHandler):
    ''' Wrapper for http server handler '''
    def log_message(self, _format, *args):
        return

def main():
    ''' Program Entry Point '''
    _host = sys.argv[1]
    _port = int(sys.argv[2])
    server_thread = threading.Thread(target=start_server, args=(_host, _port))
    server_thread.daemon = True
    server_thread.start()
    while True:
        result = input("")
        if result:
            if "exit" in result:
                sys.exit(1)
            else:
                print(ConColors.Red + "Unrecognized command"+ ConColors.Default)


def start_server(_host, _port):
    ''' Server Thread '''
    try:
        handler = Handler
        with socketserver.TCPServer((_host, _port), handler) as httpd:
            print("Starting server:")
            print("    host: " + sys.argv[1])
            print("    port: " + sys.argv[2])
            httpd.serve_forever()
    except (PermissionError):
        print("Could not load server due to a permission error")


if __name__ == "__main__":
    main()
