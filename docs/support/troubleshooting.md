---
layout: default
title: Troubleshooting
parent: "Getting help"
nav_order: 1
---
# Troubleshooting Steps for ItsyBitsy

1. Is the ItsyBitsy powered/is the USB plugged in?
   1. Are you using a micro USB data cable? some cables only supply power, not data.
2. Are you working in Mu editor?
3. Are the sensors and actuators plugged into the correct ports?
   1. If you're using Chainable LEDs, are they connected to the IN side? (See the white arrow)
   2. Chainable LEDs don't need to return to the board.
4. Is the correct code saved on the ItsyBitsy? (Not locally on your laptop)
    1. Does the file have the name "code.py"?
    2. Mu indicates where it saves it when you click save, at the very bottom left.
5. Have you clicked the reset button once? (button with "rst")
6. If you open the Serial monitor and save again, is there an error in the console?
    1. If the error contains "Module", check if all libraries are on the board.
        1. You can find the libraries by googling "CircuitPython libraries" or download them from https://circuitpython.org/libraries.
        2. We're using version 9.X
    2. If the error contains "INDENT", then there's too much or too little TAB/(SPACE) somewhere. Usually at the beginning of a code line.
    3. If the error contains "SYNTAX", there's likely a missing ":" or a keyword (such as IF or Print) is mistyped/used incorrectly.
7. Are you in REPL mode (Do you see ">>>" in your console)? You can exit by typing "ctrl + d", or a few times "ctrl + c" and then "ctrl + d".
8. Make sure you read what the code does and follow all steps.