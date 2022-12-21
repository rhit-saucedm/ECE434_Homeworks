Marco Saucedo
ECE434 - Dr. Yoder

1) Temperature Sensor
    a) Configure I2C pins
    b) to run python code input following:
        bone$  python3 tempRead.py
    c) to run shell file input following:
        bone$ chmod +x tempRead.sh
        bone$ ./tempRead.sh

2) Etch-to-Sketch
    a) run setup.sh
        bone$ chmod +x setup.sh
        bone$ ./setup.sh
    b) connect encoders to pins in setup.sh file
    c) run etch-to-sketchRE.py for basic game on laptop
        bone$ python3 etch-to-sketch8x8RE.py
    d) connect 8x8 LED matrix
    e) run etch-to-sketch8x8RE.py for game on 8x8 led matrix
        $bone python3 etch-to-sketch8x8RE.py

Enjoy!

# hw03 grading

| Points      | Description | | |
| ----------- | ----------- |-|-|
|  8/8 | TMP101 
|  2/2 |   | Documentation | *Please use Mark Down*
|  5/5 | Etch-a-Sketch
|  3/3 |   | setup.sh
|  2/2 |   | Documentation
| 20/20 | **Total**

*My comments are in italics. --may*

*Include your name in your code.*