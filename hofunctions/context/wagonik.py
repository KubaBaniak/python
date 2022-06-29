from threading import Thread

class Wagonik:

    def __init__(self):
        self.liczba_pasazerow = 0

    def __enter__(self):
        if self.liczba_pasazerow >=3:
            raise ValueError('Wagonik już odjechał')
        self.liczba_pasazerow += 1
        print('Witamy pasażera! ')
        while self.liczba_pasazerow < 3:
            pass
    
    def __exit__(self, t, e, tb):
        pass 


w = Wagonik()

def f(x):
    with w:
        print('jedziemy')

Thread(target=f, args=('A',)).start()
Thread(target=f, args=('B',)).start()
Thread(target=f, args=('C',)).start()
Thread(target=f, args=('D',)).start()