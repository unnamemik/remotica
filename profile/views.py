from socket import *

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from service.server_const import client_host, client_port
from service.server_starter import server_starter



# Create your views here.

@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def commands(request, com):
    #######################################
    server_starter()
    addr = (client_host, client_port)
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(addr)

    data = com
    if not data:
        tcp_socket.close()

    data = str.encode(data)
    tcp_socket.send(data)

    tcp_socket.close()
    # ########################################
    return HttpResponse(f'Command = {com}')