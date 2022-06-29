def dekorator(a, b):
    def d(f):
        # print(f(2)) = 4 > funcka podwajajaca

        def wew(x):
            # print(x) = 2 czyli przekazany argument
            print(f)
            print(x)
            y = f(x)
            if y < a:
                y = a
            elif y > b:
                y = b
            return y
        print(wew)
        return wew
    print(d)
    return d


@dekorator(-1, 1)
def f(x):
    return 3 * x


f(2)
