# dekoratory jako klasy
class Dekorator1:

    def __call__(self, f):
        def nowa(*args):
            nowa.liczba_wywolan += 1
            return f(*args)
        nowa.liczba_wywolan = 0
        return nowa

class Dekorator2(Dekorator1):

    def __call__(self, f):
        f = super().__call__(f)
        f.ok = 'ok'
        return f

@Dekorator2()
def f():
    return 1

for _ in range(100):
    f()

print(f.liczba_wywolan, f.ok)