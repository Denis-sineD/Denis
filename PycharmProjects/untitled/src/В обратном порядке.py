a = list(map(int, input().split()))
b = a
print(a)
for i in range(1, len(a) + 1):
    b[i - 1] = a[len(a) - i]
b[2] = a[1]
print(b)
