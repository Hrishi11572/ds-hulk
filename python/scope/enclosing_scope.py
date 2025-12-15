'''
Docstring for scope.enclosing_scope

Enclosing (Nonlocal) Scope:

    Variables in the enclosing scope of a nested function.
    Accessible inside nested functions using the nonlocal keyword.

'''


def outerFunction(): 
    enclosing_var = "Outer"
    
    def inner_function(): 
        nonlocal enclosing_var # so that changes made to the variable in the `inner function``, reflect in the `outer function` as well 
        enclosing_var = "Modified Outer"
        print("Inside inner function:", enclosing_var)
    
    inner_function()
    print("Inside outer function: ", enclosing_var)


outerFunction()