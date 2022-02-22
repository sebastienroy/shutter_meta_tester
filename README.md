# shutter_meta_tester
A project which goal is to test the accuracy of shutter speed measurement tools

The general idea is to produce a well controlled shutter-like device.
This device is used to produce a controlled open time, tested with a tool such as Shutter Speed Tester.

If the measurement result of the tool is the same as the expected value, the measurement tool is accurate.
The point is now to produce a well controlled open time. The target times are from 1s to 1/4000s.

The idea is to use a wheel that rotates at a controlled frequency. By opening a hole in the wheel, we have the following open time :

t = d / (2 x Pi x R x F)

Where
- t is the opened duration
- d is the diameter of the hole
- R is the radius from the wheel axis to the hole
- F is the wheel rotation frequency
