
2
3
4
5
6
7
8
9
10
11
12
13
14
import Adafruit_BBIO.UART as UART
import serial
 
UART.setup(&quot;UART5&quot;)
 
ser = serial.Serial(port = &quot;/dev/ttyS5&quot;, baudrate=38400)
ser.close()
ser.open()
if ser.isOpen():
   print &quot;Serial is open!&quot;
   ser.write(&quot;AT+VERSION?\r\n&quot;)
   resp=ser.readline();
   print resp;
ser.close()
