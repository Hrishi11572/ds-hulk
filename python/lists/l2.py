'''
Taking Input for Different Types of Lists:

    1. Integer Lists

    To take input of a list of integers, use the map() function along with split() to convert the input strings to integers.

    The split() method breaks the string into individual elements based on spaces, creating a list of strings.

    The map(int, ...) function then converts each string element into an integer. Finally, wrapping this in list() creates a list of integers.
    
    

'''

# Taking input of integers
numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
print("Integer List:", numbers)


'''
2. String Lists

For a list of strings, simply use the split() method without map().
'''

# Taking input of strings
words = input("Enter words separated by spaces: ").split()
print("String List:", words)
