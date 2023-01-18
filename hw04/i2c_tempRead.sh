#!/bin/bash
#chmod +x

# run setup.sh file before
# Temperature sensor needs to be at address 0x49
cd /sys/class/i2c-adapter/i2c-2
echo tmp101 0x4a > new_device
cd 2-004a/hwmon/hwmon0

while true
do
    temp=$(cat temp1_input)
    temp1=$((temp/1000))
    temp2=$((temp%1000))

    printf "The temperature is $temp1.$temp2 °C\r"
done