---
layout: default
title: "Time of Flight Sensor"
grand_parent: "Components"
parent: "Solderless Components"
nav_order: 6
has_children: false
---

<img src="assets/ToF_v2_VL53L0X.png" alt="Time of Flight Sensor Version 2"  width="250"/>

# Time of Flight Distance Sensor
<a href="../../glossary/glossary"><img src="../../glossary/assets/input.png" alt="Input" width="72"/></a> <a href="../../glossary/glossary"><img src="../../glossary/assets/digital.png" alt="Digital" width="72"/></a>

Detects the distance of objects directly in front of the sensor. Works best with white surfaces, for a range from 30 to 1200 mm.

{:.note}
<img src="assets/ToF_v1_VL53L0X_nomargins.png" alt="Time of Flight Sensor Version 1"  style="float: right; margin: 10px 0px 10px 15px;" width="90"/>The sensor included in your kit may look like the one pictured above or like the one pictured here. Both versions are functionally identical. The information in this article is valid no matter which version you own.

More detailed information about a similar component can be found [here](https://www.adafruit.com/product/3317).</br>
More code examples can be found [here](https://github.com/adafruit/Adafruit_CircuitPython_VL53L0X/tree/main/examples).

---

## Basic distance measuring
The ItsyBitsy doesn't have a built-in library to work with the ToF distance sensor. We will need to download one!
1. Download the [VL53L0X library](assets/adafruit_vl53l0x.py)
2. On your ItsyBitsy, add the file `adafruit_vl53l0x.py` to the `lib` folder. CircuitPython now knows where to find our newly downloaded library, and we can `import` it in our code.
3. Run the code and see the measured distances appear in your `Serial Monitor`
   
```python
import time
import board
import busio
import adafruit_vl53l0x

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

# Optionally adjust the measurement timing budget to change speed and accuracy.
# See the example here for more details:
#   https://github.com/pololu/vl53l0x-arduino/blob/master/examples/Single/Single.ino
# For example a higher speed but less accurate timing budget of 20ms:
# vl53.measurement_timing_budget = 20000
# Or a slower but more accurate timing budget of 200ms:
# vl53.measurement_timing_budget = 200000
# The default timing budget is 33ms, a good compromise of speed and accuracy.

# Main loop will read the range and print it every second.
while True:
    print("Range: {0}mm".format(vl53.range))
    time.sleep(1.0)

```

