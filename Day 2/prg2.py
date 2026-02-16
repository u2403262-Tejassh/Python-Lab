'''
Write a program to find the largest of three numbers using the ‘if’ statement.
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a>b:
    if a>c:
        print(a,"is largest")
    else:
        print(b,"is largest")
if b>c:
    print(b,"is largest")
else:
    print(c,"is largest")
