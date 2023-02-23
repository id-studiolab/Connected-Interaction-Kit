---
layout: default
title: "Tactile switch"
grand_parent: "Components"
parent: "Custom Components"
nav_order: 0
has_children: false
---

<img src="assets/custom-tactile-switch-centered.png" alt="Custom Tactile Switch" width="250"/>

# Tactile Switch
`Input` - detect if button is pressed down or released

Learn how to make your own tactile switch [here](../../tutorials/04-assemble-custom-component/)


---

## Basic tactile switch example
```python
# --- Imports
import digitalio
import time
import board

# --- Variables
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.D7)
button.direction = digitalio.Direction.INPUT

# --- Functions

# --- Setup
led.value = False

# --- Main loop
while True:
    print("hello world")
    if button.value == False:
        led.value = False
    else:
        led.value = True
    time.sleep(0.05)  # Make the loop run a little bit slower
```
