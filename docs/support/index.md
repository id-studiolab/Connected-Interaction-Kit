---
layout: default
title: Getting help
nav_order: 4
has_children: False
---

# Getting help

## Why is my code not working?

{:.note}
Should you run into issues during coding please first carefully read the troubleshooting page.

[Troubleshooting page](troubleshooting){: .btn .btn-blue }

## What do I do when hardware components are not working?
In case any of your components not working as expected, please check the [documentation page](../components/index) of the component first and try getting it running with the example code first.

Most issues can be fixed by double-checking the following:
1. Is your component connected to the right port of the Expander board?
2. Is your ItsyBitsy properly plugged into your computer?
3. Does an error message appear in MU's `Serial monitor`, indicating a software issue (e.g. typos, coding mistake, missing library, etc.)

If you checked the points above thoroughly and your component is still not working, you can find extra help at IO's [Model Making and Machine Lab (PMB)](https://www.tudelft.nl/io/over-io/faciliteiten/pmb).

## Where can I get more hardware components?
The Connected Interaction Kit can be extended with additional Grove components. Every Grove component should work.

You can get additional components at following places:
1. Left-over and used Grove components can be gathered from the [PMB](https://www.tudelft.nl/io/over-io/faciliteiten/pmb) for free
2. New Grove components can be bought at the [PMB](https://www.tudelft.nl/io/over-io/faciliteiten/pmb) for 1€ per piece
3. Depending on the course, components can be borrowed temporarily from IO's StudioLab and Applied Lab
4. Bought online, for instance at [Kiwi Electronics](https://www.kiwi-electronics.nl/en/home)


## Where can I get support for prototyping for courses?
Each course using the Connected Interaction Kit will have their own tech support that can guide and support you in learning prototyping.

## How do I upgrade my Circuit Python version?  

|                       For Itsy Bitsy M4                        |                        For RP2040 Expander                        |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| <img src="../components/itsybitsy-microcontroller/assets/recognize_IB_M4.jpg" alt="" width="400"/> | <img src="../components/itsybitsy-microcontroller/assets/recognize_IB_RP2040.jpg" alt="BitsyExpander" width="400"/> |
| [Start upgrade](upgradeCP_M4){: .btn .btn-blue } | [Start upgrade](upgradeCP_RP2040){: .btn .btn-blue } |

## How do I install the required Circuit Python libraries?
1. Open the latest version of our project bundle  

[Download Project Bundle](https://github.com/Jerzeek/CIK-Project-Bundle/releases/latest){: .btn .btn-blue }

2. Download the cik-project-bundle-9.x-mpy.zip file
3. Unzip the file on your computer
4. Copy the complete lib folder
5. Paste the complete lib folder in the CIRCUITPY drive
6. Press replace if prompted.



## How do I install other Circuit Python libraries?
*Guide based on [Adafruit update page](https://learn.adafruit.com/adafruit-itsybitsy-rp2040/circuitpython-libraries), check this page for more in-depth guidance*



1. Download the CircuitPython Library you want
   1. This can be part of the complete Adafruit CircuitPython bundle: “Bundle for Version 9.x” from this [page](https://circuitpython.org/libraries).  
<img src="assets/libraries.png" alt="" width="100%"/>  
   2. Or this can be part of the Adafruit Community bundle: from this [page](https://github.com/adafruit/CircuitPython_Community_Bundle/releases/latest)
<img src="assets/community_libraries.png" alt="" width="100%"/>  
1. Unzip the file and copy the file to your lib folder on your ItsyBitsy
