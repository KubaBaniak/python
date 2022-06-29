from re import X


class MK:

    def __init__(self, x):
        self.x = x

    def __enter__(self):
        return 2

    def __exit__(*args):
        print(args[1:])

with MK(5) as f:
    print(f)
    print(2*f)
with MK(5) as f:
    print(f.xx)
