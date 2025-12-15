'''
Using **kwargs (Keyword Variable Arguments)::

    Collects additional keyword arguments into a dictionary.
'''

def display_info(**kwargs): 
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, country="USSR")

'''
Explanation:

    **kwargs captures keyword arguments as key-value pairs in a dictionary.
    Useful for functions where argument names are dynamic.

'''
