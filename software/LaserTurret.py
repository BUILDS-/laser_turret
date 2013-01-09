import serial

class LaserTurret(serial.Serial):
    """
    """
    def __init__(self, port, baudrate=115200, timeout=1):
        """
        Initialize with port, baudrate and appropriate timeout.
        """
        super(LaserTurret, self).__init__(port=port, baudrate=baudrate,
                                          timeout=timeout)

    def clear(self):
        """
        Send the clear serial command.
        """
        self.write('c\n')

    def pan(self, angle):
        """
        Send out the pan serial `pX' command to set pan angle, where
        `X' is the angle from 0 (-90 to 90 degrees).
        """
        self.write('p%i\n' % angle)

    def tilt(self, angle):
        """
        Send out the tilt serial command `tX' to set the tilt angle, where
        `X' is the angle from 0 (-90 to 90 degrees)
        """
        self.write('t%i\n' % angle)

    def panTilt(self, pa, ta):
        """
        Send out a pan angle and a tilt angle.

        Variables:
        pa -- pan angle.
        ta -- tilt angle.
        """
        self.pan(pa)
        self.tilt(ta)

    def close(self):
        """
        Make sure that the turret is zeroed, then execute the
        serial.Serial close command.
        """
        self.clear()
        super(LaserTurret, self).close()
