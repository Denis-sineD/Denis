a = int(input())
b = int(input())
for c in range(a, b):
    if (c // 1000) * 10 + c % 1000 // 100 == (c % 100) // 10 + c % 10 * 10:
        print(c)
