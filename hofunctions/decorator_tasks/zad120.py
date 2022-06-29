def fibb():
    def wew():
        wew.a, wew.b = wew.b, wew.b + wew.a
        return wew.a
    wew.a = 0
    wew.b = 1
    return wew

f = fibb()
print([f() for _ in range(15)])