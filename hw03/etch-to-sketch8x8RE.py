#!/usr/bin/env python3
# run setup.sh before starting program
import Adafruit_BBIO.GPIO as GPIO

import time
import smbus

bus = smbus.SMBus(2)
matrix = 0x70

# LED Matrix Setup
bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

leds = [0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00]
        
clear= [0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00]
        
# Inital Write to LED Matrix
bus.write_i2c_block_data(matrix, 0, leds)

# GPIO pin setup
b1 = "P8_11"
GPIO.setup(b1, GPIO.IN)
GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Grid setup
x = 3     #initilize x and y on grid 
y = 3
width = 7
height = 7

maxCount = '1000000'

eQEP1 = '1'
eQEP2 = '2'

COUNTERPATH1 = '/dev/bone/counter/'+eQEP1+'/count0'
COUNTERPATH2 = '/dev/bone/counter/'+eQEP2+'/count0'

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

while True:
    l.seek(0)
    dataL = int(l.read()[:-1])

    r.seek(0)
    dataR = int(r.read()[:-1])
    
    # x position
    if(dataR < olddataR):
        y += 1
        if(y > height):
            y = 0
        time.sleep(0.1)
    if(dataR > olddataR):
        y -= 1
        if(y < 0):
            y = height
        time.sleep(0.1)

        # y position
    if(dataL < olddataL):
        x -= 1
        if(x < 0):
            x = width
        time.sleep(0.1)
        
    if(dataL > olddataL):
        x += 1
        if(x > width):
            x = 0
        time.sleep(0.1)
        
    #reset button which clears terminal and sets the cursor back to position (3,3)
    if GPIO.input(b1):
        bus.write_i2c_block_data(matrix, 0, clear)
        break

    olddataR = dataR
    olddataL = dataL   
    
    leds[2*x] = leds[2*x]|(0x80>>y)
    bus.write_i2c_block_data(matrix, 0, leds)