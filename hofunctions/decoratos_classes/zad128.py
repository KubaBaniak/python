def negacja(c):
    if not hasattr(c, '__neg__'):
        def __neg__(self):
            return self-self-self
        c.__neg__ = __neg__
    return c

@negacja
class Klasa():
    pass


k = Klasa()
print(-k(5))