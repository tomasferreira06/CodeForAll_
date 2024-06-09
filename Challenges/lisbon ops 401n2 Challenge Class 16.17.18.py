import sys
import time

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

mode = input("""To iterate through list enter 1.
To input a string and compare with list enter 2.
Choose your option: """)

if mode == "1":
    
    file = input("Please enter the password list name (ex. password.txt): ")
    
    file_iteration(file)
    
elif mode == "2":
    
    string = input("Please provide the string used for the search: ")
    file = input("Please enter the password list name (ex. password.txt): ")
    
    string_search(string, file)
    
else:
    
    print("Wrong input! Exiting program..")
    sys.exit(1)

