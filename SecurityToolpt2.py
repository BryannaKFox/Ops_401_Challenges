#!/usr/bin/env python3

# Script:                       opschallange 12
# Author:                       Bryanna Fox
# Date of latest revision:      1/23/2024
# Purpose:                      Security Tool Part 2



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

def icmp_ping_sweep(network_address):
    ip_list = [str(ip) for ip in IP(network_address).hosts()]

    online_hosts = 0

    for ip in ip_list:
        if ip == network_address or ip == IP(network_address).broadcast():
            continue

        response = sr1(IP(dst=ip) / ICMP(), timeout=1, verbose=0)

        if response:
            if response.haslayer(ICMP):
                icmp_type = response[ICMP].type
                icmp_code = response[ICMP].code

                if icmp_type == 3 and icmp_code in [1, 2, 3, 9, 10, 13]:
                    print(f"Host {ip} actively blocking ICMP traffic")
                else:
                    print(f"Host {ip} is responding")
                    online_hosts += 1
        else:
            print(f"Host {ip} is down or unresponsive")

    print(f"\nNumber of online hosts: {online_hosts}")

if __name__ == "__main__":
    print("Choose mode:")
    print("1. TCP Port Range Scanner")
    print("2. ICMP Ping Sweep")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        target_ip = input("Enter target IP address: ")
        port_range = tuple(map(int, input("Enter port range (start end): ").split()))

        open_ports = tcp_port_scan(target_ip, port_range)

        if open_ports:
            print(f"\nOpen ports on {target_ip}: {open_ports}")
        else:
            print(f"\nNo open ports found on {target_ip}")

    elif choice == 2:
        network_address = input("Enter network address with CIDR block (e.g., 10.10.0.0/24): ")
        icmp_ping_sweep(network_address)

    else:
        print("Invalid choice. Please choose 1 or 2.")
