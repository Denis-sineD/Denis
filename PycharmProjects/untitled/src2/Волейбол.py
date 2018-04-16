#! /usr/bin/env python3

import curses
import time


def main(s):

    curses.curs_set(0)
    for i in range(61):
        s.move(0, i)
        s.addstr('#')
        s.move(24, i)
        s.addstr('#')
    for j in range(1, 24):
        s.move(j, 0)
        s.addstr('#')
        s.move(j, 60)
        s.addstr('#')
    l = 9
    for k in range(l, l + 7):
        s.move(k, 55)
        s.addstr('#')
    y = 23
    x = 1
    s.move(y, x)
    s.addstr('O')
    s.refresh()
    s.move(y, x)
    s.addstr(' ')
    s.refresh()
    n = 1
    m = -1
    while x < 59 and 1 < y and not(x + n == 55 and l - 1 < y + m < l + 7):
        x += n
        y += m
        s.move(y, x)
        s.addstr('O')
        s.refresh()
        time.sleep(0.07)
        s.move(y, x)
        s.addstr(' ')
        s.refresh()
    for infinity in range(24):
        if x == 59:
            s.move(y, x)
            s.addstr('X')
            s.move(12, 30)
            s.addstr('Game over')
            s.refresh()
            time.sleep(3)
            break
        if x == 1 or (x + n == 55 and l - 1 < y + m < l + 7):
            n = -n
        if y == 23 or y == 1:
            m = -m
        x += n
        y += m
        s.move(y, x)
        s.addstr('O')
        s.refresh()
        time.sleep(0.07)
        s.move(y, x)
        s.addstr(' ')
        s.refresh()
        while 1 < x < 59 and 1 < y < 23 and not(x + n == 55 and l - 1 < y + m < l + 7):
            x += n
            y += m
            s.move(y, x)
            s.addstr('O')
            s.refresh()
            time.sleep(1)
            s.move(y, x)
            s.addstr(' ')
            s.refresh()
        c = s.getch()
        for p in range(4):
            if c == 259:
                s.move(l + 6, 55)
                s.addstr(' ')
                if l > 2:
                    l -= 1
                    s.move(l, 55)
                    s.addstr('#')
                    s.refresh()
                    time.sleep(0)
            if c == 258:
                s.move(l - 1, 55)
                s.addstr(' ')
                if l + 6 < 23:
                    l += 1
                    s.move(l + 5, 55)
                    s.addstr('#')
                    time.sleep(0)
                    s.refresh()
    else:
        s.move(12, 30)
        s.addstr('You Won!')
        s.refresh()
        time.sleep(5)
# мячик прыгает в коробке


if __name__ == '__main__':
    curses.wrapper(main)

