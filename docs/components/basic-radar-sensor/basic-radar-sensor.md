---
layout: default
title: "Basic Radar Sensor"
grand_parent: "Components"
parent: "Advanced Components"
nav_order: 0
has_children: false
---



<img src="assets/basic-radar-sensor.jpg" alt="Basic Radar Sensor" width="250"/>

# Basic Radar Sensor (LD2410)
<a href="../../glossary/glossary"><img src="../../glossary/assets/input.png" alt="Input" width="72"/></a> <a href="../../glossary/glossary"><img src="../../glossary/assets/serial.png" alt="Serial" width="72"/></a>

This sensor serves as a replacement for a PIR sensor and works on the basis of microwaves and the doppler effect. Due to a difference in speed, this sensor can detect motion, this also works through almost all materials except metal

---

## Required Libraries
Make sure to add the `ld2410.py` file to the `lib` folder on your ItsyBitsy Microcontroller.  
You can download the `ld2410.py` file here: [link](https://github.com/id-studiolab/EduGroveModules/blob/main/RadarSensor/Production%20Files/code/lib/ld2410.py)

## Basic Usage

This example prints the information from the LD2410 sensor to the serial monitor.
 
```python
import time
import board
import busio
from ld2410 import LD2410

# Initialize UART for communication with the LD2410 sensor
uart = busio.UART(board.TX, board.RX, baudrate=256000)

# Create an instance of the LD2410 class
ld2410 = LD2410(uart)

# Read Firmware Version
ld2410.read_firmware_version()

# Wait for a moment
time.sleep(1)

def main():
    while True:
        # Update the sensor data
        ld2410.update()
        
        # Print out the parsed data
        print("Target State:", ld2410.target_state)
        print("Moving Distance:", ld2410.moving_distance, "cm")
        print("Moving Energy:", ld2410.moving_energy)
        print("Stationary Distance:", ld2410.stationary_distance, "cm")
        print("Stationary Energy:", ld2410.stationary_energy)
        print("Detection Distance:", ld2410.detection_distance, "cm")
        print("-" * 40)
        
        # Delay before the next update
        time.sleep(5)

if __name__ == "__main__":
    main()
```