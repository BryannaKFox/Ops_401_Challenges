# Script:                       opschallange 12
# Author:                       Bryanna Fox
# Date of latest revision:      1/23/2024
# Purpose:                      Security Tool Part 2

#!/usr/bin/env python3

from scapy.all import IP, TCP, ICMP
import ipaddress

def test_port(target_ip, port):
    response = sr1(IP(dst=target_ip) / TCP(dport=port, flags="S"), timeout=1, verbose=0)

    if response and response.haslayer(TCP):
        if response[TCP].flags == 0x12:  # TCP SYN-ACK
            send(IP(dst=target_ip) / TCP(dport=port, flags="R"), verbose=0)
            print(f"Port {port} is open")
        elif response[TCP].flags == 0x14:  # TCP RST-ACK
            print(f"Port {port} is closed")
        else:
            print(f"Port {port} is filtered and silently dropped")
    else:
        print(f"Port {port} is filtered and silently dropped")

def scan_tcp_ports(target_ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        test_port(target_ip, port)

def test_icmp_ping(ip_address):
    try:
        response = sr1(IP(dst=ip_address) / ICMP(), timeout=1, verbose=0)
        if not response:
            print(f"{ip_address} is down or unresponsive.")
        elif response.haslayer(ICMP) and response[ICMP].type == 3 and response[ICMP].code in (1, 2, 3, 9, 10, 13):
            print(f"{ip_address} is actively blocking ICMP traffic.")
        else:
            print(f"{ip_address} is responding.")
    except Exception as e:
        print(f"Error testing ICMP ping for {ip_address}: {e}")

def scan_icmp_ping_sweep(network_address):
    network = ipaddress.IPv4Network(network_address, strict=False)
    online_hosts = 0

    for ip_address in network.hosts():
        ip_address_str = str(ip_address)
        if ip_address != network.network_address and ip_address != network.broadcast_address:
            test_icmp_ping(ip_address_str)
            online_hosts += 1

    print(f"Total online hosts: {online_hosts}")

# User menu
print("1. TCP Port Range Scanner")
print("2. ICMP Ping Sweep")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    # TCP Port Range Scanner mode
    target_ip = input("Enter target IP:")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    scan_tcp_ports(target_ip, start_port, end_port)

elif choice == "2":
    # ICMP Ping Sweep mode
    network_address = input("192.168.1.221")
    scan_icmp_ping_sweep(network_address)

else:
    print("Invalid choice. Exiting.")

