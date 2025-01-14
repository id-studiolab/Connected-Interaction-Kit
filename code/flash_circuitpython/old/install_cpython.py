import os

def is_itsybitsy_m4_connected():
    bootloader_drive_name = "ITSYM4BOOT"
    volumes_path = "/Volumes"
    
    if os.path.exists(volumes_path):
        for entry in os.listdir(volumes_path):
            if entry == bootloader_drive_name:
                return True
    return False

def copy_circuitpython_to_drive():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_directory, "cp")
    bootloader_drive_name = "ITSYM4BOOT"
    volumes_path = "/Volumes"
    destination_path = os.path.join(volumes_path, bootloader_drive_name)

    if not os.path.exists(source_path):
        print(f"Source path {source_path} does not exist.")
        return False

    if not is_itsybitsy_m4_connected():
        print("Itsybitsy M4 is not connected in bootloader mode.")
        return False

    try:
        for item in os.listdir(source_path):
            source_item = os.path.join(source_path, item)
            destination_item = os.path.join(destination_path, item)
            if os.path.isdir(source_item):
                os.makedirs(destination_item, exist_ok=True)
                copy_circuitpython_to_drive()
            else:
                with open(source_item, 'rb') as src_file:
                    with open(destination_item, 'wb') as dest_file:
                        dest_file.write(src_file.read())
        print("CircuitPython copied successfully.")
        return True
    except Exception as e:
        print(f"An error occurred while copying: {e}")
        return False


if __name__ == "__main__":
    if is_itsybitsy_m4_connected():
        print("Itsybitsy M4 is connected in bootloader mode.")
        if copy_circuitpython_to_drive():
            lib_source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
            lib_destination_path = os.path.join("/Volumes", "ITSYM4BOOT", "lib")
            try:
                if os.path.exists(lib_source_path):
                    os.makedirs(lib_destination_path, exist_ok=True)
                    for item in os.listdir(lib_source_path):
                        source_item = os.path.join(lib_source_path, item)
                        destination_item = os.path.join(lib_destination_path, item)
                        if os.path.isdir(source_item):
                            os.makedirs(destination_item, exist_ok=True)
                            # Recursively copy the directory
                            for root, dirs, files in os.walk(source_item):
                                for file in files:
                                    src_file_path = os.path.join(root, file)
                                    dest_file_path = os.path.join(destination_item, os.path.relpath(src_file_path, source_item))
                                    os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                                    with open(src_file_path, 'rb') as src_file:
                                        with open(dest_file_path, 'wb') as dest_file:
                                            dest_file.write(src_file.read())
                        else:
                            with open(source_item, 'rb') as src_file:
                                with open(destination_item, 'wb') as dest_file:
                                    dest_file.write(src_file.read())
                    print("/lib folder copied successfully.")
                else:
                    print(f"Source lib path {lib_source_path} does not exist.")
            except Exception as e:
                print(f"An error occurred while copying the /lib folder: {e}")
    else:
        print("Itsybitsy M4 is not connected in bootloader mode.")
