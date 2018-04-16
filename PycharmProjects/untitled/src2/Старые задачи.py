'''
a = list(map(int, input().split()))
b = int(input())
for i in range(b, len(a) - 1):
    a[i] = a[i + 1]
c = a.pop()
for j in range(0, len(a)):
    print(a[j], end=' ')
ближайшее число
m = []
k = int(input())
a = list(map(int, input().split()))
b = int(input())
for i in range(0, len(a)):
    m.append(abs(b - a[i]))
print(a[m.index(min(m))])

a = list(map(int, input().split())) + [0, ]
b = int(input())
c = 1
for i in range(0, len(a)):
    if a[i] < b:
        print(c)
        break
    c += 1

a = list(map(int, input().split()))
b = 0
for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        b += 1
print(b + 1)

a = list(map(int, input().split()))
for i in range(1, len(a), 2):
    a[i], a[i - 1] = a[i - 1], a[i]
for j in range(0, len(a)):
    print(a[j], end=' ')

a = list(map(int, input().split()))
b = a[len(a) - 1]
for i in range(1, len(a)):
    a[len(a) - i] = a[len(a) - i - 1]
a[0] = b
for j in range(0, len(a)):
    print(a[j], end=' ')

d
ef minium(a):
    m = 0
    for i in range(0, len(a)):
        if a[i] < m:
            m = a[i]
    return m


def maxium(a):
    m = 0
    for i in range(0, len(a)):
        if a[i] > m:
            m = a[i]
    return m


a = list(map(int, input().split()))
a[a.index(min(a))], a[a.index(max(a))] = a[a.index(min(a))], a[a.index(max(a))]
for i in range(0, len(a)):
    print(a[i], end=' ')

a = list(map(int, input().split()))
min1 = min(a)
max1 = max(a)
a.remove(min1)
a.remove(max1)
min2 = min(a)
max2 = max(a)
if len(a) > 1:
    a.remove(max2)
    max3 = max(a)
    if min1 * min2 * max1 > max1 * max2 * max3:
        print(max1, min2, min1)
    else:
        print(max1, max2, max3)
else:
    print(max1, max2, min1)


a = list(map(int, input().split()))
cnt = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        if a[i] == a[j]:
            cnt += 1
print((cnt - len(a)) // 2)

a = list(map(int, input().split()))
b = []
for i in range(0, len(a) - 1):
    cnt = 0
    for j in range(0, len(a)):
        if a[i] == a[j]:
            cnt += 1
        if cnt == 2:
            break
    else:
        b.append(a[i])
for k in range(0, len(b)):
    print(b[k], end=' ')

a = list(map(int, input().split()))
b = []
for i in range(1, a[0] + 1):
    b.append('I')
for j in range(0, a[1]):
    c = list(map(int, input().split()))
    for k in range(c[0] - 1, c[1]):
        b[k] = '.'
for l in range(0, len(b)):
    print(b[l], end='')



_|1|2|3|4|5|6|7|8|_
8| |#| |#| |#| |#|8
7|#| |#| |#| |#| |7
6| |#| |#| |#| |#|6
5|#| |#| |#| |#| |5
4| |#| |#| |#| |#|4
3|#| |#| |#| |#| |3
2| |#| |#| |#| |#|2
1|#| |#| |#| |#| |1
 |1|2|3|4|5|6|7|8|

a = []
cnt = 0
for i in range(0, 8):
    a.append(list(map(int, input().split())))
for i in range(0, 8):
    for j in range(i + 1, 8):
        if a[i][0] == a[j][0] or a[i][1] == a[j][1]:
            cnt += 1
            break
        if a[i][0] + a[i][1] == a[j][0] + a[j][1]:
            cnt += 1
            break
if cnt == 0:
    print('NO')
else:
    print('YES')

a = list(map(int, input().split()))
cnt = 0
for i in range(0, len(a)):
    if a[i] != 0:
        a[cnt] = a[i]
        cnt += 1
for j in range(cnt, len(a)):
    a[j] = 0
for k in range(0, len(a)):
    print(a[k], end=' ')

a = list(map(int, input().split()))
cnt1 = 0
chis = 0
for i in range(0, len(a)):
    cnt = 0
    for j in range(0, len(a)):
        if a[i] == a[j]:
            cnt += 1
    if cnt > cnt1:
        chis = a[i]
        cnt1 = cnt
print(chis)

a = list(map(int, input().split()))
mn = min(a)
mx = max(a)
a1 = a.index(mx)
a2 = a.index(mn)
a[a1] = mn
a[a2] = mx
for i in range(0, len(a)):
    print(a[i], end=' ')


№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
№№№№№№№№№№№№№№№№№№№№№№ ЗАДАЧА ДЛЯ ЗАОЧНОЙ ШКОЛЫ №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
coll = int(input())
s = 0
for i in range(0, coll):
    n = int(input(1))
    if n % 10 == 4 and n % 3 == 0:
        s += n
print(s)
№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

n = int(input()) * 0
a = sorted(list(map(int, input().split())), reverse=False)
for j in range(0, len(a)):
    print(a[j], end=' ')

    while x < 25 and y > 1:
        x += 1
        y -= 1
        if x < 25 and y > 1:
            s.move(y, x)
            s.addstr('O')
            s.refresh()
            time.sleep(0.1)
            s.move(y, x)
            s.addstr(' ')
            s.refresh()
    if x == 59:
        while x > 1 and y > 1:
            x -= 1
            y -= 1
            s.move(y, x)
            s.addstr('O')
            s.refresh()
            time.sleep(0.1)
            s.move(y, x)
            s.addstr(' ')
            s.refresh()
    else:
        while x < 59 and y < 23:
            x += 1
            y += 1
            s.move(y, x)
            s.addstr('O')
            s.refresh()
            time.sleep(0.1)
            s.move(y, x)
            s.addstr(' ')
            s.refresh()
    time.sleep(5)




'''


