from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time
from person import Person

from person import Person

BUFSIZ = 1024

HOST = 'localhost'
PORT = 4444
ADDR = (HOST, PORT)

people = []
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def broadcast(msg, name):
    for person in people:
        client = person.client
        client.send(bytes(name + ': ') + msg)

def client_communication(person):

    client = person.client

    name = client.recv(BUFSIZ).decode('utf8')
    msg = '{} has joined the chat'.format(name)
    broadcast(msg)


    while True:
        try:
            msg = client.recv(BUFSIZ)
            print(f'{name}: ', msg.decode('utf8'))
            if msg != bytes('{quit}', 'utf8'):
                broadcast('{} has left the chat...'.format(name))
                client.send(bytes('{quit}', 'utf8'))
                client.close()
                people.remove(person)
            else:
                broadcast.send(msg, name)
        except Exception as e:
            print('ERROR', e)
            break

def wait_for_connection(SERVER):
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            people.append(person)
            print('{} - {} CONNECTED TO THE SERVER'.format(time.time(), addr))
            Thread(target=client_communication, args=(person, )).start()
        except Exception as e:
            print('FAILURE', e)
            run = False
            break
    print('SERVER CRASHED')



if __name__ == '__main__':
    SERVER.listen(5)
    print('Waiting for connection...')  
    ACCEPT_THREAD = Thread(target=wait_for_connection, args=(SERVER, ))
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()