#!/usr/bin/env python3
import time

TMP101a='/sys/class/i2c-adapter/i2c-2/2-0048/hwmon/hwmon0/'
# TMP101b='/sys/class/i2c-adapter/i2c-2/2-0049/hwmon/hwmon1/'

while(1):
    f = open(TMP101a+'temp1_input', "r")
    temp1=f.read()[:-1]     # Remove trailing new line
    # Convert from mC to C
    temp1 = int(temp1)/1000
    f.close()
    print("temp1: " + str(temp1))
    time.sleep(50)