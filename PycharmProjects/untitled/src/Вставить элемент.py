a = list(map(int, input().split()))
b = a[len(a) - 1]
for i in range(1, len(a)):
    a[len(a) - i] = a[len(a) - i - 1]
a[0] = b
for j in range(0, len(a)):
    print(a[j], end=' ')
