# Script:                       opschallange 06
# Author:                       Bryanna Fox
# Date of latest revision:      1/16/2024
# Purpose:                      File Encryption

from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def load_key(key_path='secret.key'):
    return open(key_path, 'rb').read()

def save_key(key, key_path='secret.key'):
    with open(key_path, 'wb') as key_file:
        key_file.write(key)

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)

    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open(file_path[:-4], 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message.decode())
    return decrypted_message

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

    mode = int(input("Enter mode (1-4): "))

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
        encrypted_message = encrypt_message(message, key)
        print("Encrypted message:", encrypted_message)
    elif mode == 4:
        encrypted_message = input("Enter the encrypted message: ")
        decrypted_message = decrypt_message(encrypted_message, key)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid mode. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
