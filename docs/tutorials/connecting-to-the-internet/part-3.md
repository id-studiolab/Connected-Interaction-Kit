---
layout: default
title: "Part 3 - Get Data from the Internet"
parent: "Connecting To The Internet"
grand_parent: "Tutorials"
---

# Part 3 - Get Data from the Internet

1.  With your ItsyBitsy connected to your computer, open the file `secrets.py` that we created in [Step 1: Connect to your home Wifi or phone hotspot](/docs/tutorials/03-connect-to-the-internet/step-1).
2.  Change the `ssid` to `TUD-facility` and fill in the iPSK from [Step 3: Registering your device with TUD-facility](/docs/tutorials/03-connect-to-the-internet/step-3) as a `password`.
    ```python
    secrets = {
        "ssid": "TUD-facility",
        "password": "replace-with-your-iPSK-String",
    }
    ```
3.  Open the file `code.py` and replace the content with code below.
    ```python
    import board
    import busio
    import time
    import digitalio
    import adafruit_requests as requests
    import adafruit_esp32spi.adafruit_esp32spi_socket as socket
    from adafruit_esp32spi import adafruit_esp32spi
     
    # Get WiFi details from your secrets.py file
    from secrets import secrets
       
    joke_url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
       
    # Define the pins used by the BitsyExpander's ESP32 WiFi module:
    esp32_cs = digitalio.DigitalInOut(board.D9)
    esp32_ready = digitalio.DigitalInOut(board.D11)
    esp32_reset = digitalio.DigitalInOut(board.D12)
       
    spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)
       
    requests.set_socket(socket, esp)
       
    if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
        print("\nESP32 WiFi Module found.")
        print("Firmware version:", str(esp.firmware_version, "utf-8"))
       
    print("\nScanning for available networks...\n")
    network_list = []
    for ap in esp.scan_networks():
        network_list.append(str(ap["ssid"], "utf-8"))
          
    if secrets["ssid"] not in network_list:
        print(secrets["ssid"], "not found.\nAvailable networks:", network_list) 
        raise SystemExit(0)
       
    print(secrets["ssid"], "found. Connecting...")
    while not esp.is_connected:
        try:
            esp.connect_AP(secrets["ssid"], secrets["password"])
        except RuntimeError as e:
            print("could not connect to AP, retrying: ", e)
            continue
       
    print("Connected! IP address:", esp.pretty_ip(esp.ip_address))
       
    while esp.is_connected:
        print("\nFetching random joke from https://v2.jokeapi.dev")
        r = requests.get(joke_url)
        joke = r.json()
        print("-" * 40)
             
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
    ```
4. Click `Save` and open MU's `Serial Monitor`. If you followed the steps correctly, you will see the ItsyBitsy connect to the TUD-facility network, do a test ping to Google.com, and then deliver a new random joke every 5 seconds.
