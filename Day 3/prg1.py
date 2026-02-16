'''
Write a Python program to take a string as input and:
a. Print the length of the string
b. Convert the string to uppercase and lowercase.
c. Check if it is palindrome
d. Replace all vowels with _
e. Count the number of vowels
'''
string = input("Enter string: ")
length = len(string)
print("length =",length)
print("Uppercase:",string.upper(),"\tLowercase:",string.lower())
if string[::-1]==string:
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")
count = 0
for i in range(length):
    if string[i] in "AEIOUaeiou":
        string = string.replace(string[i],'_')
print("Replaced string:",string)
