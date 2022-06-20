from machine import Pin
from time import sleep

led = Pin(22, Pin.OUT)

while True:
    led.on()
    sleep(2)
    led.off()
    sleep(2)