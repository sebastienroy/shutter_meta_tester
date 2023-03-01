from machine import Pin, Timer, I2C
#from ssd1306 import SSD1306_I2C
import utime

stepTimer = Timer()
accelerationTimer = Timer()

buttonPin = 18
buttonState = 1

currentSpeed = 0
maxSpeed = 500

accelerationFreq = 10
accelerationStep = 5

accelerationValue = 1

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
single_step_seq = [ 
            [1,0,0,0], # A 
            [0,0,1,0], # B 
            [0,1,0,0], # A/
            [0,0,0,1]] # B/

button = Pin(buttonPin, mode=Pin.IN, pull=Pin.PULL_UP)

# begin
led.value(1)

def step(timer):
    global current_step
    for pin in range(4):
        motorPins[pin].value(single_step_seq[current_step][pin])
    current_step = (current_step + 1) % 4
    
def accelerate(timer):
    global currentSpeed, accelerationValue, accelerationStep
    currentSpeed = currentSpeed + accelerationValue * accelerationStep
    if(currentSpeed <= 0):
        currentSpeed = 0
        accelerationValue = 0
        accelerationTimer.deinit()
        stepTimer.deinit()
        for pin in range(4):
            motorPins[pin].value(0)
    elif(currentSpeed >= maxSpeed):
        currentSpeed = maxSpeed
        accelerationValue = 0
        accelerationTimer.deinit()
        
    if(currentSpeed != 0):
        stepTimer.init(freq=currentSpeed, mode=Timer.PERIODIC, callback=step)
    
def setAcceleration(value):
     global accelerationValue
     accelerationValue = value
     accelerationTimer.init(freq=accelerationFreq, mode=Timer.PERIODIC, callback=accelerate)       


def checkButton():
    global buttonState, accelerationValue, currentSpeed
    currentState = button.value()
    
    if(currentState == 0 and currentState != buttonState):
        if(currentSpeed == 0):
            setAcceleration(1)
        elif(currentSpeed == maxSpeed):
            setAcceleration(-1)
        else:
            setAcceleration(accelerationValue*-1)
    
    buttonState = currentState
    
def checkTest():
    val=button.value()
    led.value(val)
    utime.sleep(1)

led.value(1)

while(True):
    checkButton()
    utime.sleep_ms(100)
#end
led.value(0)
