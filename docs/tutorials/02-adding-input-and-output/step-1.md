---
layout: default
title: "Step 1: Connecting an input component"
parent: "02 Adding Input and Output"
grand_parent: "Tutorials"
---

# Step 1: Connecting an input component

The program used in this tutorial is similar to the program used in Tutorial 1. This time around you will type it yourself from scratch to better understand what you are doing.

1. Take the Touch Sensor (02) and a Grove cable (18) out of the box and connect it to pin `D2` of the Expander Board, as shown in the illustration.

![Illustration of the proper setup of touch sensor and ItsyBitsy](/docs/tutorials/02-adding-input-and-output/assets/Tutorial2-Illustration-1.png)

2. Start Mu and open the file `code.py`. Delete all the program statements so you end up with a blank file. If you want to save the previous code you can copy it out first and paste it somewhere you can always find it. Alternatively you can duplicate `code.py` and rename the copy for example to `code_blink.py` - in this way you create a number of different behaviours ready for use on your `CIRCUITPY` memory volume.
3. In the first three lines of the program you announce to the `Python Interpreter` that you will use libraries created by other programmers. The `board` library makes it possible to conveniently access the pins of your microcontroller. The `digitalio` library makes it possible to work with components that can be in two different states: on or off (`True` or `False`). The `time` library make it possible to use timing functionality in your program.
4. Although the Touch Sensor is already physically attached to the microcontroller, it does not do anything yet. We need to declare a variable point it to the proper pin and define it as an input.
5. Finally you add a `while loop` that continuously reads the state of the touch sensor (`sensor.value`) and prints it to the `Serial Monitor` so you can verify that it is working.

```python
import board
import digitalio
import time

sensor = digitalio.DigitalInOut(board.D2)
sensor.direction = digitalio.Direction.INPUT

while True:
    print(sensor.value)
    time.sleep(0.1)
```