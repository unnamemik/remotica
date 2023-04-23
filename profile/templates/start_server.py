import pickle
import socket
import threading
import queue

# We'll pickle a list of numbers, yet again:
someList = [1, 2, 7, 9, 0]
pickledList = pickle.dumps(someList)

#A revised version of our thread class:
def start_server(request):
    some_data = (b"Connected to server")

    class ClientThread(threading.Thread):
        print('Start server...')

    # Note that we do not override Thread's __init__ method.
    # The Queue module makes this not necessary.

        def run(self):
            # Have our thread serve "forever":
            while True:
                # Get a client out of the queue
                client = clientPool.get()

                # Check if we actually have an actual client in the client variable:
                if client != None:
                    print('Received connection:', client[1][0])

                    client[0].send(some_data)
                    print(some_data)
                    for x in range(10):
                        data = client[0].recv(1024)
                        print(data)
                        client[0].send(data.upper())
                    #client[0].close()
                    print('Closed connection:', client[1][0])

    # Create our Queue:
    clientPool = queue.Queue()

    # Start two threads:
    for x in range(2):
        ClientThread().start()
    # Set up the server:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 33444))
    server.listen(5)

    # Have the server serve "forever":
    while True:
        clientPool.put(server.accept())





# import pickle
# import socket
#
# from django.shortcuts import render
# import threading
#
#
# def start_server(request):
#     some_data = (b"Connected to server")
#
#     class ClientThread(threading.Thread):
#         print('Start server...')
#
#         def __init__(self, channel, details):
#             self.channel = channel
#             self.details = details
#             threading.Thread.__init__(self)
#
#         def run(self):
#             print('Received connection:', self.details[0])
#             self.channel.send(some_data)
#             print(some_data)
#             for x in range(10):
#                 data = self.channel.recv(1024)
#                 print(data)
#                 channel.send(data.upper())
#             #self.channel.close()
#             print('Closed connection:', self.details[0])
#
#     # Set up the server:
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind(('', 33444))
#     server.listen(5)
#
#     # Have the server serve "forever":
#     while True:
#         channel, details = server.accept()
#         ClientThread(channel, details).start()
