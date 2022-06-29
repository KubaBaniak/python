def logowanie(plik):
    def dekorator(f):
        def nowa(*args):
            with open(plik, 'a') as f:
                f.write('Wlasnie dodalem {} z funkcji {}'.format(args, f.__name__))
            return f(*args)
        return nowa
    return dekorator


# w ksiazce jest ladnie wytlumaczone