import curses
import sys
from curses import wrapper

stdscr = curses.initscr()

def main(stdscr):
    stdscr.clear()
    stdscr.keypad(True)
    stdscr.leaveok(True)
    stdscr.nodelay(False)
    
    # sets default (X,Y) location of cursor
    curseX = 0
    curseY = 0
    
    while True:
        window = stdscr.getch()

        if window == curses.KEY_LEFT:       #moves cursor to LEFT
            curseX -= 1
        elif window == curses.KEY_RIGHT:    #moves cursor to RIGHT
            curseX += 1
        elif window == curses.KEY_UP:       #moves cursor to UP
            curseY -= 1
        elif window == curses.KEY_DOWN:     #moves cursor to DOWN
            curseY += 1
        
        #detects boarders to keep curser within terminal
        if curseX >= curses.COLS:
            curseX = curses.COLS - 1
        if curseX <= 0:
            curseX = 0
        if curseY >= curses.LINES:
            curseY = curses.LINES - 1
        if curseY <= 0:
            curseY = 0
        
        stdscr.move(curseY,curseX)       # moves start to new spot
        stdscr.addstr(chr(42))           #adds * character to window

        if window == 32: #press SPACE to clear
            stdscr.clear()
        
        if window == 27: #press ESC to leave
            break

wrapper(main)