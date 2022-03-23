# shutter_meta_tester
A project which goal is to test the accuracy of shutter speed measurement tools.  

The general idea is to produce a well controlled shutter-like device.  
This device is used to produce a controlled open time, tested with a tool such as Shutter Speed Tester.  

If the measurement result of the tool is the same as the expected value, the measurement tool is accurate.  
The point is now to produce a well controlled open time. The target times are from 1s to 1/4000s.  

# Rotating window method
## Description
The idea is to use a wheel that rotates at a controlled frequency. By opening a hole in the wheel, we have the following open time :  

t = d / (2 x Pi x R x F)  

Where  
- t is the opened duration
- d is the diameter of the hole
- R is the radius from the wheel axis to the hole
- F is the wheel rotation frequency
 
## Pros/cons
- The pros
  - Very close to a real shutter
- The cons
  - A lot of hardware to buy
  - A lot of hardware to control 
  - The opening is repeated a lot, may that introduce a flaw in the measure ?   

# LED pulse method

## Description

The faster shutter speed we want to measure is 1/4000s = 250 micro seconds.  
Because the response time of an LED is very fast (about 10 nano seconds), it is possible produce a very well controlled light pulse using a microcontroler that lights on and off an LED. The pulse duration precision is induced by the precision of the microcontroler that controls the LED.  

## Pros/cons

- The pros
  - Easy to build
  - Easy to control the pulse duration
- The cons
  - Does not take into account the physical phenomenos induces by a physical shutter. Is that really a con ?     


## Schema  

![Tester schema](design/shutter_meta_tester_bb.png)
