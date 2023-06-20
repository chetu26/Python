n=int(input('enter number:'))

def factorial(n):
    if n<0:
        return -1
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)    

print("factorial: ",factorial(n))