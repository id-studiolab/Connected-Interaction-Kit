---
layout: default
title: "Advanced Radar Sensor"
grand_parent: "Components"
parent: "Advanced Components"
nav_order: 1
has_children: false
---



<img src="assets/advanced-radar-sensor.jpg" alt="Advanced Radar Sensor" width="250"/>

# Advanced Radar Sensor (LD2450)
<a href="../../glossary/glossary"><img src="../../glossary/assets/input.png" alt="Input" width="72"/></a> <a href="../../glossary/glossary"><img src="../../glossary/assets/serial.png" alt="Serial" width="72"/></a>

The ld2450 radar module allows you to monitor human presence, motion detection and tracking.  
Target tracking involves real-time tracking of the position of a (moving) target within a specific area, enabling measurement of the target’s distance, angle and speed (relative to the sensor).

---

## Required Libraries
Make sure to add the `ld2450.py` file to the `lib` folder on your ItsyBitsy Microcontroller.  
You can download the `ld2450.py` file here: [link](https://github.com/id-studiolab/EduGroveModules/blob/main/RadarSensor/Production%20Files/code/lib/ld2450.py)

## Basic Usage

This example prints the information from the LD2450 sensor to the serial monitor.
 
```python
import board
import busio
import ld2450

uart = busio.UART(board.TX, board.RX, baudrate=256000)  # Adjust pins and baudrate as needed

while True:
    parsed_data = ld2450.parse_ld2450_data(uart)  # Pass the uart object
    for target in parsed_data.targets:
        print(f"Target at ({target['x']}, {target['y']}) moving at {target['speed']} cm/s")
```