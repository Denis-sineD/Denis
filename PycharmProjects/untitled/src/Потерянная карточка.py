def factorial(a):
    n = 1
    while a > 0:
        n = n + a
        a = a - 1
    return n


m = 0
i = int(input())
k = i
while i > 1:
    e = int(input())
    m = m + e
    i = i - 1
print(factorial(k) - 1 - m)
