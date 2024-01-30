# Script:                       opschallange 16
# Author:                       Bryanna Fox
# Date of latest revision:      1/29/2024
# Purpose:                      Brute Force Attack part 1

#!/usr/bin/env python3

import time

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

if __name__ == "__main__":
    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    mode = input("Enter mode number: ")

    if mode == "1":
        word_list_file = input("Enter the word list file path: ")
        offensive_mode(word_list_file)
    elif mode == "2":
        search_string = input("Enter the string to search: ")
        word_list_file = input("Enter the word list file path: ")
        defensive_mode(search_string, word_list_file)
    else:
        print("Invalid mode selected. Please choose 1 or 2.")
