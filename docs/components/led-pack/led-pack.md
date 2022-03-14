---
layout: default
title: "LED Pack"
parent: "Components"
has_children: false
---

![Image](assets/Grove-LED-pack.png)

# LED Pack
`Output` - monochrome light on or off, color depending on the LED in the socket. The spin button next to the LED can control its luminance.

More detailed component information can be found [here](https://www.seeedstudio.com/Grove-LED-Pack-p-4364.html).

---

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

