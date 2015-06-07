#!/usr/bin/python
# Copyright (c) 2015 by Jason Seymour
# jaseymour@gmail.com

import Adafruit_BMP.BMP085 as BMP180
sensor = BMP180.BMP085(mode=BMP180.BMP085_ULTRAHIGHRES)

cTemp = sensor.read_temperature()
fTemp = ((cTemp * 9) / 5) + 32

print 'Temp = {0:0.2f} *C'.format(cTemp)
print 'Temp = {0:0.2f} *F'.format(fTemp)
print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())

