#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time

# Define the pins for each button
button1 = "P8_11"
button2 = "P8_12"
button3 = "P8_13"
button4 = "P8_14"

# Set up the pins as inputs
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)

while True:
    # Check the state of each button
    if GPIO.input(button1) == 1:
        print("Button 1 pressed")
    if GPIO.input(button2) == 1:
        print("Button 2 pressed")
    if GPIO.input(button3) == 1:
        print("Button 3 pressed")
    if GPIO.input(button4) == 1:
        print("Button 4 pressed")
    
    # Sleep for a short time to prevent excessive checking
    time.sleep(0.1)
