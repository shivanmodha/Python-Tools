''' Server script, enabling an http server in a directory '''
import http.server
import socketserver
import sys
import threading
import os
import ConColors
import NetworkConfig

PARAMETERS = {"HOST": NetworkConfig.ipaddress(), "PORT": "4000",
              "DIR": os.path.dirname(os.path.realpath(__file__)),
              "SERVER_THREAD": None, "HANDLER": None,
              "HTTPD": socketserver.TCPServer}

class Handler(http.server.SimpleHTTPRequestHandler):
    ''' Wrapper for http server handler '''
    def log_message(self, _format, *args):
        return

class StatusThread(threading.Thread):
    ''' Thread wrapper class that includes kill functionality '''
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None):
        super(StatusThread, self).__init__()
        self.statusevent = threading.Event()
    def run(self):
        if self._target:
            self._target(*self._args, **self._kwargs)
    def stop(self):
        ''' kill thread '''
        self.statusevent.set()
    def stopped(self):
        ''' Query thread status '''
        return self.statusevent.is_set()

def parse_args(_argin):
    ''' parse_args '''
    if _argin.startswith("--"):
        try:
            function_handle = getattr(sys.modules[__name__], _argin[2:])
            return function_handle
        except AttributeError:
            print(ConColors.RED + "Unknown Command: " + ConColors.BLACK + _argin[2:])
            return "ERR"
    else:
        return "params"

def parse_line(_arguments):
    ''' parse_line '''
    function = main
    parameters = []
    for i in range(0, len(_arguments)):
        _obj = parse_args(_arguments[i])
        if _obj != "params" and _obj != "ERR" and _arguments[i] != "--parse_line":
            execute(function, parameters)
            function = _obj
            parameters = []
        else:
            parameters.append(_arguments[i])
    execute(function, parameters)

def execute(function, params):
    ''' Execute function with the parameters list '''
    handled = False
    try:
        if function != main:
            if params:
                function(params)
            else:
                try:
                    function()
                except TypeError:
                    handled = True
                    function([])
    except TypeError:
        if not handled:
            print(ConColors.RED + "Error in function " + function.__name__ +\
                  ": Insufficient parameters" + ConColors.BLACK)

def main():
    ''' Program Entry Point '''
    send = []
    if len(sys.argv) >= 1:
        for i in range(1, len(sys.argv)):
            send.append(sys.argv[i])
    parse_line(send)
    show()
    while True:
        result = input(ConColors.YELLOW + "Server: " + ConColors.BLACK)
        if result:
            result = "--" + result
            params = result.split()
            error = False
            for i in range(1, len(params)):
                if i % 2 == 1:
                    if params[i].startswith("--"):
                        params[i] = params[i][2:]
                    else:
                        error = True
                        print(ConColors.RED + "Unknown parameter: " + ConColors.BLACK + params[i])
                else:
                    if params[i].startswith("--"):
                        error = True
                        print(ConColors.RED + "Unknown parameter: " + ConColors.BLACK + params[i])
            if not error:
                parse_line(params)

def show():
    ''' Print out current status of the server '''
    print()
    print("Current Parameters: ")
    print("    Host: " + PARAMETERS["HOST"])
    print("    Port: " + PARAMETERS["PORT"])
    print("     Dir: " + PARAMETERS["DIR"])
    print("Device Parameters: ")
    print("     IP : " + NetworkConfig.ipaddress())
    print("    Name: " + NetworkConfig.hostname())
    print()

def set(params):
    ''' Set dictionary values '''
    for i in range(0, int(len(params) / 2)):
        j = i * 2
        if j + 1 < len(params):
            PARAMETERS[params[j].upper()] = params[j + 1]
            print("Setting " + ConColors.GREEN + params[j].upper() + ConColors.BLACK +\
                  " to " + params[j + 1])

def server(params):
    ''' Server method handler '''
    for param in params:
        if param.upper() == "START":
            print("")
            print(ConColors.GREEN + "Starting Server" + ConColors.BLACK)
            print("    Server: " + ConColors.BLUE + "Initializing Thread" + ConColors.BLACK)
            os.chdir(PARAMETERS["DIR"])
            PARAMETERS["SERVER_THREAD"] = StatusThread()
            PARAMETERS["SERVER_THREAD"]._target = ___start_server
            PARAMETERS["SERVER_THREAD"]._args = (PARAMETERS["HOST"],
                                                 PARAMETERS["PORT"])
            PARAMETERS["SERVER_THREAD"].daemon = True
            print("    Server: " + ConColors.BLUE + "Starting Thread" + ConColors.BLACK)
            PARAMETERS["SERVER_THREAD"].start()
            print("    Server: " + ConColors.GREEN + "Ready" + ConColors.BLACK)
            print("")
        elif param.upper() == "STOP":
            print("")
            print(ConColors.RED + "Stopping Server" + ConColors.BLACK)
            print("    Server: " + ConColors.BLUE + "Shutting down" + ConColors.BLACK)
            PARAMETERS["HTTPD"].shutdown()
            print("    Server: " + ConColors.BLUE + "Ending socket" + ConColors.BLACK)
            PARAMETERS["HTTPD"].socket.close()
            print("    Server: " + ConColors.BLUE + "Ending Thread" + ConColors.BLACK)
            PARAMETERS["SERVER_THREAD"].stop()
            PARAMETERS["SERVER_THREAD"].join()
            print("    Server: " + ConColors.RED + "Stopped" + ConColors.BLACK)
            print("")
def ___start_server(_host, _port):
    ''' Server Start Thread '''
    try:
        PARAMETERS["HANDLER"] = Handler
        with socketserver.TCPServer((_host, int(_port)), PARAMETERS["HANDLER"]) as httpd:
            PARAMETERS["HTTPD"] = httpd
            httpd.serve_forever()
    except PermissionError:
        pass

def exit():
    ''' exit command forwarder '''
    quit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(ConColors.BLUE + "Interruption Detected" + ConColors.BLACK)
