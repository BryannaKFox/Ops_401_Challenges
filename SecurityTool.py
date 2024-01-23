# Script:                       opschallange 11
# Author:                       Bryanna Fox
# Date of latest revision:      1/22/2024
# Purpose:                      Security Tool

from scapy.all import *

def tcp_port_scan(target_ip, port_range):
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        response = sr1(IP(dst=target_ip) / TCP(dport=port, flags="S"), timeout=1, verbose=0)

        if response and response.haslayer(TCP):
            if response[TCP].flags == 0x12:  # TCP SYN-ACK
                open_ports.append(port)
                send(IP(dst=target_ip) / TCP(dport=port, flags="R"), verbose=0)  # Send RST to close the connection
                print(f"Port {port} is open")
            elif response[TCP].flags == 0x14:  # TCP RST-ACK
                print(f"Port {port} is closed")
            else:
                print(f"Port {port} is filtered and silently dropped")
        else:
            print(f"Port {port} is filtered and silently dropped")

    return open_ports

if __name__ == "__main__":
    target_ip = "10.0.2.5" #Target Ip address
    port_range = (1, 50)  #Target ports to scan

    open_ports = tcp_port_scan(target_ip, port_range)

    if open_ports:
        print(f"Open ports on {target_ip}: {open_ports}")
    else:
        print(f"No open ports found on {target_ip}")
