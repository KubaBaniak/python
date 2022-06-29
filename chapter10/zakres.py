from re import L
from pandas import to_datetime


class Zakres:

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.n:
            raise StopIteration
        r=self.i
        self.i += 1
        return r

for i in Zakres(4):
    print(i)

    # albo zamiast tych 2 metod to
    # def __getitem__(self, i):
    #     if i < self.n:
    #         return i
    #     else:
    #         raise IndexError
        