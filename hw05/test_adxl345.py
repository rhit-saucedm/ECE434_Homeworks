#!/usr/bin/env python3
#chmod +x
import time
from adxl345 import ADXL345
 
adxl345 = ADXL345()
 
axes = adxl345.getAxes(True)
while True:
    print("ADXL345 on address 0x%x:" % (adxl345.address))
    print("   x = %.3fG" % ( axes['x'] ))
    print("   y = %.3fG" % ( axes['y'] ))
    print("   z = %.3fG" % ( axes['z'] ))
    time.sleep(1)