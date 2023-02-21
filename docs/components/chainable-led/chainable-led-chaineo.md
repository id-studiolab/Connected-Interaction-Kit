---
layout: default
title: "Chainable RGB/W LED"
nav_exclude: true
has_children: false
---

<img src="assets/ChaiNEO-RGBW.png" alt="Chainable RGB LED" width="250"/>

# Chainable RGB/W LED (ChaiNEO)
<a href="../../glossary/glossary"><img src="../../glossary/assets/output.png" alt="Output" width="72"/></a> <a href="../../glossary/glossary"><img src="../../glossary/assets/digital.png" alt="Digital" width="72"/></a>

A light source that can produce RGB colored and white light. Can be daisy chained. 

This component is based on an [RGB/W LED](https://www.adafruit.com/product/2758) sold by Adafruit and is compatible with their NeoPixel library. Extensive information on NeoPixel components and their use is available [here](https://learn.adafruit.com/adafruit-neopixel-uberguide/the-magic-of-neopixels).


{: .important}
Before proceeding, make sure your Chainable LED looks like the illustration above. If you are not sure if this is the correct version, refer to this [overview](chainable-led).

---

## Wiring

{: .highlight }
Confirm that the ChaiNEO module is oriented correctly, with the input port (marked "**IN**", at the base of the arrow) connected to the Grove connector on your BitsyExpander Board or the previous LED in your chain.

## Blinking a Chainable LED connected to D13

The ItsyBitsy doesn't have a built-in library to control the chainable LEDs. We will need to download one! Grove Chainable LEDs are controlled by `P9813` LED drivers, hence the need for a library that knows how to interact with these drivers. 
1. Download the [`P9813` library](assets/p9813.py). 
2. On your ItsyBitsy, add the file `p9813.py` to the `lib` folder. CircuitPython now knows where to find our newly downloaded library, and we can `import` it in our code.

```python
# --- Imports
import time
import board
import p9813

# --- Variables
pin_clk = board.D13
pin_data = board.D10
num_leds = 1
leds = p9813.P9813(pin_clk, pin_data, num_leds)

# --- Functions

# --- Setup
leds.fill((0, 0, 0))
leds.write()

# --- Main loop
while True:
    print("hello world")
    leds.fill((0, 0, 255))
    leds.write()
    time.sleep(0.5)
    leds.fill((0, 0, 0))
    leds.write()
    time.sleep(0.1)
```

## Fading a Chainable LED connected to D13
This example is using the blocking `time.sleep` functionality and will not mix well with other tasks in the interaction loop.

```python
# --- Imports
import time
import board
import p9813

# --- Variables
pin_clk = board.D13
pin_data = board.D10
num_leds = 1
leds = p9813.P9813(pin_clk, pin_data, num_leds)
intensity = 0
intensity_delta = 5

# --- Functions

# --- Setup
leds.fill((0, 0, 0))
leds.write()

# --- Main loop
while True:
    print("fading up")
    while intensity < 255:
        intensity = intensity + intensity_delta
        leds.fill((0, 0, intensity))
        leds.write()
        time.sleep(0.1)
    print("fading down")
    while intensity > 0:
        intensity = intensity - intensity_delta
        leds.fill((0, 0, intensity))
        leds.write()
        time.sleep(0.1)
```
