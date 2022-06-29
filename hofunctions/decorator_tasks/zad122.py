from datetime import datetime
from time import sleep
def czas(f):
    def nowa(*args):
        nowa.czas = datetime.now()
        return f(args)
    nowa.czas = datetime.now()
    return nowa

@czas
def f1(x):
    return list(map(lambda num: num * 2, x))

s = f1

print(s(4, 2, 3, 6), s.czas)
sleep(3)
print(s(3), s.czas)