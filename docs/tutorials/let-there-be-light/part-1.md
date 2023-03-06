---
layout: default
title: "Part 1: Load the program code using Mu Editor"
parent: "Let There Be Light!"
grand_parent: "Tutorials"
---

# Part 1 - Load the program code using Mu Editor

1. Using the USB cable included in the kit, connect the ItsyBitsy to your computer. It will appear in your computer's file manager as a storage device called `CIRCUITPY`. 
1. Open Mu Editor. Click the Load button in the toolbar at the top of the program window and navigate to the `CIRCUITPY` drive. Find the file named `code.py` and open it. 
1. Your microcontroller will execute any code stored in that file. Briefly examine the example code and see if you understand some parts. In the next step, we will take a closer look at how it works and how to tweak it.

```python
# Importing some libraries for time, controlling the board and digital input/outputs
import board # Learn more at https://learn.adafruit.com/circuitpython-essentials/circuitpython-pins-and-modules
import digitalio # Learn more at https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
import time

# Define a new variable and set D13 as an Output
LED = digitalio.DigitalInOut(board.D13)
LED.direction = digitalio.Direction.OUTPUT

# Usually code runs only once top to bottom until it is complete
# The function of "while True:" allows the code to run in a continous loop
# Everything indented with a tab is part of the function loop
while True:
	time.sleep(1.0) # Wait 1 second
	LED.value = True # Turn the LED on
	print("LED is on") # Add a status comment in the serial monitor
	
	time.sleep(1.0) # Wait 1 second
	LED.value = False # Turn the LED off
	print("LED is off") # Add a status comment in the serial monitor
	#The loop will start again after this line

```

![The small internal LED will blink with our provided code](assets/blink.png)

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
    print("LED is on")
    
    time.sleep(1.0)
    LED.value = False
    print("LED is off")

```

You can download the full code file [here](assets/code.py).

[Next Step](part-2){: .btn .btn-blue }
