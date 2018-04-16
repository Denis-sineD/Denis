a = list(map(int, input().split()))
min1 = min(a)
max1 = max(a)
a.remove(min1)
a.remove(max1)
min2 = min(a)
max2 = max(a)
if min1 * min2 > max1 * max2:
    print(min1, min2)
else:
    print(max2, max1)
