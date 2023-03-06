---
layout: default
title: "Step 1: Connect to your home Wifi or phone hotspot"
parent: "Connecting To The Internet"
grand_parent: "Tutorials"
---

# Step 1: Connect to your home Wifi or phone hotspot

The easiest way to get your ItsyBitsy Expander connected to the internet is by using a Wifi that you have control over, like your home network or the internet hotspot of your smartphone.

1. Connect your ItsyBitsy to your computer.
2. Open `Mu Editor` and open the file `code.py` on your `CIRCUITPY` memory volume.
3. Copy and paste the code below into your `code.py`, replacing the content that was there before, and click `Save`.

   ```python
   # SPDX-FileCopyrightText: 2019 ladyada for Adafruit Industries
   # SPDX-License-Identifier: MIT
   
   import board
   import busio
   import time
   from digitalio import DigitalInOut
   import adafruit_requests as requests
   import adafruit_esp32spi.adafruit_esp32spi_socket as socket
   from adafruit_esp32spi import adafruit_esp32spi
   
   # Get wifi details and more from a secrets.py file
   try:
      from secrets import secrets
   except ImportError:
      print("WiFi secrets are kept in secrets.py, please add them there!")
      raise
   
   print("ESP32 SPI webclient test")
   
   TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"
   JOKE_URL = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"


   # If you are using a board with pre-defined ESP32 Pins:
   esp32_cs = DigitalInOut(board.D9)
   esp32_ready = DigitalInOut(board.D11)
   esp32_reset = DigitalInOut(board.D12)

   spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
   esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

   requests.set_socket(socket, esp)

   if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
      print("ESP32 found and in idle mode")
   print("Firmware vers.", esp.firmware_version)

   addr =""
   for i in range(len(esp.MAC_address)-1, -1, -1):
      addr += (hex(esp.MAC_address[i]))[2:4].upper()
      addr += ":"

   print("MAC addr:" + addr[0:17] )

   for ap in esp.scan_networks():
      print("\t%s\t\tRSSI: %d" % (str(ap["ssid"], "utf-8"), ap["rssi"]))

   print("Connecting to AP...")
   while not esp.is_connected:
      try:
         esp.connect_AP(secrets["ssid"], secrets["password"])
      except RuntimeError as e:
         print("could not connect to AP, retrying: ", e)
         continue
   print("Connected to", str(esp.ssid, "utf-8"), "\tRSSI:", esp.rssi)
   print("My IP address is", esp.pretty_ip(esp.ip_address))
   print(
      "IP lookup adafruit.com: %s" % esp.pretty_ip(esp.get_host_by_name("adafruit.com"))
   )
   print("\nPing google.com: %d ms" % esp.ping("google.com"))

   # esp._debug = True
   print("\nFetching text from", TEXT_URL)
   r = requests.get(TEXT_URL)
   print("-" * 40)
   print(r.text)
   print("-" * 40)
   r.close()


   while esp.is_connected:
      print()
      print("Fetching a random joke from https://v2.jokeapi.dev")
      r = requests.get(JOKE_URL)
      print("-" * 40)
      joke = r.json()
      
      # Checking for different type of joke, either one-liner or setup and delivery joke
      if "joke" in joke:
         print(joke['joke'])
      else:
               
         print(joke['setup'])
         time.sleep(3)
         print(joke['delivery'])
         
      print("-" * 40)
      r.close()
      time.sleep(5)
      print("Done!")

   ```


4. You will notice that the code does not work yet. First, we have to provide our ItsyBitsy Expander with the right network credentials to connect to a Wifi. Click `New` to create a new file, and paste in the following code. Replace the value for `ssid` with the network name of your phone hotspot or your home network, and the `password` value with the respective network password.
   ```python
   secrets = {
      "ssid": "replace-with-the-network-name",
      "password": "replace-with-the-password",
   }
   ```
5. Click `Save` and choose the `CIRCUITPY` as a destination for the file. Name the file `secrets.py`.
6. Open MU's `Serial Monitor`. If you followed the steps correctly, you will see the ItsyBitsy connect to the network, do a test ping to Google.com, and then deliver a new random joke every 5 seconds.

[Next Step](step-2){: .btn .btn-blue }
