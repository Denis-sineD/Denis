a = int(input())
b = int(input())
if a < b:
    for n in range(a, b + 1):
        print(n, end=' ')
else:
    for n in range(a, b - 1, -1):
        print(n, end=' ')
