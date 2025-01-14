import os
import time
import shutil
from subprocess import run

# Paths
CIRCUITPYTHON_FILE = "./cp/adafruit-circuitpython-itsybitsy_m4_express-en_US-9.2.1.uf2"
LIBRARY_BUNDLE = "./lib/"

def find_mount(name):
    """Check if a volume is mounted."""
    result = run(["diskutil", "list"], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if name in line:
            return line.split()[-1]  # Return the disk identifier
    return None

def wait_for_mount(name):
    """Wait until a specific volume is mounted."""
    while True:
        mount = find_mount(name)
        if mount:
            return mount
        time.sleep(1)

def copy_file_to_disk(src, dest):
    """Copy file or directory to mounted volume."""
    if os.path.isdir(src):
        shutil.copytree(src, dest, dirs_exist_ok=True)
    else:
        shutil.copy(src, dest)

def main():
    print("Waiting for ITSYM4BOOT...")
    itsym4boot_disk = wait_for_mount("ITSYM4BOOT")
    print(f"Detected ITSYM4BOOT at {itsym4boot_disk}. Copying CircuitPython UF2...")
    
    copy_file_to_disk(CIRCUITPYTHON_FILE, f"/Volumes/ITSYM4BOOT/")
    time.sleep(5)  # Allow time for the board to reset

    print("Waiting for CIRCUITPY...")
    circuitpy_disk = wait_for_mount("CIRCUITPY")
    print(f"Detected CIRCUITPY at {circuitpy_disk}. Copying library bundle...")

    copy_file_to_disk(LIBRARY_BUNDLE, f"/Volumes/CIRCUITPY/")
    time.sleep(2)  # Ensure all data is written

    print("Unmounting CIRCUITPY...")
    run(["diskutil", "unmount", f"/Volumes/CIRCUITPY"])
    print("Process complete.")

if __name__ == "__main__":
    main()
