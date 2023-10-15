import random
import string

#Ask for the length of the password
password_length = int(input("Enter password length: "))

#The program will choose random characters
password_chars = string.ascii_letters + string.digits + '!@#$%&*?'
password = random.choices(password_chars, k=password_length)

#Print the password generated
print("\nYour password is:", ''.join(password))
