import psutil
import wmi

def get_remote_ram_usage(ip_address, username, password):
    try:
        c = wmi.WMI(ip_address, user=username, password=password)
        for os in c.Win32_OperatingSystem():
            total_physical_memory = int(os.TotalVisibleMemorySize)
            free_physical_memory = int(os.FreePhysicalMemory)
            used_physical_memory = total_physical_memory - free_physical_memory
            return {
                "total_physical_memory": total_physical_memory,
                "used_physical_memory": used_physical_memory,
                "free_physical_memory": free_physical_memory
            }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    ip_address = input("Enter the IP Address of the remote Windows PC: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    ram_usage = get_remote_ram_usage(ip_address, username, password)

    if "error" in ram_usage:
        print("Error:", ram_usage["error"])
    else:
        print("Total Physical Memory:", ram_usage["total_physical_memory"], "KB")
        print("Used Physical Memory:", ram_usage["used_physical_memory"], "KB")
        print("Free Physical Memory:", ram_usage["free_physical_memory"], "KB")
