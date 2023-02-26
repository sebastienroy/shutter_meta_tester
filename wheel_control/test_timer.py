from machine import Pin, Timer, I2C
from ssd1306 import SSD1306_I2C
import utime

tim = Timer()

#i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)
#oled = SSD1306_I2C(128, 64, i2c)

#oled.fill(0)
#oled.text("Pico",5,15)
#oled.show()

current_step = 0

motorPins = [
             Pin(14, Pin.OUT),  # A+
             Pin(15, Pin.OUT),  # A-
             Pin(17, Pin.OUT),   # B- 
             Pin(16, Pin.OUT)  # B+
             ]
led = Pin(25, Pin.OUT)

full_step_seq = [ 
            [1,0,1,0], # AB 
            [0,1,1,0], # A/B 
            [0,1,0,1], # A/B/
            [1,0,0,1]] # AB/

# begin
led.value(1)

def step(timer):
    global current_step
    for pin in range(4):
        motorPins[pin].value(full_step_seq[current_step][pin])
    current_step = (current_step + 1) % 4
    
speeds=[500]

for speed in speeds:
    tim.init(freq=speed, mode=Timer.PERIODIC, callback=step)
    utime.sleep(10)
    



utime.sleep(1)
for pin in range(4):
    motorPins[pin].value(0)
#end
led.value(0)
