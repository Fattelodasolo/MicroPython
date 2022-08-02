from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(4))
while True:
    try:
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
    
        print('Temperatura: ' , t , '°C')
        print('Umidità: ', h, '%\n')
    except OSError as e:
        print('Lettura sensore fallita!')
    
    sleep(5)
