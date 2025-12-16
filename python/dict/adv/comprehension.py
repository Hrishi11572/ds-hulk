# Dictionary comprehension 

'''
1. Syntax of Dictionary Comprehension
    The general syntax for dictionary comprehension is:

        {key_expression: value_expression for item in iterable if condition}
    
    |-> key_expression: Expression to compute keys.
    |-> value_expression: Expression to compute values.
    |-> iterable: The source from which items are drawn (e.g., list, range).
    |-> if condition: Optional filter to include only items that satisfy the condition.
'''


# dictionary of squares 

square = { x: x**2 for x in range(10) if x % 2 == 0}
print(square)

''' 
Swapping Keys and Values
    Reverse the keys and values of an existing dictionary.
'''

original = {"Alice": 85, "Bob": 90, "Charlie": 78}
reversed_dict = {value: key for key, value in original.items()}
print(reversed_dict)
# Outputs: {85: 'Alice', 90: 'Bob', 78: 'Charlie'}


''' 
Nested Dictionary 
'''

table = {x: {y: x * y for y in range(1, 6)} for x in range(1, 6)}
print(table)
# Outputs: {1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}, 2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}, ...}
