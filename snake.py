#!/data/data/com.termux/files/usr/bin/python

import curses
from time import sleep

def main(scr):
    scr.addstr('Hellooooo')
    scr.refresh()
    scr.getch()

curses.wrapper(main)
