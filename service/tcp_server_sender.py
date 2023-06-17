from socketserver import *

host = '192.168.0.107'
port = 33444
addr = (host, port)


class MyTCPHandler(StreamRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print('client sent: ' + str(self.data))
        with open("exchange", "r") as file:
            replay_data = file.read()[2:-1]
            print("send: ", replay_data)
            self.request.sendall(replay_data.encode())
            # self.server_stop()

    @staticmethod
    def server_stop():
        server.server_close()
        server.shutdown()


if __name__ == "__main__":
    server = TCPServer(addr, MyTCPHandler)

    print('starting server...')
    server.serve_forever()
