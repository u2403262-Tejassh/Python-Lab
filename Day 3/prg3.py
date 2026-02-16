'''
Write a Python program to create a tuple of 10 numbers:
a. Calculate and print the sum and product of the elements
b. Check if the specific number is in the tuple.
c. Add two new elements to the list.
'''

list1=[]
sum=0
prod=1
for i in range(10):
    num = int(input("Enter element at index "+str(i)+": "))
    list1.append(num)
    sum+=num
    prod*=num
print("Sum =",sum)
print("Product =",prod)
tup=tuple(list1)
srch=int(input("Enter number to search: "))
if srch in tup:
    print(srch,"is present")
else:
    print(srch,"is not present")
list1.append(int(input("Enter first new element: ")))
list1.append(int(input("Enter second new element: ")))
print(list1)
