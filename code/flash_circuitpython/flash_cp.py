import os
import re
import time
import json
import shutil
import zipfile
import tempfile
from subprocess import run
from urllib.request import urlretrieve, urlopen
import xml.etree.ElementTree as ET

# Board
BOOT_VOLUME = "RPI-RP2"
CIRCUITPY_VOLUME = "CIRCUITPY"

# Sources
CP_S3_BASE = "https://adafruit-circuit-python.s3.amazonaws.com"
CP_S3_PREFIX = "bin/studiolab_picoexpander/en_GB/"
BUNDLE_REPO = "id-studiolab/CIK-Project-Bundle"

# Local cache dirs
CP_DIR = "./cp"
LIB_DIR = "./lib"


# --- Firmware ---

def get_latest_stable_uf2():
    """Return (version_tuple, filename, s3_key) for the latest stable UF2."""
    url = f"{CP_S3_BASE}/?prefix={CP_S3_PREFIX}"
    with urlopen(url) as resp:
        root = ET.fromstring(resp.read())
    ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}

    stable = []
    for content in root.findall("s3:Contents", ns):
        key = content.find("s3:Key", ns).text
        filename = key.split("/")[-1]
        # Stable releases match X.Y.Z with no suffix (no -alpha, -beta, -rc, etc.)
        m = re.match(r".+-en_GB-(\d+\.\d+\.\d+)\.uf2$", filename)
        if m:
            version = tuple(int(x) for x in m.group(1).split("."))
            stable.append((version, filename, key))

    if not stable:
        raise RuntimeError("No stable CircuitPython releases found on S3")
    return max(stable)


def ensure_firmware():
    """Download the latest stable firmware if not already cached. Returns (local_path, cp_major)."""
    os.makedirs(CP_DIR, exist_ok=True)
    version, filename, key = get_latest_stable_uf2()
    dest = os.path.join(CP_DIR, filename)

    if os.path.exists(dest):
        print(f"Firmware up to date: {filename}")
        return dest, version[0]

    # Remove stale firmware files
    for f in os.listdir(CP_DIR):
        if f.endswith(".uf2"):
            os.unlink(os.path.join(CP_DIR, f))

    version_str = ".".join(str(v) for v in version)
    print(f"Downloading CircuitPython {version_str}...")
    urlretrieve(f"{CP_S3_BASE}/{key}", dest)
    print(f"  -> {filename}")
    return dest, version[0]


# --- Libraries ---

def get_bundle_asset(cp_major):
    """Return (download_url, tag) for the latest bundle matching the CP major version."""
    url = f"https://api.github.com/repos/{BUNDLE_REPO}/releases/latest"
    with urlopen(url) as resp:
        release = json.load(resp)
    tag = release["tag_name"]
    for asset in release["assets"]:
        name = asset["name"]
        if f"{cp_major}.x-mpy" in name and name.endswith(".zip"):
            return asset["browser_download_url"], tag
    raise RuntimeError(f"No {cp_major}.x-mpy bundle in release {tag}")


def ensure_libraries(cp_major):
    """Download and extract the latest library bundle if not already cached."""
    os.makedirs(LIB_DIR, exist_ok=True)
    bundle_url, tag = get_bundle_asset(cp_major)

    version_file = os.path.join(LIB_DIR, ".version")
    if os.path.exists(version_file):
        with open(version_file) as f:
            if f.read().strip() == tag:
                print(f"Libraries up to date: {tag}")
                return

    print(f"Downloading library bundle {tag}...")
    with tempfile.TemporaryDirectory() as tmp:
        zip_path = os.path.join(tmp, "bundle.zip")
        urlretrieve(bundle_url, zip_path)

        extract_dir = os.path.join(tmp, "extracted")
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(extract_dir)

        # Bundles extract to a top-level folder; find lib/ inside it
        lib_src = None
        for entry in os.listdir(extract_dir):
            candidate = os.path.join(extract_dir, entry, "lib")
            if os.path.isdir(candidate):
                lib_src = candidate
                break
        if lib_src is None:
            candidate = os.path.join(extract_dir, "lib")
            if os.path.isdir(candidate):
                lib_src = candidate
        if lib_src is None:
            raise RuntimeError("Could not find lib/ folder inside bundle zip")

        lib_dest = os.path.join(LIB_DIR, "lib")
        if os.path.exists(lib_dest):
            shutil.rmtree(lib_dest)
        shutil.copytree(lib_src, lib_dest)

    with open(version_file, "w") as f:
        f.write(tag)
    print(f"  -> Libraries updated to {tag}")


# --- Flashing ---

def find_mount(name):
    result = run(["diskutil", "list"], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if name in line:
            return line.split()[-1]
    return None


def wait_for_mount(name):
    while not find_mount(name):
        time.sleep(1)


def copy_to_disk(src, dest):
    if os.path.isdir(src):
        shutil.copytree(src, dest, dirs_exist_ok=True)
    else:
        shutil.copy(src, dest)


def wipe_disk(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except PermissionError as e:
            print(f"  Skipping {item_path}: {e}")


def flash_board(firmware_path):
    print(f"Waiting for {BOOT_VOLUME} (double-press reset)...")
    wait_for_mount(BOOT_VOLUME)
    print("  -> Detected. Flashing CircuitPython...")
    copy_to_disk(firmware_path, f"/Volumes/{BOOT_VOLUME}/")
    time.sleep(5)

    print(f"Waiting for {CIRCUITPY_VOLUME}...")
    wait_for_mount(CIRCUITPY_VOLUME)
    print("  -> Detected. Wiping and copying libraries...")
    wipe_disk(f"/Volumes/{CIRCUITPY_VOLUME}/")
    lib_src = os.path.join(LIB_DIR, "lib")
    copy_to_disk(lib_src, f"/Volumes/{CIRCUITPY_VOLUME}/lib")
    time.sleep(2)

    run(["diskutil", "unmount", f"/Volumes/{CIRCUITPY_VOLUME}"])
    print("Done.")
    run(["afplay", "/System/Library/Sounds/Glass.aiff"])


def main():
    print("=== CIK Board Flasher ===\n")
    print("Checking for updates...")
    firmware_path, cp_major = ensure_firmware()
    ensure_libraries(cp_major)
    print()
    while True:
        flash_board(firmware_path)
        print("Ready for next board.\n")


if __name__ == "__main__":
    main()
