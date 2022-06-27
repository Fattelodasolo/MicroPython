from machine import Pin
from time import sleep

button = Pin(13, Pin.IN)

while True:
  
  valore = button.value()
  print(valore)
  sleep_ms(50)