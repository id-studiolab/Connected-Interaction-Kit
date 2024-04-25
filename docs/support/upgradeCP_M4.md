---
layout: default
title: Upgrade Circuit python for M4
parent: "Getting help"
nav_order: 2
---

# How to upgrade to Circuit Python for M4
*Guide based on [Adafruit update page](https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4/circuitpython), check this page for more in-depth guidance*.  

1. Connect ItsyBitsy to your computer, you should see a USB drive appear as: CIRCUITPY  
<img src="assets/circuitpy.png" alt="" width="100"/>  
2. Find out which version of CircuitPython you are running currently, you can use step a **OR** step b
   1. Open the CIRCUITPY drive and open the ```boot_out.txt``` file. you should see something like ```Adafruit CircuitPython 7.1.1``` this is the version of CircuitPython you are currently using. If this is already shows the version you want to upgrade to, you can stop this tutorial.  
<img src="assets/boot_before_upgrade_M4.png" alt="" width="100%"/>  
    2. Open MU editor, press the serial button, and in the REPL you should also see your version of CircuitPython printed.  
<img src="assets/mu_editor_before_upgrade_M4.png" alt="" width="100%"/>  

3. Double-click the RESET button, the drive disappears and reappears as: ITSYM4BOOT    
<img src="../components/itsybitsy-microcontroller/assets/recognize_IB_M4.jpg" alt="" width="200"/>
<img src="assets/ITSYM4BOOT.png" alt="" width="100"/>  
  
4. Download the latest stable version of CircuitPython at [this page](https://circuitpython.org/board/itsybitsy_m4_express/) by pressing the ```Download .uf2 now``` button.
<img src="assets/M4circuitpython.png" alt="" width="100%"/>

5. Drag the .uf2 file to the ITSYM4BOOT drive, the drive disappears and reappears as: CIRCUITPY  
<img src="assets/draguf2_M4.png" alt="" width="100%"/>  
  
6. To find out if the upgrade was successful you can use step a **OR** step b
   1. Open the CIRCUITPY drive and open the ```boot_out.txt``` file. you should see something like ```Adafruit CircuitPython 9.0.4``` this is the version of CircuitPython you are now upgraded to.
<img src="assets/boot_after_upgrade_M4.png" alt="" width="100%"/>  
   1. Open MU editor, press the serial button, and in the REPL you should also see your version of CircuitPython printed. this is the version of CircuitPython you are now upgraded to.
<img src="assets/mu_editor_after_upgrade_M4.png" alt="" width="100%"/>  