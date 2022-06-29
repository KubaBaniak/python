from time import sleep, time
from random import randrange


class LastTime:

    def __init__(self):
        self.t = time()

    def __iter__(self):
        return self

    def __next__(self):
        t = time()
        self.t, t = t, t-self.t
        return t
            
T = LastTime()
for i in range(10):
    print(next(T))
    sleep(randrange(3))
            