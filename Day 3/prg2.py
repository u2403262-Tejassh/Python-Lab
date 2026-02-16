'''
Write a Python program to create a list of 10 random numbers between 1 and 100:
a. Find the Maximum , Minimum and average of the list.
b. Reverse the list.
c. Create a list of squares of all even numbers.
'''
import random
list=[]
sum=0
for i in range(10):
    list.append(random.randint(1,100))
    sum += list[i]
print(list)
avg=sum/10
print("Maximum =",max(list),"Minimum =",min(list),"Average =",avg)
for i in range(10):
    list[i],list[-i]
#list.reverse()
print("Reversed list:",list)
for i in range(10):
    list[i] = random.randrange(2,100,2)**2
print("Even squared list:",list)
