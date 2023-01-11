#!/usr/bin/env python3
# run setup.sh before starting program
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
import sys
from flask import Flask, render_template, request

app = Flask(__name__)   

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
        
clearLED= [0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00]
        
# Inital Write to LED Matrix
bus.write_i2c_block_data(matrix, 0, leds)

# Grid setup
x = 3     #initilize x and y on grid 
y = 3
width = 7
height = 7

@app.route("/")
def index():
    DownStatus = '0'
    UpStatus = '0'
    LeftStatus = '0'
    RightStatus = '0'
    templateData = {
                'title' : 'Etch-a-Sketch',
                'Down'  : DownStatus,
                'Up'  : UpStatus,
                'Left'  : LeftStatus,
                'Right'  : RightStatus,
        }
    return render_template('index5.html', **templateData)

@app.route("/<action>")
def action(action):
    DownStatus = '0'
    UpStatus = '0'
    LeftStatus = '0'
    RightStatus = '0'
    clear = '0'
    global x
    global y

    if action == "DownPRESS":
        y += 1
        if(y > height):
            y = 0
        leds[2*x] = leds[2*x]|(0x80>>y)
        bus.write_i2c_block_data(matrix, 0, leds)

    if action == "UpPRESS":
        y -= 1
        if(y < 0):
            y = height
        leds[2*x] = leds[2*x]|(0x80>>y)
        bus.write_i2c_block_data(matrix, 0, leds)

    if action == "LeftPRESS":
        x -= 1
        if(x < 0):
            x = width
        leds[2*x] = leds[2*x]|(0x80>>y)
        bus.write_i2c_block_data(matrix, 0, leds)

    if action == "RightPRESS":
        x += 1
        if(x > width):
            x = 0
        leds[2*x] = leds[2*x]|(0x80>>y)
        bus.write_i2c_block_data(matrix, 0, leds)
    
    if action == "ClearPRESS":
        bus.write_i2c_block_data(matrix, 0, clearLED)

    templateData = {
                'Down'  : DownStatus,
                'Up'  : UpStatus,
                'Right'  : RightStatus,
                'Left'  : LeftStatus,
                'Clear': clear,
    }
    return render_template('index5.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)
