'''
Mixing Parameter Types

You can use multiple parameter types in a single function, but they must follow this order:

    Positional Parameters
    Default Parameters
    *args
    **kwargs

'''


def describe_person(name, age=30, *hobbies, **details):
    print(name)
    print(age)
    print(hobbies) # prints as tuple 
    print(details) # prints as dictionary 

describe_person("John Macenroe", 75, "Tennis Player", "Shouting", gender="Male", color="Fair")