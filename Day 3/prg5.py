'''
Write a program to ask the user to input numbers separated by spaces.
a. Convert the input string into a list of integers.
b. Calculate and print the sum of the list.
'''
string = input("Enter numbers seperated by spaces: ")
list1 = string.split()
sum  = 0
for i in list1:
    i = int(i)
    sum += i
print("Sum =",sum)
