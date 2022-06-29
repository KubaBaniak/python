from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time


class Client:
    
    HOST = 'localhost'
    PORT = 5500
    ADDR = (HOST, PORT)
    BUFISZ = 512    
    
    def __init__(self, name):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.messages = list()


    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.revc(self.BUFISZ).decode('utf8')
                print(msg)
            except Exception as e:
                print(e)
                break

    def send_message(self, msg):
        self.client_socket.send(bytes(msg, 'utf8'))
        if msg == '{quit}':
            self.client_socket.close()
