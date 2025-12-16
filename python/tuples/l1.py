'''
A tuple is a built-in Python data type that is used to store multiple items in a single variable. Tuples are similar to lists, but they are immutable, meaning their elements cannot be modified after they are created.

Immutable: Once a tuple is created, its elements cannot be added, removed, or changed.

Heterogeneous Data: A tuple can store different types of data (e.g., integers, strings, lists).

Hashable: Tuples can be used as keys in dictionaries if they contain only immutable elements.
'''

'''
Taking User Input for Tuples
Use the map() function to convert space-separated input into integers and store them in a tuple. Taking input of tuples is similar to taking input of lists.
'''

# Input: 1 2 3 4
t = tuple(map(int, input().split()))

print(t)


''' Unpacking using * operator '''
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)  # Outputs: 1
print(middle) # Outputs: [2, 3, 4]
print(last)   # Outputs: 5
