#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time
import curses
import sys
from curses import wrapper


# Define the pins for each button
buttonUP = "P8_11"
buttonLEFT = "P8_12"
buttonDOWN = "P8_13"
buttonRIGHT = "P8_14"

# Set up the pins as inputs
GPIO.setup(buttonUP, GPIO.IN)
GPIO.setup(buttonLEFT, GPIO.IN)
GPIO.setup(buttonDOWN, GPIO.IN)
GPIO.setup(buttonRIGHT, GPIO.IN)

# Set up the curses screen
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

def main(stdscr):

    stdscr.clear()
    stdscr.keypad(True)
    stdscr.leaveok(True)
    stdscr.nodelay(False)
    
    # sets default (X,Y) location of cursor
    curseX = 0
    curseY = 0
    
    while True:
        if GPIO.input(buttonUP) == 1:
            curseY -= 1
        if GPIO.input(buttonLEFT) == 1:
            curseX -= 1
        if GPIO.input(buttonDOWN) == 1:
            curseY += 1
        if GPIO.input(buttonRIGHT) == 1:
            curseX += 1

        if (GPIO.input(buttonLEFT) == 1) & (GPIO.input(buttonRIGHT) == 1):
            stdscr.clear()
        
        #detects boarders to keep curser within terminal
        if curseX >= curses.COLS:
            curseX = curses.COLS - 1
        if curseX <= 0:
            curseX = 0
        if curseY >= curses.LINES:
            curseY = curses.LINES - 1
        if curseY <= 0:
            curseY = 0
        
        stdscr.addch(curseY, curseX, "X")
        stdscr.refresh()
        time.sleep(0.15)
        
wrapper(main)
