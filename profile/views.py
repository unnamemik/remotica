from socket import *

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def commands(request, com):
    host = '192.168.0.107'
    port = 33443
    addr = (host, port)

    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(addr)

    data = com
    if not data:
        tcp_socket.close()

    data = str.encode(data)
    tcp_socket.send(data)
    # data = bytes.decode(data)
    # data = tcp_socket.recv(1024)
    # print(data)

    tcp_socket.close()
    return HttpResponse(f'Command = {com}')