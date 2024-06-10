import sys
import time
import re 

def file_iteration(file):

	with open(file, "r") as password_list:
		for password in password_list:
			password = password.strip("\n")
			print(password)
			time.sleep(1)

def string_search(string, file):

	with open(file, "r") as password_list:
		for password in password_list:
			password = password.strip("\n")

			if(string.lower() == password):

				print("\nThe string you entered is in the provided password list!")
				print("\n")
				sys.exit(0)

		print("\nThe string you entered is not in the provided pasword list!")
		print("The program will no exit...")
		sys.exit(0)


def evaluate_password(password, length_req, caps_req, nums_req, syms_req):

    length = len(password)
    caps = len(re.findall(r'[A-Z]', password))
    nums = len(re.findall(r'[0-9]', password))
    syms = len(re.findall(r'[^A-Za-z0-9]', password))
    
    length_met = length >= length_req
    caps_met = caps >= caps_req
    nums_met = nums >= nums_req
    syms_met = syms >= syms_req

    print(f"\nPassword length: {length} (Required: {length_req}) - {'Met' if length_met else 'Not Met'}")
    print(f"Capital letters: {caps} (Required: {caps_req}) - {'Met' if caps_met else 'Not Met'}")
    print(f"Numbers: {nums} (Required: {nums_req}) - {'Met' if nums_met else 'Not Met'}")
    print(f"Symbols: {syms} (Required: {syms_req}) - {'Met' if syms_met else 'Not Met'}")

    if length_met and caps_met and nums_met and syms_met:

        print("\nSUCCESS: Your password meets all the complexity requirements!\n")

    else:

        print("\nFAILURE: Your password does not meet all the complexity requirements.\n")


mode = input("""To iterate through list enter 1.
To input a string and compare with list enter 2.
To evaluate a password for complexity enter 3.
Choose your option: """)

if mode == "1":
    
    file = input("Please enter the password list name (ex. password.txt): ")
    
    file_iteration(file)
    
elif mode == "2":
    
    string = input("Please provide the string used for the search: ")
    file = input("Please enter the password list name (ex. password.txt): ")
    
    string_search(string, file)

elif mode == "3":
    
    password = input("Please provide the password to evaluate: ")
    length_req = int(input("Required minimum length of the password: "))
    caps_req = int(input("Required minimum number of capital letters: "))
    nums_req = int(input("Required minimum number of numbers: "))
    syms_req = int(input("Required minimum number of symbols: "))
    
    evaluate_password(password, length_req, caps_req, nums_req, syms_req)
    
else:
    
    print("Wrong input! Exiting program..")
    sys.exit(1)

