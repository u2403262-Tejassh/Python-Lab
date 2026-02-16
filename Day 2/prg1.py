'''
Write a program to implement a simple calculator and perform all arithmetic
operations.
'''
a = int(input("Enter first operand: "))
b = int(input("Enter second operand: "))
op = input("Enter operator(+, -, *, /): ")
if op == '+':
    res = a+b
elif op == '-':
    res = a-b
elif op == '*':
    res = a*b
elif op == '/':
    res = a/b
else:
    print("Invalid operator!")
print("Result =",res)
