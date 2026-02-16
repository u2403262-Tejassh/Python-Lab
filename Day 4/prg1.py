def fact(n) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return(fact(n-1)*n)
num = int(input("Enter number: "))
fact = fact(num)
print("Factorial =",fact)
