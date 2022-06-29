from fibb_gen import fibb

def fibb_sq(n):
    for i in fibb(n):
        yield i ** 2


test = fibb_sq(100)

for i in test:
    print(i)