#!/bin/python3

# Import Libraries

from cryptography.fernet import Fernet 
import os
import ctypes
import requests
import tkinter as tk
from tkinter import messagebox

# Define Functions  

# This function generates a key and saves it into a file
def generate_key():
    return Fernet.generate_key()

def load_key(key_path):
    return open(key_path, "rb").read()

def write_key(key, key_path):
    with open(key_path, "wb") as key_file:
        key_file.write(key)

def encrypt_file(filepath, key):

    fernet = Fernet(key)

    with open(filepath, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(filepath, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(filepath, key):
    
    fernet = Fernet(key)

    with open(filepath, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(filepath, "wb") as file:
        file.write(decrypted_data)


def encrypt_message(message, key):

    fernet = Fernet(key)

    encrypted_message = fernet.encrypt(message.encode('utf-8'))
    return encrypted_message


def decrypt_message(encrypted_message, key):
    
    fernet = Fernet(key)

    decrypted_message = fernet.decrypt(encrypted_message.encode('utf-8'))
    return decrypted_message.decode()


def key_file(filepath):
    dir_name, base_name = os.path.split(filepath)
    key_filename = f"key{base_name}"
    key_filepath = os.path.join(dir_name, key_filename)
    return key_filepath


def message_path(filepath):
    message_path = os.path.join(filepath, "encryptedmessage.txt")
    return message_path


def write_message(message, message_path):
    with open(message_path, "wb") as message_file:
        message_file.write(message)


def encrypt_folder(folder_path, message_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)


def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)
    

def folderkey_path(filepath):
    message_path = os.path.join(filepath, "folderkey.txt")
    return message_path


def download_image(url, local_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_path, 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(f"Failed to download image from {url}")

# Creates pop-up with a message for the user
def show_popup():
    message = "Your files have been encrypted! To decrypt your files, follow the instructions in the README file."  # Predefined ransomware message
    # Create a popup window with a ransomware message
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showerror("Ransomware Simulation", message)


# Sets the wallpaper for the ransomware simulation
def set_wallpaper():
    wallpaper_url = "https://image-optimizer.cyberriskalliance.com/unsafe/768x0/https://files.scmagazine.com/wp-content/uploads/2023/10/1020_ransomware.jpg"  # URL of the wallpaper image
    local_path = os.path.join(os.getenv('TEMP'), "wallpaper.jpg")  # Temporary location to save the downloaded image
    
    download_image(wallpaper_url, local_path)
    
    # Change the desktop wallpaper to the specified image and make it permanent
    ctypes.windll.user32.SystemParametersInfoW(20, 0, local_path, 3)

   
# Print the menu
mode = input("""To encrypt a file, enter 1.
To decrypt a file, enter 2. 
To encrypt a message, enter 3. 
To decrypt a message, enter 4. 
To encrypt a folder, enter 5.
To decrypt a folder, enter 6.
To simulate ransomware, enter 7.
Enter your option: """)

if mode == "1":

    filepath = input("Provide a path to the file: ")
    key = generate_key()
    key_filepath = key_file(filepath)

    encrypt_file(filepath, key)
    write_key(key, key_filepath)

    print(f"\nThe file '{filepath}' has been encrypted and overwritten.\n")
    print(f"The key has been saved to '{key_filepath}'\n")
    

elif mode == "2":

    filepath = input("Provide a path to the file:")
    key_filepath = input("Provide the path to the key file: ")
    key = load_key(key_filepath)

    decrypt_file(filepath, key)

    print(f"\nThe file '{filepath}' has been decrypted and overwritten\n")
    

elif mode == "3":
    
    message = input("Provide the cleartext string: ")
    dir_path = input("Provide the directory where the encrypted string and key will be saved: ")

    if not os.path.isdir(dir_path):
        print("\nInvalid directory path.\n")

    else:
        key = generate_key()
        encrypted_message = encrypt_message(message, key)
        dir_message = message_path(dir_path)
        key_filepath = key_file(dir_message)
        
        write_message(encrypted_message, dir_message)
        write_key(key, key_filepath)

    print(f"\nEncrypted message: {encrypted_message.decode('utf-8')}\n")
    print(f"The encrypted string has been saved to: {dir_message}\n")
    print(f"The key has been saved to: {key_filepath}\n")


elif mode == "4":

    encrypted_message = input("Provide the ciphertext string: ")
    key_filepath = input("Provide the path to the key file: ")
    key = load_key(key_filepath)
    decrypted_message = decrypt_message(encrypted_message, key)

    print(f"\nDecrypted message: {decrypted_message}\n")
    

elif mode == "5":

    folder_path = input("Provide the path to the folder: ")
    key_filepath = input("Provide the directory where the key will be saved: ")

    if not os.path.isdir(key_filepath and folder_path):
        print("\nInvalid directory path!\nInvalid directory to save key!\n")

    else:

        key = generate_key()
        encrypt_folder(folder_path, key)
        key_path = folderkey_path(key_filepath)

        write_key(key, key_path)

        print(f"\nThe folder '{folder_path}' and its contents have been encrypted.\n")
        print(f"The key has been saved to '{key_filepath}'\n")


elif mode == "6":
    folder_path = input("Provide the path to the folder: ")
    key_filepath = input("Provide the path to the key file: ")

    if not os.path.isdir(key_filepath and folder_path):
        print("\nInvalid directory path!\nInvalid directory to save the key!\n")

    else: 

        key = load_key(key_filepath)
        decrypt_folder(folder_path, key)

        print(f"\nThe folder '{folder_path}' and its contents have been decrypted.\n")


elif mode == "7":

    set_wallpaper()
    show_popup()

    print("\nRansomware simulation complete!\n")


else:
    print("\nWrong input! Please try again.\n")


