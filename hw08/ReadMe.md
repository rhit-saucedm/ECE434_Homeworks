# HW08 Files - Marco Saucedo
#### ECE434 - Dr. Yoder

### Blink LED
 For this section, I copy and pasted the files under the `cd /pru-cookbook-code/02start` into this repository. The P9_31 pin has to be configured to gpio and also direction needs to be set to `OUT`. Once that has been done, you can run the the code using the following commands. 
 ```
 bone$ source setup.sh
 bone$ make
 ```
 Depending on what the delay is the **hello.pru0.c** file, the LED on P9_31 will blink. I was able to toggle the pin with delay = 0 and record a frequency of 12.5MHz. The waveform has some jitter and a bit of overshoot, but mostly stable

### PWM Generator
 For this section you will have to configure a few things before running code. The P9_31 will need to be configured as pruout. I changed one of the delays to = 1, and this gave me a signal that measured in 50 MHz. The standard deviation was small, but the wave was close to being sinusoidal. It wasn't jittery, but it was very stable. 

| Section  | Fastest Clock Speed |
| ------------- | ------------- |
| LED Toggle  | 12.5 MHz  |
| PWM Toggle  | 50 MHz  |
