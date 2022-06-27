from machine import Pin, ADC
from time import sleep

sensor = ADC(Pin(35))
sensor.atten(ADC.ATTN_11DB)

while True:
  valore = sensor.read()
  print(valore)
  sleep(0.5)