# HW08 Files - Marco Saucedo
#### ECE434 - Dr. Yoder

### Blink LED
 For this section, I copy and pasted the files under the `cd /pru-cookbook-code/02start` into this repository. The P9_31 pin has to be configured to gpio and also direction needs to be set to `OUT`. Once that has been done, you can run the the code using the following commands. 
 ```
 bone$ source setup.sh
 bone$ make
 ```
 Depending on what the delay is the **hello.pru0.c** file, the LED on P9_31 will blink. I was able to toggle the pin with delay = 0 and record a frequency of 12.5MHz. The waveform has a little bit of overshoot, but mostly stable