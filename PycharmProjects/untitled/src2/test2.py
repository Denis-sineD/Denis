import curses
import time


def aaa(s, x, y):
    while s.move(y - 1, x) != '#' and s.move(y, x + 1) != '#':
        x += 1
        y -= 1
        if s.move(y - 1, x) != '#' and s.move(y, x + 1) != '#':
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
    while s.move(y + 1, x) != '#' and s.move(y, x + 1) != '#':
        x += 1
        y += 1
        if s.move(y + 1, x) != '#' and s.move(y, x + 1) != '#':
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
    while s.move(y + 1, x) != '#' and s.move(y, x - 1) != '#':
        x -= 1
        y += 1
        if s.move(y + 1, x) != '#' and s.move(y, x - 1) != '#':
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
    while s.move(y - 1, x) != '#' and s.move(y, x - 1) != '#':
        x -= 1
        y -= 1
        if s.move(y - 1, x) != '#' and s.move(y, x - 1) != '#':
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
