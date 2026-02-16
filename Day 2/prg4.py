'''
Write a program that takes an integer as input and calculates the sum of its digits
using a ‘while’ loop.
'''
num = int(input("Enter number: "))
copy = num
sum = 0
while copy>0:
    digit = copy%10
    sum += digit
    copy = copy//10
print("Sum of the digits in",num,"is",sum)
