from socket import SO_REUSEADDR, socket, AF_INET, SOCK_STREAM, SOL_SOCKET
from threading import Thread, Lock
from datetime import datetime
from person import Person


BUFSIZ = 1024

HOST = 'localhost'
PORT = 4444
ADDR = (HOST, PORT)

l = Lock()

people = []
messages = [b'29/06/2022 16:20:01 ada\r\n>test1\r\n',
            b'29/06/2022 16:20:05 bada\r\n>test2\r\n',
            b'29/06/2022 16:20:06 cada\r\n>test3\r\n',
    ]   
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
SERVER.bind(ADDR)

def broadcast(msg, name="", client_to_skip=()):
    for person in people:
        client = person.client
        if client != client_to_skip and person.name is not None:
            client.send(bytes(msg, 'utf8'))

def print_all_users(client):
        for user in people:
            client.send(bytes(f'---{user}\n', 'utf8'))

def client_communication(person):
    global l
    client = person.client
    client.send(bytes('Input your nickname: ', 'utf8'))
    name = client.recv(BUFSIZ).decode('utf8')
    person.set_name(name.upper())

    msg = '%s has joined the chat\n' % person.name

    broadcast(msg, name, client)

    for message in messages:
        client.send(message + b'\n')

    while True:
        try:
            msg = client.recv(BUFSIZ)
            text = '{} %s>%s'.format(datetime.now().strftime('%d/%m/%Y %H:%M:%S')) %(person.name, msg.decode('utf-8'))

            if msg.decode('utf-8').replace('\r\n', '') == 'quit':
                broadcast('{} has left the chat...\n'.format(person.name), client)
                client.send(bytes('quit', 'utf8'))
                client.close()
                people.remove(person)

            elif msg.decode('utf-8').replace('\r\n', '') == '$all':
                print_all_users(client)

            else:
                messages.append(bytes(text, 'utf8'))
                broadcast(text, name, client)
                print(messages)

        except Exception as e:
            print('ERROR', e)
            break



def wait_for_connection(SERVER):
    global l
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            with l:
                people.append(person)
                print('{} - {} CONNECTED TO THE SERVER'.format(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), addr))
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