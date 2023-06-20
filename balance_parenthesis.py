brackets=input('enter parenthesis:')
def check_balance(brackets):
    num=0
    
    for i in range(len(brackets)):
        if(brackets[i]=='['):
            num=num+1
        else:
            num=num-1
    if(num==0):
        return 1
    else:
        return 0        

print(check_balance(brackets))                
            
