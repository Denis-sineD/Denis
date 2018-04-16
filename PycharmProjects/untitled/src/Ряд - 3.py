n = int(input())
for m in range((10 ** n), (10 ** (n - 1)) - 1, -1):
    if m % 2 == 1:
        print(m, end=' ')
