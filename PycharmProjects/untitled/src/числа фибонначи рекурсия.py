def fib(n):
    b = 1
    c = 1
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        while n >= 0:
            a = b + c
            b, c = a, b
            n = n - 1
        return a


def fib2(m):
    a, b = 1, 0
    while m > 0:
        a, b = a + b, a
        m = m - 1
    return a


print(fib2(int(input())))
