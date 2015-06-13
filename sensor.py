#!/usr/bin/python
# Copyright (c) 2015 by Jason Seymour
# jaseymour@gmail.com

import socket
import json
import time
import Adafruit_BMP.BMP085 as BMP180
import Adafruit_DHT

sensor1 = BMP180.BMP085(mode=BMP180.BMP085_ULTRAHIGHRES)
sensor2 = Adafruit_DHT.AM2302
pin = 23

cTemp = sensor1.read_temperature()
fTemp = ((cTemp * 9) / 5) + 32
hPa = sensor1.read_pressure() / 100

rh, dht_temperature = Adafruit_DHT.read_retry(sensor2, pin)

JSON_PORT = 10000
JSON_HOST = '192.168.1.138'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((JSON_HOST, JSON_PORT))

data = {'Temperature *C': '{0:0.2f}'.format(cTemp), 'Temperature *F': '{0:0.2f}'.format(fTemp), 'Pressure': '{0:0.2f}'.format(hPa), 'Humidity': '{0:0.1f}'.format(rh), 'Probe': 'Home Outdoor 1'}

s.send(json.dumps(data))
s.send('\n')
s.close()

print 'Temperature = {0:0.2f} *C'.format(cTemp)
print 'Temperature = {0:0.2f} *F'.format(fTemp)
print 'Pressure = {0:0.2f} hPa'.format(hPa)
print 'Humidity={0:0.1f}%'.format(rh)
