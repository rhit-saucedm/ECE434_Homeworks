#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
import curses
import sys
from curses import wrapper

# Define the pins for each button
buttonUP = "P8_11"

# Set up the pins as inputs
GPIO.setup(buttonUP, GPIO.IN)

# Set up the curses screen
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

def main(stdscr):

    stdscr.clear()
    stdscr.keypad(True)
    stdscr.leaveok(True)
    stdscr.nodelay(False)
    
    # Setup Rotary Encoders
    eQEP1 = '1'
    eQEP2 = '2'

    COUNTERPATH1 = '/dev/bone/counter/'+eQEP1+'/count0'
    COUNTERPATH2 = '/dev/bone/counter/'+eQEP2+'/count0'

    maxCount = '1000000'

    # Initalize Left Encoder Position
    l = open(COUNTERPATH2+'/ceiling', 'w')
    l.write(maxCount)
    l.close()

    l = open(COUNTERPATH2+'/enable', 'w')
    l.write('1')
    l.close()

    l = open(COUNTERPATH2+'/count', 'r')

    olddataL = -1

    # Initalize Right Encoder Position
    r = open(COUNTERPATH1+'/ceiling', 'w')
    r.write(maxCount)
    r.close()

    r = open(COUNTERPATH1+'/enable', 'w')
    r.write('1')
    r.close()

    r = open(COUNTERPATH1+'/count', 'r')

    olddataR = -1
    
    # sets default (X,Y) location of cursor
    curseX = 0
    curseY = 0
    
    while True:

        #checking encoders
        l.seek(0)
        dataL = int(l.read()[:-1])

        r.seek(0)
        dataR = int(r.read()[:-1])

        if(dataR > olddataR):
          curseY -= 1
          time.sleep(0.1)
        if(dataL < olddataL):
          curseX -= 1
          time.sleep(0.1)
        if(dataR < olddataR):
          curseY += 1
          time.sleep(0.1)
        if(dataL > olddataL):
          curseX += 1
          time.sleep(0.1)

        if GPIO.input(buttonUP) == 1:
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

        olddataR = dataR
        olddataL = dataL  
        
        stdscr.addch(curseY, curseX, "X")
        stdscr.refresh()
        
wrapper(main)
