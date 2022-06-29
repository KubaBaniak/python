def srednia():
    def wew(x):
        try:
            wew.s += x
            wew.n += 1
        except:
            pass
        return wew.s / wew.n
    wew.s = 0
    wew.n = 0
    def reset():
        wew.s = 0
        wew.n = 0
    wew.reset = reset
    return wew 

s = srednia()

print([s(i) for i in [5, 3, 3, 2, 1, 6, 7, 4]])
s.reset()
print([s(i) for i in [4, 2, 0]])