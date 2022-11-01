import machine

sdaPIN=machine.Pin(15)
sclPIN=machine.Pin(22)

i2c=machine.I2C(sda=sdaPIN, scl=sclPIN, freq=10000)   

devices = i2c.scan()
if len(devices) == 0:
 print("Dispositivo non trovato!")
else:
 print('Dispositivo trovato:',len(devices))
for device in devices:
 print("Indirizzo: ",hex(device))