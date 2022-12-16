#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time
GPIO_PIN = "P9_12"
GPIO.setup(GPIO_PIN, GPIO.OUT)

while True:
    GPIO.output(GPIO_PIN, GPIO.HIGH)
    # time.sleep(0.001)
    GPIO.output(GPIO_PIN, GPIO.LOW)
    # time.sleep(0.001)
