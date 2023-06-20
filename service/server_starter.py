from threading import Thread
from time import sleep

from service import tcp_server_receiver, tcp_server_sender


class Thr1(Thread):
    def run(self):
        Thread(target=tcp_server_receiver.starter())


class Thr2(Thread):
    def run(self):
        Thread(target=tcp_server_sender.starter())


def starter():
    Thr1().start()
    Thr2().start()


def server_starter():
    if not Thr1().is_alive() or not Thr2().is_alive():
        starter()
    else:
        print("Server stopped")
        sleep(5)