#!/bin/python3

# Import Libraries

from cryptography.fernet import Fernet 

# Define Functions  

# This function generates a key and saves it into a file
def write_key():
    key = Fernet.generate_key()









print("To encrypt a file, enter 1.")
print("To decrypt a file, enter 2.")
print("To encrypt a message, enter 3.")
print("To decrypt a message, enter 4.")

mode = input("Enter your option: ")

if mode == "1":
    print("Provide a path to the file: ")


elif mode == "2":
    print("Provide a path to the file: ")


elif mode == "3":
    print("Provide the cleartext string: ")


elif mode == "4":
    print("Provide the ciphertext string: ")


else:
    print("Wrong input! Please try again.")


