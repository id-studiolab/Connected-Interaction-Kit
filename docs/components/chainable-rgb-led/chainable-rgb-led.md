---
layout: default
title: "Chainable RGB LED"
parent: "Components"
has_children: false
---

![Image](assets/Grove-Chainable-LED-2.0.png)

# Chainable RGB LED
`Output` - typical RGB light can vary colour as well as brightness, can be chained into a LED strip with additional Chainable RGB LEDs

More detailed component information can be found [here](https://www.seeedstudio.com/Grove-Chainable-RGB-Led-V2-0.html).

---

## Blinking the internal LED (D13)
```python
# --- Imports
import digitalio
import time
import board

# --- Variables
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# --- Functions

# --- Setup
led.value = False

# --- Main loop
while True:
    print("hello world")
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.1)

```

## Blinking a Chainable LED connected to D13 (and D10)
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

## Fading a Chainable LED connected to D13 (and D10)
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
