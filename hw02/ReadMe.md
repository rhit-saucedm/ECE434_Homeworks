1. What's the min and max voltage?
    Max = 3.4V, Min = -80mV
2. What period and frequency is it?
    f = 3.5 Hz, T = 285ms
3. How close is it to 100ms?
    The period is almost 3 times longer
4. Why do they differ?
    The processor is waiting 100ms in addition to the delay to toggle the pin
5. Run htop and see how much processor you are using.
    3.9%
6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? Make a table of the fastest values you try and the corresponding period and processor usage. Try using markdown tables: https://www.markdownguide.org/extended-syntax/#tables
| Time | Period | Processor Usage |
| ----------- | ----------- | ----------- |
| 0.1 | 285ms | 3.9% |
| 0.01 | 72ms | 15.5% |
| 0.001 | 56ms | 17.4% |
| 0.0001 | 49.7ms | 18.1% |
7. How stable is the period?
    The Period becomes more unstable the shorter the period becomes
8. Try launching something like vi. How stable is the period?
    The period becomes less stable when using nano
9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period?
    It slightly impacts the period. 
10. Togglegpio.sh uses bash (first line in file). Try using sh. Is the period shorter?
    No, the period isn't much shorter.
11. What's the shortest period you can get
    15Hz


Python
Write a python script to toggle a gpio pin as fast as possible.
run togglegpio.py

1. What period and frequency is it?
   248us and 4.7kHz
2. Run htop and see how much processor you are using.
    85.8%
3. Present the shell script and Python script results in a table for easy comparison.
| Time | Shell Script | Python |
| ----------- | ----------- | ----------- |
| 0.1 | 285ms |  |
| 0.01 | 72ms |  |
| 0.001 | 56ms |  |
| 0.0001 | 49.7ms |  | 

Etch to Sketch
What: The etch-to-sketchPB implements the use GPIO pushbuttons to move around an X to mimic a Etch-to-Sketch

How to run: 
    Configure 4 GPIO pushbuttons to "P8_11", "P8_12", "P8_13", and "P8_14". 
    Once wired, run the following command
    python3 etch-to-sketchPB.py

Enjoy!