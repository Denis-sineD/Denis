#! /usr/bin/env python3
#import random

import curses
import time
'''

def main(s):
    s.nodelay(1)
    curses.curs_set(0)
    for i in range(61):  # началопечатаниярамки
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
    l = 9# конецпечатаниярамки
    y = 12  # random.randint(2, 30)
    x = 30
    s.move(y, x)  # размещаюшарик
    s.addstr('O')
    n = 1
    m = -1
    t = time.time()
    while 2 < 3:
        c = s.getch()
        if time.time() - t >= 0.7:
            if 1 < x < 59 and 1 < y < 23 and not(x + n == 55 and l - 1 < y + m < l + 7):
                if x == 59:  # еслимячиккоснулсяворот
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

                t = time.time()
                x += n
                y += m
                s.move(y, x)
                s.addstr('O')
                s.refresh()
        if x == 59:  # еслимячиккоснулсяворот
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
        if c == 259:
            if l > 1:
                s.move(y - m, x - n)
                s.addstr(' ')
                s.refresh()
                s.move(y, x)
                s.addstr(' ')
                s.refresh()
                s.move(l + 6, 55)
                s.addstr(' ')
                l -= 1
                s.move(l, 55)
                s.addstr('#')
                s.refresh()
        if c == 258:
            if l + 6 < 23:
                s.move(l, 55)
                s.addstr(' ')
                l += 1
                s.move(l + 6, 55)
                s.addstr('#')
                s.refresh()
    else:
        s.move(12, 30)
        s.addstr('You Won!')
        s.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
'''

# ! /usr/bin/env python3


import curses
import time


"""
    LEFT
TOP ####
    #  #
    #### BOTTOM
       RIGHT

WIDTH
STEP

"""
'''
LEFT = 1
RIGHT = 30
TOP = 1
BOTTOM = 12
WIDTH = 5
STEP = 3


def main(s):
    s.nodelay(1)
    curses.curs_set(0)
    for i in range(LEFT - 1, RIGHT + 2):
        s.move(TOP - 1, i)
        s.addstr('#')
        s.move(BOTTOM + 1, i)
        s.addstr('#')
    for j in range(TOP - 1, BOTTOM + 1):
        s.move(j, LEFT - 1)
        s.addstr('#')
        s.move(j, RIGHT + 1)
        s.addstr('#')
    l, v = 7, 2
    for k in range(l, l + WIDTH):
        s.move(k, RIGHT - STEP)
        s.addstr('#')
    for k in range(v, v + WIDTH):
        s.move(k, LEFT + STEP)
        s.addstr('#')
    time.sleep(1)
    y, x = 6, 15
    dx = -1
    dy = 1
    while True:
        if x == RIGHT or x == LEFT:
            s.move(y, x)
            s.addstr('X')
            s.move(BOTTOM//2, RIGHT//2)
            s.addstr('Game over')
            s.refresh()
            time.sleep(10)
            break
        if (x+dx == RIGHT-STEP and l - 1 < y+dy < l+WIDTH) or (x+dx == LEFT+STEP and v - 1 < y+dy < v+WIDTH):
            dx = -dx
        if y+dy == BOTTOM or y+dy == TOP:
            dy = -dy
        if (x + dx == RIGHT - STEP and l < y + dy < l + WIDTH) or (x + dx == LEFT + STEP and v < y + dy < v + WIDTH):
            dx = -dx
        if dy == -1:
            if v > TOP:
                s.move(v + WIDTH - 1, LEFT + STEP)
                s.addstr(' ')
                v -= 1
                s.move(v, LEFT + STEP)
                s.addstr('#')
                s.refresh()
        else:
            if v + WIDTH - 1 < BOTTOM:
                s.move(v, LEFT + STEP)
                s.addstr(' ')
                v += 1
                s.move(v + WIDTH - 1, LEFT + STEP)
                s.addstr('#')
                s.refresh()
        s.move(y, x)
        s.addstr('O')
        s.refresh()
        time.sleep(0.07)
        s.move(y, x)
        s.addstr(' ')
        s.refresh()
        c = s.getch()
        x += dx
        y += dy
        if c == 259:
            if l > TOP:
                s.move(l + WIDTH - 1, RIGHT - STEP)
                s.addstr(' ')
                l -= 1
                s.move(l, RIGHT - STEP)
                s.addstr('#')
                s.refresh()
        if c == 258:
            if l + WIDTH - 1 < BOTTOM:
                s.move(l, RIGHT - STEP)
                s.addstr(' ')
                l += 1
                s.move(l + WIDTH - 1, RIGHT - STEP)
                s.addstr('#')
                s.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
'''
'''
#! /usr/bin/env python3
'''
'''
import curses
import time


def main(s):
    s.nodelay(1)
    curses.curs_set(0)
    for i in range(61):  #начало печатания рамки
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
        s.addstr('#')  #конец печатания рамки
    y = 12
    x = 30
    s.move(y, x)  #размещаю шарик
    s.addstr('O')
    s.refresh()
    s.move(y, x)
    s.addstr(' ')
    s.refresh()
    n = -1
    m = 1
    for infinity in range(100):
        if x == 59:
            s.move(y, x)
            s.addstr('X')
            s.move(12, 30)
            s.addstr('Game over')
            s.refresh()
            time.sleep(10)
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
        t = time.time()
        if time.time() - t >= 0.7:
            s.move(y, x)
            s.addstr(' ')
            s.refresh()
            while 1 < x < 59 and 1 < y < 23 and not(x + n == 55 and l - 1 < y + m < l + 7):
                x += n
                y += m
                s.move(y, x)
                s.addstr('O')
                s.refresh()
                t1 = time.time()
                if time.time() - t1 >= 0.7:
                    s.move(y, x)
                    s.addstr(' ')
                    s.refresh()
                    c = s.getch()
                    if c == 259:
                        if l > 1:
                            s.move(l + 6, 55)
                            s.addstr(' ')
                            l -= 1
                            s.move(l, 55)
                            s.addstr('#')
                            s.refresh()
                            time.sleep(0)
                if c == 258:
                    if l + 6 < 23:
                        s.move(l, 55)
                        s.addstr(' ')
                        l += 1
                        s.move(l + 6, 55)
                        s.addstr('#')
                        time.sleep(0)
                        s.refresh()
                if c == 259:
                    if l > 1:
                        s.move(l + 6, 55)
                        s.addstr(' ')
                        l -= 1
                        s.move(l, 55)
                        s.addstr('#')
                        s.refresh()
                        time.sleep(0)
                if c == 258:
                    if l + 6 < 23:
                        s.move(l, 55)
                        s.addstr(' ')
                        l += 1
                        s.move(l + 6, 55)
                        s.addstr('#')
                        time.sleep(0)
                        s.refresh()
    else:
        s.move(12, 30)
        s.addstr('You Won!')
        s.refresh()
        time.sleep(5)
# полная игра волейбол


if __name__ == '__main__':
    curses.wrapper(main)


'''
''' 
  1        10        20        30        40                                   
 "###############################################################",
 "#    []     |             []         ))))))                    ",
 "#    [] ____/             []         ((((((                    ",
 "#                         []         ))))))                    ",
 "#    []                   []         ((((((                    ",
 "#    []  ==========  ====={]         ))))))                    ",
 "#    []        |№         []         ((((((                    ",
 "#    []        |№         []        \------/                   ",
 "#    []     [ ]|№         []                                   ",
 "#    [}============  ====={]        /------\                   ",
 "#                                    ((((((                    ",
 "#                                    ))))))                    ",
 "#|№№№№№№ №№№№№№|                     ((((((                    ",
 "#|             |                     ))))))                    ",
 "#|             |                     ((((((                    ",
 "#|             |                     ))))))                    ",
 "#|             |                     ((((((                    ",
 "#|             |                     ))))))                    ",
 "#|             |                     ((((((                    ",
 "###############################################################",
'''
'''
def main(s):
    arrow1 = [1,1, '', 0]
    #Начинаю печатать поле
    high = 20
    long = 52
    mapn1 = [
        "###############################################################",
        "#    #      |             #     || ))))))                  ",
        "#    #  ____/             |     || ((((((                  ",
        "#    |                    #     || ))))))                  ",
        "#    #                    #     || ((((((                  ",
        "#    #   ##########  ######     || ))))))                  ",
        "#    #       OHH#         #     || ((((((                  ",
        "#    |          #         #     ||\------/                 ",
        "#    #      []  #         #                                    ",
        "#    ###-####-#####  #-####     ||/------\                 ",
        "#                               || ((((((                  ",
        "#                               || ))))))                  ",
        "######## #######                || ((((((                  ",
        "#              #                || ))))))                  ",
        "#              |                || ((((((                  ",
        "#              #                || ))))))                  ",
        "#[]            |                // ((((((                  ",
        "#              #               //  ))))))                  ",
        "#OHH           #              //   ((((((                  ",
        "###############################################################"
        ]
    for i in range(high):
        for j in range(long):

            s.move(i, j)
            s.addstr(mapn1[i][j])
            time.sleep(0)

    s.nodelay(1)
    curses.curs_set(0)
    #Заканчиваю печатать поле
    #Задаю координаты игрока
    y = 8
    x = 22
    s.move(y, x)
    s.addstr('^')
    direction = '^'
    #Задаю противников
    #назвние =ХР У  Х
    enemy1 = [5, 4, 4]
    enemy2 = [6, 5, 4]
    enemy3 = [7, 1, 10]
    enemy4 = [8, 8, 4]
    enemy5 = [9, 3, 3]
    enemys = [enemy1, enemy2, enemy3, enemy4, enemy5]
    for i in range(len(enemys)):
        s.move(enemys[i][1], enemys[i][2])
        s.addstr(str(enemys[i][0]))
    #Начинаем игру
    while True:
        c = s.getch()
        #Движение вниз
        if c == 258:
            direction = 'v'
            g = mapn1[y + 1]
            if g[x] == ' ':
                s.move(y, x)
                s.addstr(' ')
                y += 1
            s.move(y, x)
            s.addstr(direction)
            s.refresh()
        #Движение вврех
        if c == 259:
                direction = '^'
                g = mapn1[y - 1]
                if g[x] == ' ':
                    s.move(y, x)
                    s.addstr(' ')
                    y -= 1
                s.move(y, x)
                s.addstr(direction)
                s.refresh()
        #Движение вправо
        if c == 261:
            direction = '>'
            g = mapn1[y]
            if g[x + 1] == ' ':
                    s.move(y, x)
                    s.addstr(' ')
                    x += 1
            s.move(y, x)
            s.addstr(direction)
            s.refresh()
        #Движение влево
        if c == 260:
            direction = '<'
            g = mapn1[y]
            if g[x - 1] == ' ':
                    s.move(y, x)
                    s.addstr(' ')
                    x -= 1
            s.move(y, x)
            s.addstr(direction)
            s.refresh()
        # Выстрел
        if c == 32:
            arrow1x = x
            arrow1y = y
            if direction == '^' and mapn1[arrow1y - 1][arrow1x] == ' ':
                arrow1y = arrow1y - 1
                arrow1 = [arrow1y, arrow1x, '^', 1]
                s.move(arrow1[0], arrow1[1])
                s.addstr('|')
                s.refresh()
                time.sleep(0.05)
                s.move(arrow1y, arrow1x)
                s.addstr(' ')
            if direction == 'v' and mapn1[arrow1y + 1][arrow1x] == ' ':
                arrow1y = arrow1y + 1
                arrow1 = [arrow1y, arrow1x, 'v', 1]
                s.move(arrow1[0], arrow1[1])
                s.addstr('|')
                s.refresh()
                time.sleep(0.05)
                s.move(arrow1y, arrow1x)
                s.addstr(' ')
            if direction == '<' and mapn1[arrow1y][arrow1x - 1] == ' ':
                arrow1x = arrow1x - 1
                arrow1 = [arrow1y, arrow1x - 1, '<', 1]
                s.move(arrow1[0], arrow1[1])
                s.addstr('-')
                s.refresh()
                time.sleep(0.02)
                s.move(arrow1y, arrow1x)
                s.addstr(' ')
            if direction == '>' and mapn1[arrow1y][arrow1x + 1] == ' ':
                arrow1x = arrow1x + 1
                arrow1 = [arrow1y, arrow1x + 1, '>', 1]
                s.move(arrow1[0], arrow1[1])
                s.addstr('-')
                s.refresh()
                time.sleep(0.02)
                s.move(arrow1y, arrow1x)
                s.addstr(' ')
        #первая стрела
        if arrow1[3] != 0:
            if arrow1[2] == '^':
                if mapn1[arrow1y - 1][arrow1x] == ' ':
                    arrow1y -= 1
                    s.move(arrow1y, arrow1x)
                    s.addstr('|')
                    s.refresh()
                    time.sleep(0.05)
                    s.move(arrow1y, arrow1x)
                    s.addstr(' ')
                else:
                    arrow1[3] = 0
            if arrow1[2] == 'v':
                if mapn1[arrow1y + 1][arrow1x] == ' ':
                    arrow1y += 1
                    s.move(arrow1y, arrow1x)
                    s.addstr('|')
                    s.refresh()
                    time.sleep(0.05)
                    s.move(arrow1y, arrow1x)
                    s.addstr(' ')
                else:
                    arrow1[3] = 0
            if arrow1[2] == '<':
                if mapn1[arrow1y][arrow1x - 1] == ' ':
                    arrow1x -= 1
                    s.move(arrow1y, arrow1x)
                    s.addstr('-')
                    s.refresh()
                    time.sleep(0.02)
                    s.move(arrow1y, arrow1x)
                    s.addstr(' ')
                else:
                    arrow1[3] = 0
            if arrow1[2] == '>':
                if mapn1[arrow1y][arrow1x + 1] == ' ':
                    arrow1x += 1
                    s.move(arrow1y, arrow1x)
                    s.addstr('-')
                    s.refresh()
                    time.sleep(0.02)
                    s.move(arrow1y, arrow1x)
                    s.addstr(' ')
                else:
                    arrow1[3] = 0

            for i in range(5):
                if enemys[i][2] == arrow1x and enemys[i][1] == arrow1y and enemys[i][0] > 1:
                    enemys[i][0] -= 1
                    s.move(enemys[i][1], enemys[i][2])
                    s.addstr(str(enemys[i][0]))
                    s.refresh()

            s.move(19, 50)
            s.addstr(str(enemys[4][2]))
            s.move(18, 50)
            s.addstr(str(s.addstr(str(enemys[4][1]))))

if __name__ == '__main__':
    curses.wrapper(main)
'''
def main(s):
    cnt = 0
    #Задаю игровое поле
    high = 15
    long = 47
    mapn1 = [
        "        ##########                             ",
        "        ##      ##                             ",
        "        ##      ##                             ",
        "    ######      ####                           ",
        "    ##            ##                           ",
        "######  ##  ####  ##      ############         ",
        "##      ##  ####  ##########        ##         ",
        "##                                  ##         ",
        "##########  ######  ##  ####        ##         ",
        "        ##          ##################         ",
        "        ##############                         ",
        "                                               ",
        "                                               ",
        "                                               ",
        "                                               "
        ]
    #Печатаю игровое поле
    for i in range(high):
        for j in range(long):
            g = mapn1[i]
            s.move(i, j)
            s.addstr(g[j])
            time.sleep(0)
    s.nodelay(1)
    curses.curs_set(0)
    #Задаю координаты игрока
    y = 8
    x = 22
    s.move(y, x)
    s.addstr('**')
    #Задаю кординаты ящиков
    y1 = 7
    x1 = 10
    y2 = 7
    x2 = 4
    y3 = 4
    x3 = 10
    y4 = 2
    x4 = 10
    y5 = 4
    x5 = 14
    y6 = 3
    x6 = 14
    yall = [y1, y2, y3, y4, y5, y6]
    xall = [x1, x2, x3, x4, x5, x6]
    for i in range(len(yall)):
        xi = xall[i]
        yi = yall[i]
        s.move(yi, xi)
        s.addstr("[]")
    #Задаю координаты мест куда нужно поставить ящики
    y1s = 7
    x1s = 32
    y2s = 7
    x2s = 34
    y3s = 6
    x3s = 32
    y4s = 6
    x4s = 34
    y5s = 8
    x5s = 34
    y6s = 8
    x6s = 32

    #Отмечаю места, куда нужно поставить ящики
    yalls = [y1s, y2s, y3s, y4s, y5s, y6s]
    xalls = [x1s, x2s, x3s, x4s, x5s, x6s]
    for i in range(len(yall)):
        xi = xalls[i]
        yi = yalls[i]
        s.move(yi, xi)
        s.addstr("..")
    #Начинаем игру
    while True:
        c = s.getch()
        #Движение вниз
        if c == 258:
            cnt1 = 0
            cnt2 = 0
            if mapn1[y + 1][x] != '#':
                for i in range(len(xall)):
                    if y + 1 == yall[i] and xall[i] == x and mapn1[y + 2][x] != '#' or y + 1 != yall[i] or xall[i] != x:
                        cnt += 1
                    if y + 1 == yall[i] and xall[i] == x:
                        cnt1 += 1
                    if y + 2 == yall[i] and xall[i] == x:
                        cnt2 += 1
                if cnt == 6 and not(cnt1 != 0 and cnt2 != 0):
                    s.move(y, x)
                    s.addstr('  ')
                    y += 1
                    s.move(y, x)
                    s.addstr('**')
                    #Двигаю ящики
                    for i in range(len(xall)):
                        if x == xall[i] and y == yall[i]:
                            s.move(y + 1, x)
                            s.addstr('[]')
                            yall[i] += 1
                    
                    s.refresh()
                cnt = 0
        #Движение вврех
        if c == 259:
            cnt1 = 0
            cnt2 = 0
            if mapn1[y - 1][x] != '#':
                for i in range(len(xall)):
                    if y - 1 == yall[i] and xall[i] == x and mapn1[y - 2][x] != '#' or y - 1 != yall[i] or xall[i] != x:
                        cnt += 1
                    if y - 1 == yall[i] and xall[i] == x:
                        cnt1 += 1
                    if y - 2 == yall[i] and xall[i] == x:
                        cnt2 += 1
                if cnt == 6 and not (cnt1 != 0 and cnt2 != 0):
                    s.move(y, x)
                    s.addstr('  ')
                    y -= 1
                    s.move(y, x)
                    s.addstr('**')
                    # Двигаю ящики
                    for i in range(len(xall)):
                        if x == xall[i] and y == yall[i]:
                            s.move(y - 1, x)
                            s.addstr('[]')
                            yall[i] -= 1

                    s.refresh()
                cnt = 0
        #Движение вправо
        '''
        if c == 260:
            g = mapn1[y]
            if g[x - 2] != '#':
                if ((y == y1 and x - 2 == x1 and g[x - 4] != '#') or y != y1 or x - 2 != x1) and ((y == y2 and x - 2 == x2 and g[x - 4] != '#') or y != y2 or x - 2 != x2):
                    s.move(y, x)
                    s.addstr('  ')
                    x -= 2
                    s.move(y, x)
                    s.addstr('**')
                    
                    if x == x1 and y == y1:
                        s.move(y, x - 2)
                        s.addstr('[]')
                        x1 -= 2
                    if x == x2 and y == y2:
                        s.move(y, x - 2)
                        s.addstr('[]')
                        x2 -= 2
                    s.refresh()
        '''
        if c == 261:
            cnt1 = 0
            cnt2 = 0
            if mapn1[y][x + 2] != '#':
                for i in range(len(xall)):
                    if y == yall[i] and xall[i] == x + 2 and mapn1[y][x + 4] != '#' or y != yall[i] or xall[i] != x + 2:
                        cnt += 1
                    if y == yall[i] and xall[i] == x + 2:
                        cnt1 += 1
                    if y == yall[i] and xall[i] == x + 4:
                        cnt2 += 1
                if cnt == 6 and not (cnt1 != 0 and cnt2 != 0):
                    s.move(y, x)
                    s.addstr('  ')
                    x += 2
                    s.move(y, x)
                    s.addstr('**')
                    # Двигаю ящики
                    for i in range(len(xall)):
                        if x == xall[i] and y == yall[i]:
                            s.move(y, x + 2)
                            s.addstr('[]')
                            xall[i] += 2

                    s.refresh()
                cnt = 0
        if c == 260:
            cnt1 = 0
            cnt2 = 0
            if mapn1[y][x - 2] != '#':
                for i in range(len(xall)):
                    if y == yall[i] and xall[i] == x - 2 and mapn1[y][x - 4] != '#' or y != yall[i] or xall[i] != x - 2:
                        cnt += 1
                    if y == yall[i] and xall[i] == x - 2:
                        cnt1 += 1
                    if y == yall[i] and xall[i] == x - 4:
                        cnt2 += 1
                if cnt == 6 and not (cnt1 != 0 and cnt2 != 0):
                    s.move(y, x)
                    s.addstr('  ')
                    x -= 2
                    s.move(y, x)
                    s.addstr('**')
                    # Двигаю ящики
                    for i in range(len(xall)):
                        if x == xall[i] and y == yall[i]:
                            s.move(y, x - 2)
                            s.addstr('[]')
                            xall[i] -= 2

                s.refresh()
            cnt = 0
        #Выводим показатели
        s.move(12, 3)
        s.addstr(str(x))
        s.move(13, 3)
        s.addstr(str(y))


if __name__ == '__main__':
    curses.wrapper(main)


'''
     /--\ 
    /----\ 
   /------\ 
  /--------\ 
 /----------\ 
/------------\ 
'''
''' 
                
                      |>
                     / \ 
                    /   \ 
               |>  /     \ 
              / \ /_______\ 
             /   \|       | 
            /_____\       |      
            |     |       |
            |[] []|       |
            |     |   П_П_П_П_П
            |     |   \       /        
            |     |___|[]   []|#########
            | ___ |   |       ###########
____________|_|_|_|___|_______||_|_|_|_|__
_
'''
'''

 
#############
##           ##
#############



'''