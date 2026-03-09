---
layout: default
title: "Part 3 - Connect to a WiFi Network"
parent: "Connecting To The Internet"
grand_parent: "Tutorials"
---

# Part 3 - Connect to a WiFi Network

{:.note}
If you prefer to use a `settings.py` file please follow [this page](part-3old)

To connect your microcontroller to a network, you must provide a network name (SSID) and password. However, directly using sensitive data like WiFi passwords in your code is risky. Therefore, creating a separate file to hold your personal keys and passwords outside your `code.py` file is a good idea. This way, you can share your code without revealing sensitive data to others.

1. On your picoexpander there is a settings.toml file. Open this file in a **text-editor**. Unfortunately you can not use Mu Editor to do this.

2. Copy and paste the following code to the new file, replacing `network-name` with the name of your WiFi network and `network-passwd` with your network's password (or the iPSK generated during [part two](part-2) when connecting to TUD-facility).

```python
CIRCUITPY_WIFI_SSID = "network-name"
CIRCUITPY_WIFI_PASSWORD = "network-password"
```
3. Save your `settings.toml` file.

4. Enter your `code.py` file and replace the code you wrote in [part one](part-1) with the code below, then hit **Save**.
{% tabs data-struct %}

{% tab data-struct PicoExpander %}
```python
import time
import wifi
import socketpool
import ipaddress
import os

print("Raspberry Pi Pico 2 W Connection Test")
print("*" * 40)

print("\nScanning for available networks...")
network_list = []

# Scan for networks (native method)
# start_scanning_networks returns an iterable, so we loop through it
for network in wifi.radio.start_scanning_networks():
    if network.ssid: # Filter out hidden/empty SSIDs
        network_list.append(network.ssid)
wifi.radio.stop_scanning_networks()

# Check if your target SSID was found in the scan
if os.getenv("CIRCUITPY_WIFI_SSID") not in network_list:
    print(os.getenv("CIRCUITPY_WIFI_SSID"), "not found.\nAvailable networks:", network_list)
    # In CircuitPython, SystemExit doesn't always stop the code effectively in IDEs,
    # but we will keep it to match your logic.
    raise SystemExit(0)

print(os.getenv("CIRCUITPY_WIFI_SSID"), "found. Connecting...")

# Connection Loop
while not wifi.radio.ipv4_address:
    try:
        # Connect to the WiFi network
        wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
    except Exception as e:
        print("\nUnable to establish connection. Are you using a valid password?")
        print("Error message:", e, "\nRetrying...")
        time.sleep(2) # Short pause before retry
        continue

print("Connected! IP address:", wifi.radio.ipv4_address)

# Create a SocketPool to resolve domain names (DNS)
pool = socketpool.SocketPool(wifi.radio)

while True:
    print("\nPinging google.com...")
    try:
        # 1. Resolve domain name to IP address
        # getaddrinfo returns a list of info; we grab the first IP address found
        info = pool.getaddrinfo("google.com", 80)
        google_ip_str = info[0][4][0]
        google_ip = ipaddress.ip_address(google_ip_str)
        
        # 2. Ping the IP address
        # wifi.radio.ping returns time in seconds (float) or None if timeout
        response_s = wifi.radio.ping(google_ip)
        
        if response_s is not None:
            # Convert seconds to milliseconds to match your original format
            ms = response_s * 1000
            print(f"Ping successful. Response time: {ms:.1f} ms")
        else:
            print("Ping timed out.")
            
    except Exception as e:
        print("Ping failed with error:", e)

    time.sleep(5)
```
{% endtab %}

{% tab data-struct BitsyExpander %}
```python
import board
import busio
import time
import digitalio
from adafruit_esp32spi import adafruit_esp32spi
import os

# Define the pins used by the BitsyExpander's ESP32 WiFi module
esp32_cs = digitalio.DigitalInOut(board.D9)
esp32_ready = digitalio.DigitalInOut(board.D11)
esp32_reset = digitalio.DigitalInOut(board.D12)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

# Initialize the ESP32 WiFi module
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
    print("\nESP32 WiFi Module found.")
    print("Firmware version:", str(esp.firmware_version, "utf-8"))
    print("*" * 40)

print("\nScanning for available networks...\n")
network_list = [str(ap["ssid"], "utf-8") for ap in esp.scan_networks()]    
if os.getenv("CIRCUITPY_WIFI_SSID") not in network_list:
    print(os.getenv("CIRCUITPY_WIFI_SSID"), "not found.\nAvailable networks:", network_list) 
    raise SystemExit(0)
         
print(settings["ssid"], "found. Connecting...")
while not esp.is_connected:
    try:
        esp.connect_AP(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
    except (RuntimeError, ConnectionError) as e:
        print("\nUnable to establish connection. Are you using a valid password?")
        print("Error message:", e, "\nRetrying...")
        continue
         
print("Connected! IP address:", esp.pretty_ip(esp.ip_address))
          
while True:
    print("\nPinging google.com...")
    response = esp.ping("google.com")
    print("Ping successful. Response time:", response, "ms")
    time.sleep(5)
```
{% endtab %}

{% endtabs %}



5. Open Mu's `Serial Monitor` to verify that the microcontroller successfully connects to the chosen network and can get a response from `google.com`.

6. Note the differences from the code you encountered in [part one](part-1) of this tutorial:

      - The network scan has been moved out of the `while True:` loop and is performed once before entering the loop.
      - The code verifies the network you configured is available and waits for the successful establishment of a connection.
      - The content of the `while True:` loop has been replaced: It now pings google.com and reports the response time. This confirms internet connectivity for your microcontroller.

---

{: .highlight }
> Your microcontroller is now ready for connecting to the internet or even other microcontroller's! Good luck with your connected projects ;-)
