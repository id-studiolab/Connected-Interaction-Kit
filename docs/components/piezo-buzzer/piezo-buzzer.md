---
layout: default
title: "Piezo Buzzer"
parent: "Components"
has_children: false
---

<img src="assets/Grove-Piezo-Buzzer.png" alt="Piezo Buzzer" width="250"/>

# Piezo Buzzer
`Output` - produces an alarming beep, can also be used to play simple melodies
`Input` - detect sound, can hear loud noises relative to silence

More detailed component information can be found [here](https://www.seeedstudio.com/Grove-Buzzer.html).

---

## Basic analog output
Drive a buzzer with a sawtooth function
```python
# --- Imports
import board
import time
from analogio import AnalogOut

# --- Variables
analog_out = AnalogOut(board.A0)

# --- Functions

# --- setup: code to run only once at the start
def setup():
	print("setup")

# --- loop: code to run every time in the main loop
def loop():
	print("loop")
	# Count up from 0 to 65535, with 64 increment
	# which ends up corresponding to the DAC's 10-bit range
	for i in range(0, 65535, 64):
		analog_out.value = i
		time.sleep(0.002)

# --- Main program
setup()
while True:
	loop()

```

## Melody
Play a simple melody using varying PWM frequencies
```python
import time
import board
import pwmio

piezo = pwmio.PWMOut(board.D4, variable_frequency=True)

onTime = 65535 // 20  # 5% Duty Cycle for clear tone on active buzzer

        # freq  durt  pause
melody = [[262, 0.25, 0.05],
          [294, 0.25, 0.05],
          [330, 0.25, 0.05],
          [349, 0.25, 0.05],
          [392, 0.5, 0.1],
          [392, 0.5, 0.1],
          [440, 0.25, 0.05],
          [440, 0.25, 0.05],
          [440, 0.25, 0.05],
          [440, 0.25, 0.05],
          [392, 0.75, 0.4],
          [440, 0.25, 0.05],
          [440, 0.25, 0.05],
          [440, 0.25, 0.05],
          [440, 0.25, 0.05],
          [392, 0.75, 0.4],
          [349, 0.25, 0.05],
          [349, 0.25, 0.05],
          [349, 0.25, 0.05],
          [349, 0.25, 0.05],
          [330, 0.5, 0.1],
          [330, 0.5, 0.1],
          [294, 0.25, 0.05],
          [294, 0.25, 0.05],
          [294, 0.25, 0.05],
          [294, 0.25, 0.05],
          [262, 0.75, 0.4]]

def make_tone(freq, duration, pause):
    piezo.frequency = freq
    piezo.duty_cycle = onTime
    time.sleep(duration)    # Duration of note
    piezo.duty_cycle = 0    # Off
    time.sleep(pause)       # Pause after note

while True:
    for note in melody:
        make_tone(note[0], note[1], note[2])

    time.sleep(0.75)
```

