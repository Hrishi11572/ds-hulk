'''
The map() function applies a given function to every element of an iterable (e.g., a list) and returns a map object (an iterator).

- map(function, iterable)

* function: A function that takes an element of the iterable as input and returns a new value.

* iterable: The sequence (e.g., list, tuple) whose elements the function will process.
'''


numbers = range(0, 10)
function_values = map(lambda x : x **2 , numbers)
print(list(function_values)) # prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
