---
layout: default
title: Components
nav_order: 2
has_children: true
has_toc: false
---

# Components

 The core of the Connected Interaction Kit is an CircuitPython microcontroller board. With the help of a bit of code, this microcontroller allows you to interact with and perceive the outside world using various electronic sensors and actuators.

In addition, the kit contains the Expander, a board that allows you to easily build prototypes without the need for soldering. Later on, it can also enable you to make use of Wifi or Bluetooth, as well as to power your project from a battery.

## Core Components

|                       Microcontroller                        |                        Expander                        |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                Pico 2W                |           Solderless Connector Board for Pico           |
| <img src="pico-microcontroller/assets/pico2w-horizontal.svg" alt="pico2w" width="400"/> | <img src="pico-expander/assets/picoexpander-horizontal.svg" alt="PicoExpander" width="400"/> |
| [Learn More](pico-microcontroller/pico){: .btn .btn-blue } | [Learn More](pico-expander/pico-expander){: .btn .btn-blue } |

{: .important }
There are **multiple, functionally equivalent editions** of Connected Interaction Kit. The Core Components you own differ slightly between editions. Your exact components are determined by the year in which you purchased your Connected Interaction Kit. This page is designed to help you identify which version you own.

If in doubt, jump to the bottom of the page for helpful pointers on how to [recognize your hardware](components-core).


## Sensors & Actuators

Beyond that, the kit offers a selection of sensors and actuators. There are solderless components you can use right away, as well as custom components that require you to assemble them first. 

*Some components listed below may not be part of your kit edition but are available separately.*

### Solderless Grove Components

|                         Touch Sensor                         |                       Vibration Motor                        |                         Piezo Buzzer                         |                         Sound Sensor                         |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                       Capacitive Touch                       |                       Haptics & Touch                        |                            Sound                             |                            Sound                             |
| ![Touch Sensor](touch-sensor/assets/Grove-Touch-Sensor.png)  | ![Vibration Motor](vibration-motor/assets/Grove-Vibration-Motor.png) | ![Piezo Buzzer](piezo-buzzer/assets/Grove-Piezo-Buzzer.png)  | ![Sound Sensor](sound-sensor/assets/Grove-Sound-Sensor.png)  |
| <a href="../glossary/glossary"><img src="../glossary/assets/input.png" alt="Input" width="57"/></a> <a href="../glossary/glossary"><img src="../glossary/assets/digital.png" alt="Digital" width="57"/></a> | <a href="../glossary/glossary"><img src="../glossary/assets/output.png" alt="Output" width="57"/></a> <a href="../glossary/glossary"><img src="../glossary/assets/pwm.png" alt="PWM" width="57"/></a> | <a href="../glossary/glossary"><img src="../glossary/assets/output.png" alt="Output" width="57"/></a> <a href="../glossary/glossary"><img src="../glossary/assets/pwm.png" alt="PWM" width="57"/></a> | <a href="../glossary/glossary"><img src="../glossary/assets/input.png" alt="Input" width="57"/></a> <a href="../glossary/glossary"><img src="../glossary/assets/analog.png" alt="Analog" width="57"/></a> |
|  [Learn More](touch-sensor/touch-sensor){: .btn .btn-blue }  | [Learn More](vibration-motor/vibration-motor){: .btn .btn-blue } |  [Learn More](piezo-buzzer/piezo-buzzer){: .btn .btn-blue }  |  [Learn More](sound-sensor/sound-sensor){: .btn .btn-blue }  |

| Time of Flight Sensor | Chainable LED | Servo motor | IMU sensor |
| :---: | :---: | :---: | :---: |
| Distance | RGB/W Light | Motion | Motion |
| ![Time of Flight Sensor Version 2](time-of-flight-distance-sensor/assets/ToF_v2_VL53L0X.png) | ![ChaiNEO RGB/W LED](chainable-led/assets/ChaiNEO-RGBW.png) | ![Servo motor](servo-motor/assets/Grove-Servo.png) | ![IMU sensor](imu-sensor/assets/imu.svg) |
| <a href="../glossary/glossary"><img src="../glossary/assets/input.png" alt="Input" width="57"/></a> <a href="../glossary/glossary"><img src="../glossary/assets/iic.png" alt="I2C" width="57"/></a> | <a href="../glossary/glossary"><img src="../glossary/assets/output.png" alt="Output" width="57"/></a> <a href="../glossary/glossary"><img src="../glossary/assets/digital.png" alt="Digital" width="57"/></a> | <a href="../glossary/glossary"><img src="../glossary/assets/output.png" alt="Output" width="57"/></a> <a href="../glossary/glossary"><img src="../glossary/assets/pwm.png" alt="PWM" width="57"/></a> | <a href="../glossary/glossary"><img src="../glossary/assets/input.png" alt="Input" width="57"/></a> <a href="../glossary/glossary"><img src="../glossary/assets/iic.png" alt="I2C" width="57"/></a> |
| [Learn More](time-of-flight-distance-sensor/time-of-flight-distance-sensor){: .btn .btn-blue } | [Learn More](chainable-led/chainable-led-chaineo){: .btn .btn-blue } | [Learn More](servo-motor/servo-motor){: .btn .btn-blue } | [Learn More](imu-sensor/imu-sensor){: .btn .btn-blue } |



### Custom Components

|                        Potentiometer                         |                        Tactile Switch                        |                         Tilt Switch                          |                          Thermistor                          |                        Photoresistor                         |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                        Position/Angle                        |                             Push                             |                             Tilt                             |                         Temperature                          |                          Brightness                          |
| ![Custom Potentiometer](rotary-potentiometer/assets/custom-rotation-pot-centered.png) | ![Tactile Switch](tactile-switch/assets/custom-tactile-switch-centered.png) | ![Tilt Switch](tilt-switch/assets/custom-tilt-switch-centered.png) | ![Temperature Sensor](thermistor/assets/custom-temperature-sensor-centered.png) | ![Photoresistor](photoresistor/assets/custom-photo-resistor-centered.png) |
| <a href="../glossary/glossary"><img src="../glossary/assets/input.png" alt="Input" width="57"/></a> <a href="../glossary/glossary"><img src="../glossary/assets/analog.png" alt="Analog" width="57"/></a> | <a href="../glossary/glossary"><img src="../glossary/assets/input.png" alt="Input" width="57"/></a> <a href="../glossary/glossary"><img src="../glossary/assets/digital.png" alt="Digital" width="57"/></a> | <a href="../glossary/glossary"><img src="../glossary/assets/input.png" alt="Input" width="57"/></a> <a href="../glossary/glossary"><img src="../glossary/assets/digital.png" alt="Digital" width="57"/></a> | <a href="../glossary/glossary"><img src="../glossary/assets/input.png" alt="Input" width="57"/></a> <a href="../glossary/glossary"><img src="../glossary/assets/analog.png" alt="Analog" width="57"/></a> | <a href="../glossary/glossary"><img src="../glossary/assets/input.png" alt="Input" width="57"/></a> <a href="../glossary/glossary"><img src="../glossary/assets/analog.png" alt="Analog" width="57"/></a> |
| [Learn More](rotary-potentiometer/rotary-potentiometer){: .btn .btn-blue } | [Learn More](tactile-switch/tactile-switch){: .btn .btn-blue } |   [Learn More](tilt-switch/tilt-switch){: .btn .btn-blue }   |    [Learn More](thermistor/thermistor){: .btn .btn-blue }    | [Learn More](photoresistor/photoresistor){: .btn .btn-blue } |

