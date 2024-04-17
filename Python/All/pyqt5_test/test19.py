import psutil

def bytes_to_gb(bytes_value):
    gb_value = bytes_value / (1024 ** 3)
    return gb_value

def get_connected_flash_drives():
    flash_drives = []
    
    # Iterate over all disk partitions
    for partition in psutil.disk_partitions():
        if "removable" in partition.opts:
            flash_drives.append(partition.device)

    return flash_drives

def get_drive_space_info(drive):
    try:
        usage = psutil.disk_usage(drive)
        total_space = usage.total
        used_space = usage.used
        free_space = usage.free

        return total_space, used_space, free_space
    except Exception as e:
        print(f"Error getting disk space info for {drive}: {e}")
        return None, None, None

def main():
    flash_drives = get_connected_flash_drives()
    
    if not flash_drives:
        print("No flash drives found.")
        return

    for drive in flash_drives:
        total_space, used_space, free_space = get_drive_space_info(drive)
        total_space_gb = bytes_to_gb(total_space)
        used_space_gb = bytes_to_gb(used_space)
        free_space_gb = bytes_to_gb(free_space)

        print(f"Drive: {drive}")
        print(f"Total Space: {total_space_gb:.2f} GB")
        print(f"Used Space: {used_space_gb:.2f} GB")
        print(f"Free Space: {free_space_gb:.2f} GB")
        print()

if __name__ == "__main__":
    main()
