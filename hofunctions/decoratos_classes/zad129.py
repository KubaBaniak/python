# def power(x, n):
#     if x == 1:
#         return x
#     if (n < 1):
#         return x/power(x, -n+1)
#     if n % 2:
#         a = power(x, (n-1)/2)
#         return x * a*a
#     a = power(x, n/2)
#     return a*a

def potegowanie(c):
    if not hasattr(c, '__pow__'):
        def power(x, n):
            if x == 1:
                return x
            if (n < 1):
                return x/power(x, -n+1)
            if n % 2:
                a = power(x, (n-1)/2)
                return x * a*a
            a = power(x, n/2)
            return a*a
        c.__pow__ = power
    return c