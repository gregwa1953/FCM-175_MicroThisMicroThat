# writer_demo.py Demo pogram for rendering arbitrary fonts to an SSD1306 OLED display.
# Illustrates a minimal example. Requires ssd1306_setup.py which contains
# wiring details.

# The MIT License (MIT)
#
# Copyright (c) 2018 Peter Hinch
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# https://learn.adafruit.com/monochrome-oled-breakouts/wiring-128x32-spi-oled-display
# https://www.proto-pic.co.uk/monochrome-128x32-oled-graphic-display.html

# V0.3 13th Aug 2018

import machine
from ssd1306_setup import WIDTH, HEIGHT, setup
from writer import Writer
import time
# Font
# import freesans20
import font6
# import font10


def test(use_spi=False):
    # ssd = setup(use_spi)  # Create a display instance
    ssd = setup(False, False)
    # wri = Writer(ssd, font10)
    wri = Writer(ssd, font6)
    # wri = Writer(ssd, freesans20)
    Writer.set_textpos(ssd, 0, 0)  # verbose = False to suppress console output
    
    dt = time.localtime()
    print(dt)
    dtstr1 = "{0}/{1}/{2}\n".format(dt[1],dt[2],dt[0])
    print(dtstr1)
    wri.printstring(dtstr1)
    dtstr2 = "{0}:{1}:{2}".format(dt[3],dt[4],dt[5])
    wri.printstring(dtstr2)
    ssd.show()
    for cntr in range(120):
        Writer.set_textpos(ssd,14,0)  # font6.py
        # Writer.set_textpos(ssd,18,0)  # font10.py
        # Writer.set_textpos(ssd,20,0)  # freesans20.py
        dt = time.localtime()
        if dt[5] < 10:
            sec = "0" + str(dt[5])
        else:
            sec = dt[5]
        dtstr2 = "{0}:{1}:{2}".format(dt[3],dt[4],sec)
        wri.printstring(dtstr2)        
        ssd.show()
        time.sleep(1)
        
print('Test assumes a 128*64 (w*h) display. Edit WIDTH and HEIGHT in ssd1306_setup.py for others.')
print('Device pinouts are comments in ssd1306_setup.py.')
print('Issue:')
print('writer_demo.test() for an I2C connected device.')
print('writer_demo.test(True) for an SPI connected device.')
test(False)

