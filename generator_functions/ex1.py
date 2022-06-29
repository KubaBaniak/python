def zakres(n):
    i = 0
    while i < n:
        yield i
        i += 1


test = zakres(5)

for x in test:
    print(x)