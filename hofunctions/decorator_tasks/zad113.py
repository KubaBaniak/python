from functools import wraps
import numpy as np
import matplotlib.pyplot as plt

def dekorator(*args):
    print(args)
    if callable(args[0]):
        a = -1
        b = 1
        f = args[0]
        @wraps(f)
        def wew(x):
            y = f(x)
            if y < a:
                y = a
            elif y > b:
                y = b
            return y
        return wew
    else:
        if len(args) == 2:
            a, b = args
        else:
            a = -args[0]
            b = args[0]
        def d(f):
            @wraps(f)
            def wew(x):
                y = f(x)
                if y < a:
                    y = a
                elif y > b:
                    y = b
                return y
            return wew
        return d

def pochodna(f):
    if callable(f):
        dx = 1e-5
        @wraps(f)
        def nowa(x):
            return (f(x+dx) - f(x))/dx
        return nowa
    else:
        dx = f
        print(f) #to co ile ma liczyc punkt
        def d(f):
            # tutaj f to juz podana funkcja (d(def f():....))
            @wraps(f)
            def nowa(x):
                return (f(x+dx) - f(x))/dx
            return nowa
        return d



@dekorator
@pochodna(1e-10)
def f1(x):
    return x**2

@pochodna
@dekorator
def f2(x):
    return x**2

X = np.linspace(-2, 2, 401)
plt.plot(X, list(map(f1, X)))
plt.plot(X, list(map(f2, X)))
plt.show()