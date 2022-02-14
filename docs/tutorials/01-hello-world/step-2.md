---
layout: default
title: Step 2: Connecting the ItsyBitsy to your computer
parent: "01 Hello World"
---

# Step 2: Connecting the ItsyBitsy to your computer
1. Take the USB cable from the Connected Interaction Kit and connect the ItsyBitsy with your computer. The ItsyBitsy will be recognized by your computer as a device called `CIRCUITPY`.
2. Open the MU editor, click on `Load` in the menu bar at the top and  select the file `code.py` from the device `CIRCUITPY`. Usually this file would be empty, but you will notice that we already uploaded some default code on your board that makes the internal LED blink:

```python
# Importing some libraries for time, controlling the board and digital input/outputs
import board # Learn more at https://learn.adafruit.com/circuitpython-essentials/circuitpython-pins-and-modules
import digitalio # Learn more at https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
import time

# Define a new variable and set D13 as an Output
LED = digitalio.DigitalInOut(board.D13)
LED.direction = digitalio.Direction.OUTPUT

# Usually code runs only once, until it is complete
# This function of "while True:" allows the code to run in a continous loop
# Everything indented with a tab is part of the function loop
while True:
	time.sleep(1.0) # Wait 1 second
	LED.value = True # Turn the LED on
	print("LED is: " + LED.value) # Add a status comment in the serial monitor
	
	time.sleep(1.0) # Wait 1 second
	LED.value = False # Turn the LED off
	print("LED is off") # Add a status comment in the serial monitor
	#The loop will start again after this line

```

![The small internal LED will blink with our provided code](assets/03-Blinking.png)

You notice that some of the code (starting with a `#`) is greyed out. These commented sections are used for explanation, but will be skipped by the code and not influence our logic. 

The functional code without any comments looks like this:

```python
import board
import digitalio
import time 

LED = digitalio.DigitalInOut(board.D13)
LED.direction = digitalio.Direction.OUTPUT

while True:
    time.sleep(1.0)
    LED.value = True
    print("LED is ")
    
    time.sleep(1.0)
    LED.value = False
    print("LED is off")

```