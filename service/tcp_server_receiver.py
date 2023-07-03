from socketserver import *

from service.server_const import receiver_host, receiver_port

addr = (receiver_host, receiver_port)
global rec_server


class MyTCPHandler(StreamRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print('client send: ' + str(self.data))
        with open("exchange", "w") as file:
            file.write(str(self.data))
        with open("exchange", "r") as file:
            print("received: ", file.read())
        # self.request.sendall(b'replay')

    def server_stop(self):
        rec_server.server_close()
        rec_server.shutdown()


def starter():
    global rec_server
    try:
        rec_server = TCPServer(addr, MyTCPHandler)
        print('receiver started...')
        rec_server.serve_forever()
    except:
        print('receiver restarted!')


if __name__ == "__main__":
    starter()
