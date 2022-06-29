def numer(f):
    # dodaje do lacznej liczby udekorowanych przez ten dekorator funkcji i przypisuje jej ktora to udekorowana funkcja
    numer.liczba_udekorowanych += 1
    f.numer = numer.liczba_udekorowanych
    return f
numer.liczba_udekorowanych = 0

@numer
def f1(x):
    return 1

@numer
def f2(x):
    return x

@numer
def f2(x):
    return x

@numer
def f3(x):
    return x



print(f1.numer)
print(f2.numer)
print(f3.numer)