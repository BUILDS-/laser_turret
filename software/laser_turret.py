import serial
import time
from math import sin, cos, pi, acos, atan
from LaserTurret import LaserTurret
from optparse import OptionParser

if __name__ == "__main__":
    # Setup OptionParser to parse commandline arguments including:
    # * port    -- string that stores the location of the tty serial port
    # * baud    -- baudrate of the laser turret firmware. Default to
    #              115,200 baud now.
    # * verbose -- sets a verbose flag
    parser = OptionParser()
    parser.add_option("-p", "--port", action="store", type="string",
                      dest="port", help="Open LaserTurret on port",
                      default="/dev/tty.usbserial-A9007KVJ",
                      metavar="PORT")
    parser.add_option("-b", "--baud", action="store", type="int",
                      dest="baud",
                      help="Set baudrate, default is 115,200 baud.",
                      default=115200, metavar="BAUD")
    parser.add_option("-v", "--verbose", action="store_true",
                      help="Print out status messages")
    
    (options, args) = parser.parse_args()
    
    with LaserTurret(options.port, options.baud) as laser:
        #    with LaserTurret("/dev/tty.usbserial-A9007KVJ") as laser:
        p = 0
        t = 0
        i = 1

        while True:
            # Implement something to set pan and tilt
            p = 2.5*(2*cos(4*pi*i/100) - cos(1*pi*i/100)) - 10
            t = 2.5*(2*sin(4*pi*i/100) - sin(2*pi*i/100)) - 25

            if options.verbose is True:
                print "pan %i | tilt %i" % (p, t)

            # Send pan and tilt
            laser.pan(p)
            laser.tilt(t)

            # Step forward
            if i == 1000:
                i = 0
            else:
                i += 1

            time.sleep(.1)
