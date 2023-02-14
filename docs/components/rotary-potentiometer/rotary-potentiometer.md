---
layout: default
title: "Rotary potentiometer"
grand_parent: "Components"
parent: "Custom Components"
nav_order: 1
has_children: false
---

<img src="assets/custom-rotation-pot-centered.png" alt="Custom Rotation Potentiometer" width="250"/>

# Rotary Potentiometer
`Input` - detect rotation changes between 0 and 270 of the central axis

Learn how to make your own rotation potentiometer [here](../../tutorials/04-assemble-custom-component/)

---

## Basic rotation potentiometer example
```python
# --- Imports
import time
import board
import analogio

# --- Variables
# Initialize analog input connected to rotation potentiometer
potentiometer = analogio.AnalogIn(board.A2)

# --- Functions

# --- Setup

# --- Main loop
while True:
    val = potentiometer.value # Read the potentiometer value
    print(val) # Output the value in the serial monitor
    time.sleep(0.05)  # Make the loop run a little bit slower
```

## Rotation potentiometer example with conversion to voltage 
```python
# --- Imports
import time
import board
import analogio

# --- Variables
# Initialize analog input connected to rotation potentiometer
potentiometer = analogio.AnalogIn(board.A2)

# --- Functions
# Make a function to convert from analog value to voltage.
def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage

# --- Setup

# --- Main loop
while True:
    val = potentiometer.value # Read the photo resistor value
    volts = analog_voltage(potentiometer) # Convert to voltage

    # Print the values
    print('Photo resistor value: {0} voltage: {1}V'.format(val, volts))
    time.sleep(0.05)  # Make the loop run a little bit slower
```

## Rotation potentiometer example with angle mapping
```python
# --- Imports
import time
import board
import analogio

# --- Variables
# Initialize analog input connected to rotation potentiometer
potentiometer = analogio.AnalogIn(board.A2)

# --- Functions
# Make a function to convert from analog value to 270 degrees
def get_angle(adc):
    return adc.value / 65535 * 270

# --- Setup

# --- Main loop
while True:
    val = potentiometer.value # Read the photo resistor value
    angle = get_angle(potentiometer) # Convert to voltage

    # Print the values
    print('Potentiometer value: {0} Angle: {1}º'.format(val, angle))
    time.sleep(0.05)  # Make the loop run a little bit slower
```

