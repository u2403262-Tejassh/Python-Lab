def fib(lim):
    count = 2
    prev = 0
    curr = 1
    if lim == 0:
        return
    elif lim == 1:
        print("0")
    print("0 1",end=' ')
    while count<lim:
        t = curr
        curr += prev
        prev = t
        print(curr,end=' ')
        count+=1
limit = int(input("Enter Fibonacci series number limit: "))
fib(limit)
