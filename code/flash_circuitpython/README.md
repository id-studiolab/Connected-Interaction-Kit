# Flash CircuitPython

A macOS script for flashing CircuitPython firmware and the library bundle onto **Adafruit ItsyBitsy M4 Express** boards. Designed for batch production of the Connected Interaction Kit — plug in a board, wait for the beep, repeat.

---

## What it does

1. Waits for a board to appear in bootloader mode (`ITSYM4BOOT`)
2. Copies the CircuitPython UF2 firmware to flash it
3. Waits for the board to reboot as `CIRCUITPY`
4. Wipes all existing files from the board
5. Copies the full library bundle to the board
6. Unmounts the drive and plays a confirmation sound
7. Loops back and waits for the next board

---

## Requirements

- macOS (uses `diskutil` and `afplay`)
- Python 3
- No additional Python packages needed (uses standard library only)

---

## Usage

Put the board into bootloader mode by double-pressing the reset button. The board will mount as `ITSYM4BOOT`.

Then run the script from the `flash_circuitpython` directory:

```bash
python flash_cp.py
```

The script runs in a continuous loop. Once a board is done (confirmed by the Glass sound), unplug it and plug in the next one.

---

## Folder structure

```
flash_circuitpython/
├── flash_cp.py                  # Main flashing script
├── cp/
│   └── adafruit-circuitpython-itsybitsy_m4_express-en_US-9.2.1.uf2
├── lib/
│   └── lib/                     # Copied to /lib on the board
│       ├── adafruit_bus_device/
│       ├── adafruit_debouncer.py
│       ├── adafruit_dotstar.py
│       ├── adafruit_esp32spi/
│       ├── adafruit_hid/
│       ├── adafruit_minimqtt/
│       ├── adafruit_motor/
│       ├── adafruit_motorkit.py
│       ├── adafruit_pca9685.py
│       ├── adafruit_pixelbuf.py
│       ├── adafruit_register/
│       ├── adafruit_requests.py
│       ├── adafruit_servokit.py
│       ├── adafruit_vl53l0x.py
│       ├── neopixel.py
│       └── ...
└── old/                         # Previous versions of the script
```

---

## Updating the firmware or libraries

- **Firmware:** Replace the `.uf2` file in `cp/` and update the `CIRCUITPYTHON_FILE` path in `flash_cp.py`.
- **Libraries:** Add, remove, or update files in `lib/lib/`. The entire folder is synced to the board on each flash.
