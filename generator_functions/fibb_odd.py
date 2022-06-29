from fibb_gen import fibb

def fibb_sq(n):
    for i in fibb(n):
        if i % 2:
            yield i


test = fibb_sq(100)

for i in test:
    print(i)