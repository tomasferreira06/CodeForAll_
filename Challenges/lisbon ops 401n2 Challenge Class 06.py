#!/bin/python3

print("To encrypt a file, enter 1.")
print("To decrypt a file, enter 2.")
print("To encrypt a message, enter 3.")
print("To decrypt a message, enter 4.")

mode = input("Enter your option: ")

if mode == 1:
    print("Provide path")
elif mode == 2:
    print("provide path")
elif mode == 3:
    print("provide cleartext")
elif mode == 4:
    print("provide ciphertext")
else:
    print("Wrong input! Please try again.")


