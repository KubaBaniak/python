from re import X


def dekorator(a, b):
    # tworzy i zwraca dekorator, ktory zdeklarowalem w kodzie (w tym przypadku to @dekorator(-1, 1))
    def d(f):
    # f do funkcja zdeklarowana pod dekoratorem
    # wew() to funkcja, która zostala zainicjalizowana pod dekoratorem
        def wew(x):
            print(f)
            print(x)
            y = f(x)
            if y < a:
                y = a
            elif y > b:
                y = b
            return y  # zwracamy wartość z udekorowanej (użytej) funkcji

        return wew   # zwracany udekorowaną funkcję

    return d    # zwracamy stworzony dekorator

# dekorator normalnie dawał od def d(f) fo return wew z a = 1 i b = -1, ale ten w dodatkowej funkcji modyfikuję wcześniejszą funkcję i ją zwraca


@dekorator(-1, 1)
def f(x):
    return 3 * x

# 24 linika to tak jakbym napisal d(def f(x): return 3*x )

f(2)                   
