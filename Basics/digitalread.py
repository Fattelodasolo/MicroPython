from machine import Pin
from time import sleep_ms

button = Pin(16, Pin.IN)

while True:
  
  valore = button.value()
  print(valore)
  sleep_ms(50)
