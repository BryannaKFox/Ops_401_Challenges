#!/usr/bin/env python3

# Script:                       opschallange 36
# Author:                       Bryanna Fox
# Date of latest revision:      2/26/2024
# Purpose:                      Creating a Web Application Fingerprinting

import subprocess

def banner_grabbing_netcat(target_address, port):
    try:
        # Execute netcat command to perform banner grabbing
        result = subprocess.check_output(['nc', '-vz', target_address, str(port)])
        print("Banner Grabbing with netcat:")
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e.output.decode())

def banner_grabbing_telnet(target_address, port):
    try:
        # Execute telnet command to perform banner grabbing
        result = subprocess.check_output(['telnet', target_address, str(port)])
        print("Banner Grabbing with telnet:")
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e.output.decode())

def banner_grabbing_nmap(target_address):
    try:
        # Execute nmap command to perform banner grabbing
        result = subprocess.check_output(['nmap', '-Pn', '-sV', target_address])
        print("Banner Grabbing with Nmap:")
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e.output.decode())

def main():
    target_address = input("Enter the target URL or IP address: ")
    port = input("Enter the port number: ")

    banner_grabbing_netcat(target_address, port)
    banner_grabbing_telnet(target_address, port)
    banner_grabbing_nmap(target_address)

if __name__ == "__main__":
    main()
