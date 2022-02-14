---
layout: default
title: Step 3: Editing code
parent: "01 Hello World"
---

# Step 3: Editing code

Now that we have our two essential components (our computer + code editor, and ItsyBitsy + Expander board) set up we can start playing with the code.

1. Take a look at the `code.py` file. Can you understand what it is doing when reading the `# explaining comments`?
2. Let us change the blinking frequency of our LED. To do so, play around with the values inside the apprentices of `time.sleep(1.0)`. Try making it blink slower, or faster. 
3. Open the `Serial monitor` of your MU editor by clicking the button next to the `Save icon` in the menu bar. The serial monitor is an important tool for us, as we can use it to print out messages when code is executed, or see error messages that help us figure out what is going wrong.
4. Let us change the message that gets printed every time we turn our LED on and off. Change the two messages of the `print()` function to something else, and see how it changes in the Serial monitor after you save the file.

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
