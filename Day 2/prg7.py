'''
Write a program to take an email address as input and check if it is valid. (Basic
validation: must contain @ and .
'''
email = input("Enter email address: ")
if "@" in email and '.' in email:
    print("Valid email")
else:
    print("Invalid email")
