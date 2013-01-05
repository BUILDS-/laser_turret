import serial
import time
from math import sin, cos, pi

class LaserTurret(serial.Serial):
    def clear(self):
        self.write('c')
        
Lazor = serial.Serial('/dev/tty.usbserial-A9007KVJ')
Lazor.open()

p = 0
t = 0
i = 1
Lazor.write("c")
while 1:
    p = 20*(sin(pi*i/20)**3)
    t = 13*cos(pi*i/20) - 5*cos(pi*2*i/20) - 2*cos(pi*3*i/20) - cos(pi*4*i/20)

    Lazor.write("p%it%i\n" % (p,t))

    if i == 160:
        i = 0
    else:
        i += 1

    time.sleep(.01)
