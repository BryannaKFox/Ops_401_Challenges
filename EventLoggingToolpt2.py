#!/usr/bin/env python3

# Script:                       opschallange 27
# Author:                       Bryanna Fox
# Date of latest revision:      2/13/2024
# Purpose:                      Event Logging Tool Part 2 (using the Brute Force Script)

import logging
from logging.handlers import RotatingFileHandler
import time

# Configure logging with RotatingFileHandler
log_file = 'script.log'
max_log_size_bytes = 1024 * 1024  # 1 MB
backup_count = 3  # Number of backup log files
handler = RotatingFileHandler(log_file, maxBytes=max_log_size_bytes, backupCount=backup_count)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(handler)

def offensive_mode(word_list_file):
    try:
        with open(word_list_file, 'r') as f:
            for word in f:
                word = word.strip()  
                print(word)
                time.sleep(0.5)  
    except FileNotFoundError:  # Error handling: file not found
        logging.error(f"The file '{word_list_file}' was not found.")
    except Exception as e:  # General error handling
        logging.error(f"An error occurred in offensive_mode: {str(e)}")

def defensive_mode(search_string, word_list_file):
    try:
        with open(word_list_file, 'r') as f:
            word_list = [line.strip() for line in f]

        if search_string in word_list:
            print(f"The string '{search_string}' was found in the word list.")
        else:
            print(f"The string '{search_string}' was not found in the word list.")
    except FileNotFoundError:  # Error handling: file not found
        logging.error(f"The file '{word_list_file}' was not found.")
    except Exception as e:  # General error handling
        logging.error(f"An error occurred in defensive_mode: {str(e)}")

if __name__ == "__main__":
    try:
        # Log program start
        logging.info("Program started.")

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
            logging.warning("Invalid mode selected.")
    except Exception as e:  # General error handling
        logging.error(f"An error occurred: {str(e)}", exc_info=True)
    finally:
        # Log program end
        logging.info("Program ended.")

# Resources used:
# For this script I used and added on logging to the original script that I created in from lab 16. https://github.com/BryannaKFox/Ops_401_Challenges/blob/main/BruteForce.py
# I also added to my previous script EventLoggingToolpt1. https://github.com/BryannaKFox/Ops_401_Challenges/blob/main/EventLoggingToolpt1.py 