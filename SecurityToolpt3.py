# Script:                       opschallange 13
# Author:                       Bryanna Fox
# Date of latest revision:      1/24/2024
# Purpose:                      Security Tool Part 3

#!/usr/bin/env python3

from scapy.all import *

def tcp_port_scan(target_ip, port_range):
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        response = sr1(IP(dst=target_ip) / TCP(dport=port, flags="S"), timeout=1, verbose=0)

        if response and response.haslayer(TCP):
            if response[TCP].flags == 0x12:  # TCP SYN-ACK
                open_ports.append(port)
                print(f"Port {port} is open")
                send(IP(dst=target_ip) / TCP(dport=port, flags="R"), verbose=0)  # Send RST to close the connection
            elif response[TCP].flags == 0x14:  # TCP RST-ACK
                print(f"Port {port} is closed")
            else:
                print(f"Port {port} is filtered and silently dropped")
        else:
            print(f"Port {port} is filtered and silently dropped")

    return open_ports

def combined_scan(target_ip):
    response = sr1(IP(dst=target_ip) / ICMP(), timeout=1, verbose=0)

    if response:
        print(f"\nHost {target_ip} is responding to ICMP echo requests.")
        port_range = tuple(map(int, input("Enter port range (start end): ").split()))
        open_ports = tcp_port_scan(target_ip, port_range)

        if open_ports:
            print(f"\nOpen ports on {target_ip}: {open_ports}")
        else:
            print(f"\nNo open ports found on {target_ip}")
    else:
        print(f"\nHost {target_ip} is down or unresponsive to ICMP echo requests.")

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    combined_scan(target_ip)
