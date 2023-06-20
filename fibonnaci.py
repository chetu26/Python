n=int(input('enter number:'))
def fib(n):
    if n<0:
        return -1
    if n==1:
        return 0
    if n==2:
        return 1

    return fib(n-1)+fib(n-2)        

print('number at',n,'is:',fib(n))