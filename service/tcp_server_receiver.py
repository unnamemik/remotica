from socketserver import *

host = '192.168.0.107'
port = 33443
addr = (host, port)


class MyTCPHandler(StreamRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print('client send: ' + str(self.data))
        with open("exchange", "w") as file:
            file.write(str(self.data))
        with open("exchange", "r") as file:
            print("received: ", file.read())
        self.request.sendall(b'replay')
        # self.server_stop()

    @staticmethod
    def server_stop():
        server.server_close()
        server.shutdown()


if __name__ == "__main__":
    server = TCPServer(addr, MyTCPHandler)
    print('starting server...')
    server.serve_forever()
