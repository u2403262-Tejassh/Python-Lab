'''
Write a program to take an integer input n and calculate the sum of squares of all
numbers from 1 to n and display the result.
'''
n = int(input("Enter limit: "))
sum = 0
for i in range(1,n+1):
    sum += i*i
print("Sum of squares till",n,"is",sum)

