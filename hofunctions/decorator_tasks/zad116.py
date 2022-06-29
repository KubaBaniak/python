from inspect import signature
from functools import wraps

def typowanie(warunek):
    def dekorator(f):
        def nowa(*args):
            if warunek(tuple(map(type, args))):
                return f(*args)
            else:
                raise TypeError
        return nowa
    return dekorator

def typowanie_z_annotacji(f):
    par = signature(f).parameters
    print(par)
    @wraps(f)
    def wew(*args):
        for war, p in zip(args, par.keys()):
            if type(a:=par[p].annotation) == type and type(war) != a:
                raise TypeError
        return f(*args)
    return wew

@typowanie(lambda x:all([i in (int, float) for i in x]))
def funkcja(x, y):
    return x**2+y**2

@typowanie_z_annotacji
def f2(x:int):
    return x**2

# print(funkcja(1, 2.0))
# print(funkcja(1j, 1j))
print(f2(5))
print(f2(1.2))