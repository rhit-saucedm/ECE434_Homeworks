#!/usr/bin/env python3
# $bone config-pin P8_33 eqep    eQEP1
# $bone config-pin P8_35 eqep

# $bone config-pin P8_41 eqep   eQEP2
# $bone config-pin P8_42 eqep
import time

# eQEP = '1'
# COUNTERPATH = '/dev/bone/counter/'+eQEP+'/count0'

eQEP1 = '1'
eQEP2 = '2'

COUNTERPATH1 = '/dev/bone/counter/'+eQEP1+'/count0'
COUNTERPATH2 = '/dev/bone/counter/'+eQEP2+'/count0'

ms = 100
maxCount = '1000000'

# f = open(COUNTERPATH+'/ceiling', 'w')
# f.write(maxCount)
# f.close()

# f = open(COUNTERPATH+'/enable', 'w')
# f.write('1')
# f.close()

# f = open(COUNTERPATH+'/count', 'r')

# olddata = -1

# while True:
#     f.seek(0)
#     data = f.read()[:-1]
#     if data != olddata:
#         olddata = data
#         print("data = " + data)
#     time.sleep(ms/1000)


# Initalize Left Encoder Position
l = open(COUNTERPATH2+'/ceiling', 'w')
l.write(maxCount)
l.close()

l = open(COUNTERPATH2+'/enable', 'w')
l.write('1')
l.close()

l = open(COUNTERPATH2+'/count', 'r')

olddataL = -1

# Initalize Right Encoder Position
r = open(COUNTERPATH1+'/ceiling', 'w')
r.write(maxCount)
r.close()

r = open(COUNTERPATH1+'/enable', 'w')
r.write('1')
r.close()

r = open(COUNTERPATH1+'/count', 'r')

olddataR = -1


while True:
    r.seek(0)
    right_data = r.read()[:-1]
    l.seek(0)
    left_data = l.read()[:-1]

    if right_data != olddataR:
        olddataR = right_data
        print("Right data = " + right_data)
    
    if left_data != olddataL:
        olddataL = left_data
        print("Left data = " + left_data)
    time.sleep(ms/1000)