from fibb_gen import fibb

fibb_sq1 = (f ** 2 for f in fibb(5))
fibb_sq2 = map(lambda x: x ** 2, fibb(5))
fibb_sq3 = map((2).__rpow__, fibb(5))

test = fibb_sq3

for i in test:
    print(i)