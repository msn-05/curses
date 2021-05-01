#!/data/data/com.termux/files/usr/bin/python

import curses
from time import sleep

menu = ['Home','Play','Scoreboard','Exit']

def print_menu(scr, row_i):
    scr.clear()
    
    h, w = scr.getmaxyx()

    for i, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + i
        if i == row_i:
            scr.attron(curses.color_pair(1))
            scr.addstr(y,x,row)
            scr.attroff(curses.color_pair(1))
        else:
            scr.addstr(y,x,row)

    scr.refresh()
def main(scr):
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
    
    c_row_i = 0
    print_menu(scr, c_row_i)
    while True:
        key = scr.getch()
        
        scr.clear()
        
        if key == curses.KEY_UP and c_row_i > 0:
            c_row_i -= 1
        elif key == curses.KEY_DOWN and c_row_i < len(menu)-1:
            c_row_i += 1
        elif key == curses.KEY_ENTER or key in [10,13]:
            scr.addstr(0,0,f"You selected {menu[c_row_i]}")
            scr.refresh()
            if c_row_i == len(menu)-1:
                break
            scr.getch()
        print_menu(scr,c_row_i)
        scr.refresh()

curses.wrapper(main)
