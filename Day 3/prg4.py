'''
Write a Python program to create a dictionary with 5 key- value pairs:
a. Print all the keys , values , items in the dictionary.
b. Update the value of a specific key.
c. Add a new value to the dictionary.
'''
dict1 = {1:'a',2:'b',3:'c',4:'d',5:'e'}
print("Keys: ",dict1.keys(),"\nValues: ",dict1.values(),"\nItems: ",dict1.items())
key = int(input("Enter key of the value to be updated: "))
dict1[key] = input("Enter value to be updated: ")
key = input("Enter new key: ")
dict1[key] = input("Enter new value: ")
print(dict1)
