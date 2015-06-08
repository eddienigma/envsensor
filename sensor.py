#!/usr/bin/python
# Copyright (c) 2015 by Jason Seymour
# jaseymour@gmail.com

import Adafruit_BMP.BMP085 as BMP180
import Adafruit_DHT

sensor1 = BMP180.BMP085(mode=BMP180.BMP085_ULTRAHIGHRES)
sensor2 = Adafruit_DHT.AM2302
pin = 23

cTemp = sensor1.read_temperature()
fTemp = ((cTemp * 9) / 5) + 32
hPa = sensor1.read_pressure() / 100

rh, dht_temperature = Adafruit_DHT.read_retry(sensor2, pin)

print 'Temperature = {0:0.2f} *C'.format(cTemp)
print 'Temperature = {0:0.2f} *F'.format(fTemp)
print 'Pressure = {0:0.2f} hPa'.format(hPa)
print 'Humidity={0:0.1f}%'.format(rh)
