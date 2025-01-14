import os
import time

root_watch_path = "/Volumes" if os.name == "posix" else "E:\\\\"  # Adjust for your system

while True:
    drives = os.listdir(root_watch_path)
    print(f"Mounted drives: {drives}")
    if any("ITSYBOOT" in drive.upper() for drive in drives):
        print("ItsyBitsy M4 detected in UF2 mode!")
        break
    time.sleep(2)
