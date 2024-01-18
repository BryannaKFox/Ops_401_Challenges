# Script:                       opschallange 07
# Author:                       Bryanna Fox
# Date of latest revision:      1/17/2024
# Purpose:                      File Encryption Part 2 

from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def load_key(key_path='secret.key'):
    return open(key_path, 'rb').read()

def save_key(key, key_path='secret.key'):
    with open(key_path, 'wb') as key_file:
        key_file.write(key)
#the encrypt_data and decrypt_data is added to handle the encryption and decryption of data using Fernet key. 
def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data

def decrypt_data(data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(data)
    return decrypted_data

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    encrypted_data = encrypt_data(data, key)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = decrypt_data(encrypted_data, key)

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
#the 2 below encrypt_folder and decrypt_folder was added for to recursively encrypt and decrypt the folders. 
def encrypt_folder(folder_path, key):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            encrypt_file(file_path, key)

def decrypt_folder(folder_path, key):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            decrypt_file(file_path, key)

def main():
    key_path = 'secret.key'

    try:
        key = load_key(key_path)
    except FileNotFoundError:
        key = generate_key()
        save_key(key, key_path)

    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    #I added modes 5 and 6 to for the additional options. 
    print("5. Recursively encrypt a folder")
    print("6. Recursively decrypt a folder")

    mode = int(input("Enter mode (1-6): "))

    if mode == 1:
        file_path = input("Enter the path of the file to encrypt: ")
        encrypt_file(file_path, key)
        print("File encrypted successfully.")
    elif mode == 2:
        file_path = input("Enter the path of the file to decrypt: ")
        decrypt_file(file_path, key)
        print("File decrypted successfully.")
    elif mode == 3:
        message = input("Enter the message to encrypt: ")
        encrypted_message = encrypt_data(message.encode(), key)
        print("Encrypted message:", encrypted_message)
    elif mode == 4:
        encrypted_message = input("Enter the encrypted message: ")
        decrypted_message = decrypt_data(encrypted_message.encode(), key).decode()
        print("Decrypted message:", decrypted_message)
    # I added the responses for mode 5 and 6 and the output that would display when the selections are selected. 
    elif mode == 5:
        folder_path = input("Enter the path of the folder to recursively encrypt: ")
        encrypt_folder(folder_path, key)
        print("Folder recursively encrypted successfully.")
    elif mode == 6:
        folder_path = input("Enter the path of the folder to recursively decrypt: ")
        decrypt_folder(folder_path, key)
        print("Folder recursively decrypted successfully.")
    else:
        print("Invalid mode. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
