# Needed Modules
import secrets
import sys
import time
import string


#The Random Letters and Digits
letters = string.ascii_letters + string.digits

# Welcoming :) 
print("Welcome To The Secure Password Generator...")
time.sleep(1)

# Variables to Define 
length = input("Length of Pass: ")
amount = input("Generate Multi Amount Of Passes Y/N:  ")

# Generate the Password
def passwordGenerate():
    password = ''.join(secrets.choice(letters) for i in range(int(length)))
    print(str(password))

# Conditional Statement 
try:
    if amount.lower() == "y":
        while True:
            time.sleep(1)
            passwordGenerate()
    else:
        sys.exit("Exiting System...")
except KeyboardInterrupt:
    sys.exit("Exiting System...")



