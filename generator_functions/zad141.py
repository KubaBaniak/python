from datetime import datetime
from time import sleep

def last_call():
    i = 0
    while i < 5:
        yield datetime.now()
        i += 1


test = last_call()

for i in test:
    sleep(2)
    print(i)