---
layout: default
title: "LED Pack"
grand_parent: "Components"
parent: "Solderless Components"
nav_order: 7
has_children: false
---

<img src="assets/Grove-LED-pack.png" alt="LED Pack" width="250"/>

# LED Pack
<a href="../../glossary/glossary"><img src="../../glossary/assets/output.png" alt="Output" width="72"/></a> <a href="../../glossary/glossary"><img src="../../glossary/assets/pwm.png" alt="PWM" width="72"/></a>

A monochrome light source that is simple to use.

{:.highlight-yellow}
Should your Connected Interaction Kit not include this component, you can use these examples with the LED built into your microcontroller, connected internally to pin **`D13`**.

More information on this component is available [here](https://www.seeedstudio.com/Grove-LED-Pack-p-4364.html).

---



## Blinking the internal LED (D13)

This is for the interal LED, however a LED Pack does work in port D13. A [Chainable LED](../chainable-led/chainable-led) does *NOT* work with this code.

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

## Blinking the LED Pack (connected to D2)
If the touch sensor is touched, turn the internal LED on. Otherwise turn the LED off.
```python
# --- Imports
import digitalio
import time
import board

# --- Variables
led = digitalio.DigitalInOut(board.D2)
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

