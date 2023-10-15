import random
import string

#Ask for the length of the password
password_length = int(input("Enter password length: "))

#Characters to use in the password
password_chars = string.ascii_letters + string.digits + '!@#$%&*?'

#The program will choose random characters and print it
print("\nYour password is:", end = " ")

for i in range(1, password_length):
    password = random.choice(password_chars)
    print(password, end='')
print()
