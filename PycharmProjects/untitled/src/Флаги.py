a1 = '+___ '
a2 = '|__\\ '
a3 = '|    '
n = int(input())
print(a1 * n)
for a in range(1, n + 1):
    print('|', a, ' /', end=' ', sep='')
print('')
print(a2 * n)
print(a3 * n)
