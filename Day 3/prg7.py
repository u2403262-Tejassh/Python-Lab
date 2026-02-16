'''
Write a Python program to input a string
and count the number of vowels, consonants, and spaces.
'''
string = input("Enter string: ")
vow = 0
con = 0
space = 0
for i in string:
    if i in "aeiouAEIOU":
        vow+=1
    elif i.isalpha():
        con+=1
    elif i.isspace():
        space+=1
print("Vowels =",vow,"\nConsonants  =",con,"\nSpaces =",space)
