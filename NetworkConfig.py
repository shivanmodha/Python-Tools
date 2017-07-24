''' Script query a devices network details '''
import socket

def ipaddress():
    ''' Return IP Address '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    __return = sock.getsockname()[0]
    sock.close()
    return __return

def hostname():
    ''' Return Host Name '''
    return socket.gethostname()
