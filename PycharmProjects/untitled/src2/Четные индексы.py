
import curses
import time
'''
cnt = 0
n = int(input())
a = list(map(int, input().split()))
for i in range(0, len(a)):
    if a[i] >= n:
        for j in range(i, len(a) - 1):
            if a[j + 1] - a[j] >= 3:
                cnt += 1
    break
print(cnt + 1)
'''

def aaa(s, x, y):
    while x < 59 and y > 0:
        x += 1
        y -= 1
        if x < 59 and y > 1:
            s.move(y, x)
            s.addstr('O')
            s.refresh()
            time.sleep(0.03)
            s.move(y, x)
            s.addstr(' ')
            s.refresh()
    if x == 59:
        ddd(s, x, y)
    else:
        bbb(s, x, y)


def bbb(s, x, y):
    while x < 59 and y < 23:
        x += 1
        y += 1
        s.move(y, x)
        s.addstr('O')
        s.refresh()
        time.sleep(0.03)
        s.move(y, x)
        s.addstr(' ')
        s.refresh()
    if x == 59:
        ccc(s, x, y)
    else:
        aaa(s, x, y)


def ccc(s, x, y):
    while x > 1 and y < 23:
        x -= 1
        y += 1
        s.move(y, x)
        s.addstr('O')
        s.refresh()
        time.sleep(0.03)
        s.move(y, x)
        s.addstr(' ')
        s.refresh()
    if x == 1:
        bbb(s, x, y)
    else:
        ddd(s, x, y)


def ddd(s, x, y):
    while x > 1 and y > 1:
        x -= 1
        y -= 1
        s.move(y, x)
        s.addstr('O')
        s.refresh()
        time.sleep(0.03)
        s.move(y, x)
        s.addstr(' ')
        s.refresh()
    if y == 1:
        ccc(s, x, y)
    else:
        aaa(s, x, y)

def main(s):
    curses.curs_set(0)
    for j in range(61):
        s.move(0, j)
        s.addstr('#')
        s.move(24, j)
        s.addstr('#')
    for i in range(1, 24):
        s.move(i, 0)
        s.addstr('#')
        s.move(i, 60)
        s.addstr('#')
    s.refresh()
    y = 23
    x = 1
    s.move(y, x)
    s.addstr('O')
    s.refresh()
    s.move(y, x)
    s.addstr(' ')
    s.refresh()
    while x < 59 and y > 1:
        x += 1
        y -= 1
        s.move(y, x)
        s.addstr('O')
        s.refresh()
        time.sleep(0.1)
        s.move(y, x)
        s.addstr(' ')
        s.refresh()
    aaa(s, x, y)


if __name__ == '__main__':
    curses.wrapper(main)
