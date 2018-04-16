def factorial(a):
    if a > 1:
        return a * factorial(a - 1)
    else:
        return a


m = 0
for n in range(1, int(input()) + 1):
    m = m + factorial(n)
print(m)
