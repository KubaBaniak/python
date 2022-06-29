# zle
# l = [lambda x: x**i for i in range(1, 21)]
# print([f(2) for f in l])
# to samo
# def f(x):
#     return x**i

# dobrze 
# l = [lambda x, i=i: x**i for i in range(1, 21)]
# print([f(2) for f in l])

def exp():
    return [lambda x, i=i: x**i for i in range(20)]

print([f(2) for f in exp()])