principle = int(input("Enter principle(Rs): "))
rate  = int(input("Enter rate(%): "))
time = int(input("Enter time(years): "))
simple_intrest = principle*rate*time/100
compound_intrest = principle*(1+rate/100)**time
print("Simple intrest = Rs.", simple_intrest, "\nCompound Intrest = Rs.",compound_intrest)
