import Adafruit_BBIO.GPIO as GPIO
GPIO.setup("P9_12", GPIO.OUT)
while True:
    if state == GPIO.HIGH:
        state = GPIO.LOW
    else:
        state = GPIO.HIGH
    GPIO.output("P9_12", state)
try:
    # Code to toggle the pin goes here
finally:
    GPIO.cleanup()
