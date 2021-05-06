#!/data/data/com.termux/files/usr/bin/python

import curses
from random import randint
from curses import textpad

dirs = [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN]
oppo_dirs = {
    curses.KEY_UP: curses.KEY_DOWN,
    curses.KEY_DOWN: curses.KEY_UP,
    curses.KEY_RIGHT: curses.KEY_LEFT,
    curses.KEY_LEFT: curses.KEY_RIGHT
}

def add_food(snake, box):
    food = None
    while food is None:
        food = [randint(box[0][0]+1,box[1][0]-1),
                randint(box[0][1]+1,box[1][1]-1)]
        if food in snake:
            food = None
    return food

def print_score(scr, score):
    h, w = scr.getmaxyx()
    txt = f'Score: {score}'
    scr.addstr(0,w//2-len(txt)//2,txt)
    scr.refresh()

def main(scr):
    curses.curs_set(0)
    scr.nodelay(True)
    scr.timeout(150)
    
    sh, sw = scr.getmaxyx()
    box = [[3, 3], [sh-3, sw-3]]
    textpad.rectangle(scr, *box[0], *box[1])

    snake = [[sh//2,sw//2-1], [sh//2,sw//2], [sh//2,sw//2+1]]
    dir = curses.KEY_LEFT
    for y, x in snake:
        scr.addstr(y, x, '#')
    food = add_food(snake,box)
    scr.addstr(*food,'*')

    score = 0
    print_score(scr, score)    
    while True:
        key = scr.getch()
        if key in dirs and key != oppo_dirs[dir]:
            dir = key
        head = snake[0]
        if dir == curses.KEY_RIGHT:
            new_head = [head[0],head[1]+1]
        elif dir == curses.KEY_LEFT:
            new_head = [head[0],head[1]-1]
        elif dir == curses.KEY_UP:
            new_head = [head[0]-1,head[1]]
        elif dir == curses.KEY_DOWN:
            new_head = [head[0]+1,head[1]]
        snake.insert(0,new_head)
        scr.addstr(*new_head, '#')

        if snake[0] == food:
            food = add_food(snake,box)
            scr.addstr(*food,'*')

            score += 1
            print_score(scr, score)
        else:
            scr.addstr(*snake[-1], ' ')
            snake.pop()

        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1] in [box[0][1], box[1][1]] or
            snake[0] in snake[1:]):
                msg = "Game Over!"
                scr.addstr(sh//2,sw//2-len(msg)//2,msg)
                scr.nodelay(False)
                scr.getch()
                break
        
        scr.refresh()

curses.wrapper(main)
