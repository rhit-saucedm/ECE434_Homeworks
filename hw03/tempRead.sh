#!/bin/bash

# Read the temperature from the TMP101 sensor
temp1=`i2cget -y 2 0x49`
temp2=`i2cget -y 2 0x4a`

# Convert the temperature to Fahrenheit
temp1_f=$((($temp1 *9/5) + 32))
temp2_f=$((($temp2 *9/5) + 32))
# Print the temperature in Fahrenheit
echo "Temperature of Sensor 1: $temp1_f F"
echo "Temperature of Sensor 2: $temp2_f F"
