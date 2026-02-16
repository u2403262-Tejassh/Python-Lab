'''
6. Write a Python program to check the strength of a password based on
length, use of uppercase, lowercase, numbers, and special characters.
'''
password = input("Enter password: ")
upper_flag  = False
lower_flag = False
num_flag = False
spcl_flag = False
for i in password:
    if i.isupper():
        upper_flag = True
    if i.islower():
        lower_flag = True
    if i.isdigit:
        num_flag = True
    if not i.isalnum():
        spcl_flag = True
if len(password) >=8 and upper_flag and lower_flag and num_flag and spcl_flag:
    print("Strength: Strong")
elif len(password) <8 :
    print("Strength: Weak")
else:
    print("Strength: Moderate")
