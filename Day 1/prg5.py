'''
5. Write a Python program to calculate simple interest and display.
'''
principle = int(input("Enter principle(Rs): "))
rate  = int(input("Enter rate(%): "))
time = int(input("Enter time(years): "))
simple_intrest = principle*rate*time/100
print("Simple intrest = Rs.", simple_intrest)
