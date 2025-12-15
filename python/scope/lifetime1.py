'''
# Keywords  

1. global keyword :
    To modify a global variable inside a function, use the global keyword.
    
2. nonlocal keyword: 
    To modify the variables in a nested function definition
'''


x = 56 


def modifyGlobal(): 
    global x 
    x += 45 
    
    print("Inside function x = ", x)
    return None 


print("Outside the value of x, before function call = ", x)
modifyGlobal()
print("Outside the value of x, after function call = ", x)




def modifyNonLocal(): 
    y = 34 
    print("Before inner function call" , y)
    def innerfunction(): 
        nonlocal y 
        y = 99 
        return None 
    innerfunction()
    print("After inner function call" , y)

# call the function to see the effect 
modifyNonLocal()