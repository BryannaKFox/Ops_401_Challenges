# Script:                       ops401d10-Challenge02
# Author:                       Bryanna Fox
# Date of latest revision:      1/9/2024
# Purpose:                      Create an Uptime Sensor Tool

import platform
import subprocess
import time
from datetime import datetime
from ping3 import ping

def is_host_up(host):
    try:
        # Using ping3 library to send an ICMP Echo Request packet
        response = ping(host, timeout=1)
        if response is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking {host}: {e}")
        return False

def main():
    destination_ip = "192.168.2.103"

    while True:
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

            # Check if the host is up
            if is_host_up(destination_ip):
                status = "Network Active"
            else:
                status = "Network Inactive"

            # Print the status along with a comprehensive timestamp and destination IP
            print(f"{timestamp} {status} to {destination_ip}")

            # Wait for 2 seconds before the next transmission
            time.sleep(2)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()

