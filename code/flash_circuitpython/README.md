# Flash CircuitPython

A macOS script for flashing CircuitPython firmware and the library bundle onto **StudioLab PicoExpander** boards. Designed for batch production of the Connected Interaction Kit — plug in a board, wait for the beep, repeat.

On each run the script checks for the latest stable firmware and libraries and downloads them automatically before flashing.

---

## What it does

1. Fetches the latest stable CircuitPython UF2 from the [Adafruit S3 bucket](https://adafruit-circuit-python.s3.amazonaws.com/index.html?prefix=bin/studiolab_picoexpander/en_GB/) (cached locally, only re-downloaded when a newer version is available)
2. Fetches the matching library bundle from the [CIK-Project-Bundle releases](https://github.com/id-studiolab/CIK-Project-Bundle/releases/latest) (cached locally by release tag)
3. Waits for a board to appear in bootloader mode (`RPI-RP2`)
4. Copies the CircuitPython UF2 to flash it
5. Waits for the board to reboot as `CIRCUITPY`
6. Wipes all existing files from the board
7. Copies the library bundle to `/lib` on the board
8. Unmounts the drive and plays a confirmation sound
9. Loops back and waits for the next board

---

## Requirements

- macOS (uses `diskutil` and `afplay`)
- Python 3 (standard library only — no extra packages needed)

---

## Usage

Put the board into bootloader mode by double-pressing the reset button. The board will mount as `RPI-RP2`.

Run the script from the `flash_circuitpython` directory:

```bash
python flash_cp.py
```

The script checks for firmware and library updates once on startup, then runs in a continuous loop. Once a board is done (confirmed by the Glass sound), unplug it and plug in the next one.

---

## Folder structure

```
flash_circuitpython/
├── flash_cp.py       # Main flashing script
├── cp/               # Cached firmware (auto-populated on first run)
│   └── adafruit-circuitpython-studiolab_picoexpander-en_GB-X.Y.Z.uf2
├── lib/              # Cached library bundle (auto-populated on first run)
│   ├── .version      # Tracks the installed bundle release tag
│   └── lib/          # Copied to /lib on the board
│       ├── adafruit_*/
│       ├── neopixel.py
│       └── ...
└── old/              # Previous versions of the script
```

Both `cp/` and `lib/` are populated automatically on first run. Stale firmware files are replaced whenever a newer stable release is found.

---

## Sources

| Asset | Source |
|---|---|
| CircuitPython firmware | `adafruit-circuit-python.s3.amazonaws.com` → `bin/studiolab_picoexpander/en_GB/` |
| Library bundle | `github.com/id-studiolab/CIK-Project-Bundle` → latest release, `X.x-mpy` variant |
