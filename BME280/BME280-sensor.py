from machine import Pin, I2C
from time import sleep
import BME280

i2c = I2C(scl=Pin(22), sda=Pin(15), freq=10000)

while True:
  bme = BME280.BME280(i2c=i2c)
  t = bme.temperature
  h = bme.humidity
  p = bme.pressure

  print('Temperatura: ', t)
  print('Umidità: ', h)
  print('Pressione: ', p)

  sleep(1)