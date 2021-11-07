from machine import Pin
from time import sleep
import dht 
from ssd1306_setup import WIDTH, HEIGHT, setup
from writer import Writer
# import font10
import font6

sensor = dht.DHT22(Pin(14))

ssd = setup(False, False)
# wri = Writer(ssd, font10)
wri = Writer(ssd, font6)
Writer.set_textpos(ssd, 0, 0)  # verbose = False to suppress console output

while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    Writer.set_textpos(ssd, 0, 0)
    # print('Temperature: %3.1f C' %temp)
    # print('Temperature: %3.1f F' %temp_f)
    wri.printstring('Temp: %3.1f F\n' %temp_f)
    
    # print('Humidity: %3.1f %%' %hum)
    wri.printstring('Humidity: %3.1f %%' %hum)
    ssd.show()
  except OSError as e:
    print('Failed to read sensor.')