#!/bin/python3

# Import Libraries

from cryptography.fernet import Fernet 
import os

# Define Functions  

# This function generates a key and saves it into a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb")as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb").read()

def encrypt_file(filepath, key):

    fernet = Fernet(key)

    with open(filepath, "rb") as file:
        file_data = file.read()

        encrypted_data = fernet.encrypt(file_data)

        with open(filepath, "wb") as file:
            file.write(encrypted_data)

if not os.path.exists("key.key"):
    write_key()

    key = load_key()

# Print the menu

mode = input("""To encrypt a file, enter 1.
To decrypt a file, enter 2. 
To encrypt a message, enter 3. 
To decrypt a message, enter 4. 
Enter your option: """)

if mode == "1":
    filepath = input("Provide a path to the file: ")

    encrypt_file(filepath, key)
    print(f"The file '{filepath}' has been encrypted and overwritten.")

elif mode == "2":
    print("Provide a path to the file: ")


elif mode == "3":
    print("Provide the cleartext string: ")


elif mode == "4":
    print("Provide the ciphertext string: ")


else:
    print("Wrong input! Please try again.")


