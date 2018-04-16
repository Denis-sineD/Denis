








'''
from time import sleep
sleep(5)
print(5)
print(80 * '#')
for i in range
'''

import curses
import time

def main(s):
    s.move(0,0)
    s.addstr('#')
    s.refresh()
    time.sleep(10)

if __name__ == '__main__':
    curses.wrapper(main)
