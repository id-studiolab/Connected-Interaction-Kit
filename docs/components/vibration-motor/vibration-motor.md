---
layout: default
title: "Vibration Motor"
parent: "Components"
has_children: false
---

![Image](/assets/Grove-Vibration-Motor.png)

# Vibration Motor
`Output` - vibrates on a scale from soft to harsh, comparable to the one in your phone.

More detailed component information can be found [here](https://www.seeedstudio.com/Grove-Vibration-Motor.html).

---

## Basic analog output
Drive a vibration motor with a basic sawtooth function. Control the frequency by changing the value in `sleep.time`.
```python
# --- Imports
import board
import time
from analogio import AnalogOut

# --- Variables
analog_out = AnalogOut(board.A0)

# --- Functions

# --- Main program
while True:
	# Count up from 0 to 65535, with 64 increment
	# which ends up corresponding to the DAC's 10-bit range
	for i in range(0, 65535, 64):
		analog_out.value = i
		time.sleep(0.002)

```

