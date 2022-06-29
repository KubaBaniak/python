from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time

HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
BUFISZ = 512

messages = []

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

