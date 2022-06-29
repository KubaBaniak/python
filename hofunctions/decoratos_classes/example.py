def dekorator_ok(c):
    def ok(self):
        return 'OK'
    c.ok = ok
    return c

@dekorator_ok
class Klasa:
    pass

k = Klasa()
print(k.ok())