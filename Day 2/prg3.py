'''
Write a program to print numbers from 1 to 30, skipping multiples of 3. Use
‘continue’ to skip the iteration when a number is divisible by 3.
'''
for i in range(1,30):
    if i%3==0:
        continue
    else:
        print(i, end=' ')
