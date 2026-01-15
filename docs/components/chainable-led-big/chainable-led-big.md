---
layout: default
title: "Big chainable LED"
grand_parent: "Components"
parent: "Advanced Components"
nav_order: 3
has_children: false
---



<img src="assets/chainable-led-big.png" alt="Big Chainable LED" width="250"/>

# Big Chainable LED
<a href="../../glossary/glossary"><img src="../../glossary/assets/output.png" alt="Output" width="72"/></a> <a href="../../glossary/glossary"><img src="../../glossary/assets/digital.png" alt="Digital" width="72"/></a>

This is the big brother module of the chainable led, you can even use the original Neopixel library!
It is a 12W neopixel with extra white chip for accurate color reproduction. It uses the UCS2904B chip to toggle the channels.



{:.warning}
Each Big Chainable LED module requires 12v power and can draw up to 4 Amps.  
Chaining multiple is possible, but make sure you get a power supply that can deliver that amount of power and dont chain more than 5 units.  

---

## Required Libraries
Standard Neopixel library

## Basic Usage

A simple example of turning a single LED module red, green, blue and white.
 
```python
# --- Imports
import time
import board
import neopixel

# --- Variables
pin_leds = board.D13

num_leds = 1
leds = neopixel.NeoPixel(pin_leds, num_leds, auto_write=False, pixel_order=neopixel.GRBW)

# --- Functions

# --- Setup
leds.fill(0) # turn off all LEDs
leds.show()

# --- Main loop
while True:
    leds[0] = (255, 0, 0, 0) # red
    leds.show()
    time.sleep(2)
    leds[0] = (0, 255, 0, 0) # green
    leds.show()
    time.sleep(2)
    leds[0] = (0, 0, 255, 0) # blue
    leds.show()
    time.sleep(2)
    leds.fill((0, 0, 0, 255)) # white
    leds.show()
    time.sleep(2)
    leds.fill((0, 0, 0, 0)) # off
    leds.show()
    time.sleep(2)

```

