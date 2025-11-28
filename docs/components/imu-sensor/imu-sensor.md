---
layout: default
title: "IMU Sensor"
grand_parent: "Components"
parent: "Solderless Components"
nav_order: 0
has_children: false
---

<img src="assets/imu.svg" alt="IMU" width="250"/>

# IMU Sensors
<a href="../../glossary/glossary"><img src="../../glossary/assets/input.png" alt="Input" width="72"/></a> <a href="../../glossary/glossary"><img src="../../glossary/assets/iic.png" alt="I2C" width="72"/></a>



---

## Background



## Basic Usage



```python
# --- Imports
import time
import board
import pwmio
from adafruit_motor import servo

# --- Variables
pwm = pwmio.PWMOut(board.D13, frequency=50)
servo_motor = servo.Servo(pwm, min_pulse=700, max_pulse=2600)

# --- Functions

# --- Setup

# --- Main loop
while True:
    for angle in [0, 45, 90, 135, 180]:
        servo_motor.angle = angle
        time.sleep(1)
```

{:.note}
If you define a new position before reaching the previous one, the motor will abort its current operation and directly move to the new position.