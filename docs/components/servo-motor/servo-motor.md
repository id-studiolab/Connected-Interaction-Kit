---
layout: default
title: "Servo Motor"
grand_parent: "Components"
parent: "Solderless Components"
nav_order: 0
has_children: false
---

<img src="assets/Grove-Servo.png" alt="Servo" width="250"/>

# Servo Motor
`Output` - movement, can rotate its arm like the windshield wiper of a car

More detailed component information can be found [here](https://www.seeedstudio.com/Grove-Servo.html).

---

## Basic servo example
Drive a servo motor with a windshield wiping motion. Control the frequency by changing the value in `sleep.time`.
```python
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin D13.
pwm = pwmio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
```
