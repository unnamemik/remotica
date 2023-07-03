from socketserver import *

from service.server_const import sender_host, sender_port

addr = (sender_host, sender_port)
global send_server


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
        send_server.server_close()
        send_server.shutdown()


def starter():
    global send_server
    try:
        send_server = TCPServer(addr, MyTCPHandler)
        print('sender started...')
        send_server.serve_forever()
    except:
        print('sender restarted!')


if __name__ == "__main__":
    starter()
