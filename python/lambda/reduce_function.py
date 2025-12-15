'''
- reduce() (from functools)

The reduce() function applies a rolling computation to a sequence of elements and reduces it to a single value.

    reduce(function, iterable)
    - function: A function that takes two arguments and returns a single result.
    - iterable: The sequence to reduce.
'''

from functools import reduce 

numbers = range(11)
ls = reduce(lambda x, y : x+y , numbers)

print(ls)