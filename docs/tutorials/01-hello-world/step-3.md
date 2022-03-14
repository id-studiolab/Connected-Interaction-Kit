---
layout: default
title: "Step 3: Changing the way your ItsyBitsy behaves"
parent: "01 Hello World"
grand_parent: "Tutorials"
---

# Step 3: Changing the way your ItsyBitsy behaves

1. Take a look at the `code.py` program in Mu’s window. Can you understand how the blink behaviour is created by reading the instructions in the program?
2. Can you change the blinking frequency of the internal LED? To do so, play around with the values specified in the parentheses of `time.sleep(1.0)`. Try to make it blink slower or faster. Press the `Save` button in the toolbar of Mu’s window to store and run your new program on the ItsyBitsy.
3. Show the `Serial Monitor` panel in the Mu window (click the toolbar button with the label `Serial`). The `Serial Monitor` is an important tool as it can show messages from your program and the `Python Interpreter`.
4. Can you change the message that is now printed every time the LED turns on and off? To do so change the two `strings` in the parentheses of the `print` instructions. Don’t forget to press the `Save` button in the toolbar of Mu’s window to store and run your new program on the ItsyBitsy.

After tinkering around, your code might now look like this:

```python
# Change the blinking speed to twice a second and edit the printing outputs
import board
import digitalio
import time 

LED = digitalio.DigitalInOut(board.D13)
LED.direction = digitalio.Direction.OUTPUT

while True:
    time.sleep(0.5)
    LED.value = True
    print("Yay, there is light! :)")
    
    time.sleep(0.5)
    LED.value = False
    print("No light anymore :(")
```
