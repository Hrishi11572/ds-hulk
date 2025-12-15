'''
On parameter parsing : by value & by reference

#    In Python, arguments are passed to functions using object references. This means that whether the argument behaves as "pass-by-value" or "pass-by-reference" depends on the mutability of the data type.

KEY CONCEPTS 

1. Mutable and Immutable Objects:

    Mutable Objects: Can be changed after creation. Examples: list, dict, set.
    Immutable Objects: Cannot be changed after creation. Examples: int, float, str, tuple.

2. Pass-by-Value Behavior:

    For immutable objects, Python creates a new object when changes are made inside the function. The original value remains unchanged outside the function.

3. Pass-by-Reference Behavior:

    For mutable objects, changes made to the object inside the function affect the original object outside the function.

'''

# EXAMPLE OF PASS-BY-VALUE 

def passbyValue(stringVar : str)->None:
    stringVar += " Heil Lord Voldemort!"
    
variable = "Harry Potter"
print(variable)
passbyValue(variable)
print(variable) # remains unchanged 

print("\n \n")

# EXAMPLE OF PASS-BY-REFERENCE 

def passbyRef(ls: list)->None:
    ls.append("Lord Voldermot!")
    return None 

ls = ["Harry", "Ron" , "Hermoine"]

print(ls)
passbyRef(ls)
print(ls)  # gets changed as its passed by reference 