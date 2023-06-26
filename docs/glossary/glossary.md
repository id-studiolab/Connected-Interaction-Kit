---

layout: default
title: Glossary
nav_order: 3
has_children: true
has_toc: false

---

# Glossary

 ## Signal Terms

|              Term              | Description                                                  |
| :----------------------------: | :----------------------------------------------------------- |
|   ![Input](assets/input.png)   | An **input** is something a micro-controller can detect, such as the state of a switch, the rotation of a dial, or a microphone’s signal. |
|  ![Output](assets/output.png)  | An **output** is something that can be controlled by a microcontroller, such as a light, speaker, or motor. |
| ![Digital](assets/digital.png) | A **digital** signal is created by anything that assumes discrete states, such as on/off, true/false, or 1/0. |
|  ![Analog](assets/analog.png)  | An **analog** signal is created by anything that can assume any state on a continuous spectrum, such as temperature or pressure. |
|     ![PWM](assets/pwm.png)     | A **pulse-width modulated** signal is an analog-like signal created by switching a digital signal on and off very fast. |
|     ![I²C](assets/iic.png)     | The **I²C** protocol is used to interface advanced components using two digital signals. |
| ![Two Wire](assets/2wire.png)  | Components labeled with the **2-Wire** tag need two pins to function. Typically, that includes one pin used for transmitting data, while the other pin carries a clock signal that acts as a metronome to synchronize with the data stream's speed. The **I²C** protocol is a widely used standard that follows this principle. |

SECTIONS BELOW ARE UNDER CONSTRUCTION
{: .label .label-yellow }

## Programming Terms


|          Term           | Description                                                  |
| :---------------------: | :----------------------------------------------------------- |
|       `Variable`        | A **variable** is a named container used to store data values, such as a number, a string of text, or a more complex data structure. Variables can be overwritten, manipulated, and changed during the execution of a program, making them an essential part of any computer program. |
|       `Function`        | A **function** is a block of code that performs a specific task and can be called by other parts of the program. It typically takes input  parameters, processes them, and then returns an output value. Functions  are designed to be reusable, modular components that can simplify the  code, improve readability, and reduce errors. They allow programmers to  break down complex tasks into smaller, more manageable pieces, making  them an essential part of any computer program. |
|         `Loop`          | A **loop** is a structure that allows a set of instructions to be  repeatedly executed. Depending on the type of loop used, this can either happen for a specified number of times or until a particular condition is met. |
|   `Library`, `Module`   | **Libraries** and **modules** contain code written by other people to fulfill specific tasks. Core modules, such as `board`, `digitalio`, and `time` provide functionality essential to working with your board. Therefore, they are already included in CircuitPython. In some cases, you may need to download additional libraries to add functionality, such as drivers for specific sensors, to your code. You can learn more about that subject by reading the chapter on CircuitPython Libraries in [Adafruit's guide](learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries). |
|        `Object`         |                                                              |
|         `Class`         |                                                              |
|      `Declaration`      |                                                              |
|        `Method`         |                                                              |
|       `Instance`        |                                                              |
|        `Comment`        | In CircuitPython, comments start with a `#` character. Everything following `#` the character until the end of the line is considered part of the comment. Comments don't affect the program's execution and exist to help you and others understand the code better. |
| `Conditional Statement` |                                                              |
|          `API`          |                                                              |

## Electronics Terms

| Term | Description |
| :--------: | :----------------------------------------------------------- |
| **`Series`** | In a series circuit, each component is connected end-to-end with the other components, creating a single path for current to flow. This means that the current flowing through each component in the circuit is the same, but the voltage across each component differs. |
| `Parallel` | In a parallel circuit, are connected side-by-side, creating multiple paths for current to flow. This means that the current flowing through each component in the circuit can differ, but the voltage across each component is the same. |
| `Voltage`  |                                                              |
| `Current`  |                                                              |
| `Resistance` |                                                              |
| `MAC Address` | A MAC address (Media Access Control address) is a unique hardware address used to identify devices on a network. |
