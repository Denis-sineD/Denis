a = list(map(int, input().split()))
for i in range(0, len(a)):
    if 0 > a[i]:
        a[i] = 10000
print(min(a))
