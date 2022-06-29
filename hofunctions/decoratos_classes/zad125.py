def wypisz(c):
    if not hasattr(c, '__str__'):
        def str(self):
            return 'Instancja klasy: {}'.format(self.__class__.__name__)
        c.__str__ = str
    return c
    
@wypisz
class Klasa:
    pass

@wypisz
class Klasa2:
    def __str__(self):
        return 'ok'

k = Klasa()
print(k)
k2 = Klasa2()
print(k2)