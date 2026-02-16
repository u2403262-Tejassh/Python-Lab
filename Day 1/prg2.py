'''
2. Write a Python script that:
      a. Declare a variable in the program.
      b. Determines and prints its data type and the variable. (do for all datatypes)
'''
List = [a:=67, b:=6.7, c:=complex(real=6, imag= 7), d:='a', e:="hello", f:=[1,2,3], g:=(1,2,3), h:={a:1, b:2}, i:=True]
for i in List:
    print("Value:",i, "\tDatatype: "+str(type(i)).strip('<>').removeprefix('class '))
    
