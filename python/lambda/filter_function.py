'''
- filter()
    The filter() function filters elements from an iterable based on a condition. It returns a filter object (an iterator) containing elements for which the condition evaluates to True.

    filter(function, iterable)
    |
    |-> function: A function that takes an element as input and returns True or False.
    |-> iterable: The sequence to filter.
'''

numbers = range(10)
even_numbers = filter(lambda x: x%2 == 0, numbers)

print(list(even_numbers)) # prints [0, 2, 4, 6, 8]