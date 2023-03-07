---
layout: default
title: "Step 2: Find out your ItsyBitsy's MAC address"
parent: "Connecting To The Internet"
grand_parent: "Tutorials"
---

# Step 2: Find out your ItsyBitsy's MAC address

To give our ItsyBitsy Expander internet access on campus, it must be registered with the network and a unique identifier in order to get an iPD (password). For that we need the radio's `MAC address`.

1. If not done yet, connect your ItsyBitsy to your computer.
2. Open `Mu Editor` and open the file `code.py` on your `CIRCUITPY` memory volume.
3. Open the MU's `Serial Monitor`.
4. Copy and paste the code below into your `code.py`, replacing the content that was there before and click `Save`.
5. Write down the printed `MAC address`. I looks something like `A1:B2:C3:D4:E5:F6`
   
   ```python
   import board
   import busio
   from digitalio import DigitalInOut
      
   from adafruit_esp32spi import adafruit_esp32spi
      
   print()
   print()
   print("*********************************************")
   print("BitsyExpander MAC Address identification tool")
   print("*********************************************")
      
      
   esp32_cs = DigitalInOut(board.D9)
   esp32_busy = DigitalInOut(board.D11)
   esp32_reset = DigitalInOut(board.D12)
      
   spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
   esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_busy, esp32_reset)
      
   if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
      print()
      print("ESP32 found and in idle mode!")
      print()
   print("##########################")
      
   print("##########################")
   print("##                      ##")
   print("##  MAC address found:  ##")
   print("##                      ##")
   addr = ""
      
   # Format the MAC address (invert and parse hex values)
   for i in range(len(esp.MAC_address)-1, -1, -1):
      if (len((hex(esp.MAC_address[i]))[2:4]) < 2):
         addr += "0" 
      addr += (hex(esp.MAC_address[i]))[2:4].upper()
      addr += ":"
   
   print("##  " + addr[0:17] + "   ##")
   
   print("##                      ##")
   print("##########################")
   print("##########################")
   ```

[Next Step](step-3){: .btn .btn-blue }
