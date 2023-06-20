# from socket import *
#
# host = '192.168.0.107'
# port = 33443
# addr = (host, port)
#
# tcp_socket = socket(AF_INET, SOCK_STREAM)
# tcp_socket.connect(addr)
#
# data = input('input: ')
# if not data:
#     tcp_socket.close()
#
# data = str.encode(data)
# tcp_socket.send(data)
# # data = bytes.decode(data)
# # data = tcp_socket.recv(1024)
# # print(data)
#
# tcp_socket.close()
