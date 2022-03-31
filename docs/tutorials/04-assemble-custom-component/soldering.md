---
layout: default
title: "Before you Begin..."
parent: "04 Assemble a Custom Component"
grand_parent: "Tutorials"

---

# Soldering: Tools and Technique

*Fore a more complete introduction into soldering, we recommend reading Sparkfun's excellent guide [HERE](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering/).*

## Introduction

This guide intends to be a short read covering the basics of soldering using the tools available in the PMB. 

If you are already familiar with the tools we will work with, you may skip ahead to the following sections:

* [How to solder trhough-hole components](#how-to-solder-through-hole-components)
* [How to find and fix bad solder joints](#how-to-find-and-fix-bad-solder-joints)

First, let us take a look at the tools we will need:

### Essential Tools

| Soldering Iron                                     | Brass Sponge                                       | Stand                                      |
| -------------------------------------------------- | -------------------------------------------------- | ------------------------------------------ |
| ![Soldering Iron](assets/tutorial4-tools-iron.jpg) | ![Brass Sponge](assets/tutorial4-tools-sponge.jpg) | ![Stand](assets/tutorial4-tools-stand.jpg) |
| The most important tool you will be working with.  | To keep the iron clean and in working order.       | For safely storing the iron while hot.     |

| Solder (with flux core)                                    | Flush Cutters                                             | Vise or Third Hand                           |
| ---------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------- |
| ![Solder](assets/tutorial4-tools-solder.jpg)               | ![Flush Cutters](assets/tutorial4-tools-cutters.jpg)      | ![Vise](assets/tutorial4-tools-vise.jpg)     |
| To join components together electrically and mechanically. | For trimming excess leads and cutting components to size. | To hold your workpiece while you work on it. |

### Nice-to-Haves

| Flux Pen                                                     | Solder Wick                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="assets/tutorial4-tools-flux.jpg" alt="Flux Pen" width="500"> | <img src="assets/tutorial4-tools-wick.jpg" alt="Solder Wick" width="500"> |
| Add flux a solder joint for repair work or to make the solder flow better. NEEDED IF WORKING WITH SOLDER WITH NO FLUX CORE. | Can be used to "soak up" excess solder. Important in removing solder bridges, desoldering components, and other repair work. |



## Procedure

### How to solder through-hole components

| Step                                     | Description                                                  | Preview                                                      |
| ---------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **0. Before you begin**                  | Make sure the power to your work station is turned on.       | <img src="assets/tutorial4-pth-power.jpg" alt="Power On" style="zoom:120%;" /> |
| **1. Pre-heat the iron**                 | Turn on the exhaust and the soldering iron. Set the iron to 370°C and let it heat up for a few seconds. (370°C works best for the lead-free solder, for leaded solder use 340°C) | ![Settings](assets/tutorial4-pth-settings.jpg)               |
| **2. Clean and tin the tip** (if needed) | Make sure the tip of your soldering iron is shiny. If it is blackened and matte, dirt and oxidation will prevent the heat from transfering into the joint. In this case, wipe the tip of the iron in the brass sponge to clean it. Then tin it by applying a bit of solder to the tip. It should look shiny before you proceed. | ![Oxidation](assets/tutorial4-pth-oxidation.jpg)![Tinned Tip](assets/tutorial4-pth-tinning.jpg) |
| **3. Seat a component**                  | Insert one or more components and fix them. Components with flexible leads (e.g. resistors) can be easily fixed by bending the legs on the back of the PCB. Other components are easier to fix with a vise. Avoid short-circuits by checking that components are not touching any other conductive parts of the board. **Secure the hot iron in the stand while you do this.** | ![Populating](assets/tutorial4-pth-populating.jpg)![Fixing](assets/tutorial4-pth-fixing.jpg) |
| **4. Make a joint**                      | Apply heat to the joint you want to solder for a few seconds. Make sure you heat the pad and the lead at the same time. Then feed some solder wire into the joint until it is fully covered in solder and forms a tent shape. | ![Joining](assets/tutorial4-pth-joining.jpg)                 |
| **5. Trim excess leads**                 | Use the flus cuttes to cut excess leads as close as possible to the board. | ![Trimming](assets/tutorial4-pth-trimming.jpg)               |
| **6. Inspect**                           | Check that all the joints look good and no solder bridges/short circuits exist. Check the following paragraph for guidance on finding and resolving issues. | ![Inspecting](assets/tutorial4-pth-inspecting.jpg)           |
| **7. Wrap-up**                           | Clean the tip of the iron (see step 2) so the next person finds it in working order, and turn off your iron. If no one else is working at the station when you leave, turn off the main power. | ![Power Off](assets/tutorial4-pth-poweroff.jpg)              |

### How to find and fix bad solder joints

Instructions coming soon
{: .label .label-yellow }

