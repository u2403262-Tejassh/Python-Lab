'''
4. Write a Python program that takes marks for 5 subjects as input, calculates the total,
percentage, and displays the result in a formatted way.
'''
mark1 = int(input("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))
mark3 = int(input("Enter marks for subject 3: "))
mark4 = int(input("Enter marks for subject 4: "))
mark5 = int(input("Enter marks for subject 5: "))
total = mark1+mark2+mark3+mark4+mark5
percent = total/5
print("Total marks:",total,"\nPercentage:",percent)
