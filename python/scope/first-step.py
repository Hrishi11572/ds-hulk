'''
On the scope and lifetime of variables in python


1. Scope of variables 
    The scope of a variable refers to the part of a program where a variable is accessible 

>> Types of Scope: 

    a. Local Scope 
        - Variables defined inside a function or a block.
        - Accessible only within the function or block where they are defined.


    b. Global Scope 
        - Variables defined outside any function or block.
        - Accessible throughout the program, including inside functions (with limitations).
        
    c. Enclosing (Nonlocal) Scope:

        - Variables in the enclosing scope of a nested function.
        - Accessible inside nested functions using the nonlocal keyword.
        
    d. Built-in Scope:

        - Names that are pre-defined in Python, such as built-in functions like print(), len(), etc.
        - Accessible throughout the program.
        
'''



# Example of Local Scope 

def knowLocalScope(stringvar : str)->None: 
    logan = "LOGAN"
    logan += stringvar
    print(logan)
    return None

print(knowLocalScope(" is my hero!"))

# print(logan) -- throws error 


# Example of Global scope 
gloabal_var = 23 

def printGlobalVar():
    global gloabal_var # without the `global` keyword, python thinks it is a local variable 
    gloabal_var += 1 # it is because of this assignment += , that python thinks it as local 
    print("This is printed, inside function - ", gloabal_var)
    return None 


printGlobalVar()
print("This is printed, outside the function - ", gloabal_var)


# Notice, python thinks gvar as global here, while due to assignment, it thought as local above
gvar = 34
def printIT():
    print("Inside the function", gvar)    
    return None 

printIT()
print("Outside the function" ,gvar)