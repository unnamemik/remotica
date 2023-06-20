from socketserver import *

from service.server_const import sender_host, sender_port

addr = (sender_host, sender_port)
global server


class MyTCPHandler(StreamRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print('client sent: ' + str(self.data))
        with open("exchange", "r") as file:
            replay_data = file.read()[2:-1]
            print("send: ", replay_data)
            self.request.sendall(replay_data.encode())

    @staticmethod
    def server_stop():
        server.server_close()
        server.shutdown()


def starter():
    global server
    try:
        server = TCPServer(addr, MyTCPHandler)
        print('sender started...')
        server.serve_forever()
    except:
        print('sender restarted!')


if __name__ == "__main__":
    starter()
