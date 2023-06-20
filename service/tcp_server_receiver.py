from socketserver import *

from service.server_const import receiver_host, receiver_port

addr = (receiver_host, receiver_port)
global server


class MyTCPHandler(StreamRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print('client send: ' + str(self.data))
        with open("exchange", "w") as file:
            file.write(str(self.data))
        with open("exchange", "r") as file:
            print("received: ", file.read())
        self.request.sendall(b'replay')

    def server_stop(self):
        server.server_close()
        server.shutdown()


def starter():
    global server
    try:
        server = TCPServer(addr, MyTCPHandler)
        print('receiver started...')
        server.serve_forever()
    except:
        print('receiver restarted!')


if __name__ == "__main__":
    starter()
