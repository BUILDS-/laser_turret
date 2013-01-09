import serial
import time
from math import sin, cos, pi, acos, atan

class LaserTurret(serial.Serial):
    def __init__(self, port, baudrate=115200, timeout=1):
        super(LaserTurret, self).__init__(port=port, baudrate=baudrate, timeout=timeout)
    def clear(self):
        self.write('c\n')

    def pan(self, angle):
        self.write('p%i\n' % angle)

    def tilt(self, angle):
        self.write('t%i\n' % angle)

    def panTilt(self, pa, ta):
        self.pan(pa)
        self.tilt(ta)

    def close(self):
        self.clear()
        super(LaserTurret, self).close()

if __name__ == "__main__":
    with LaserTurret("/dev/tty.usbserial-A9007KVJ") as l:
        l.pan(20)
        l.tilt(-10)
        
        p = 0
        t = 0
        i = 1
        ip = 0
        it = 0
        while 1:
            i = (i + 1) % 60

            if i < 20:                
                p += 2
                t += 2
            elif (i >= 20) and (i < 40):
                p -= 4
            else:
                t -= 2
                p += 2
            p = 2.5*(2*cos(4*pi*i/100) - cos(1*pi*i/100))- 10
            t = 2.5*(2*sin(4*pi*i/100)-sin(2*pi*i/100))  -25

            l.pan(p)
            l.tilt(t)

            if i == 1000:
                i = 0
            else:
                i += 1
            time.sleep(.1)
