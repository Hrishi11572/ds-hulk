'''
    It provides a compact syntax to generate new lists by applying an expression to each  element of an iterable or based on certain conditions. It is not only more readable but also often faster than using traditional loops.
    
    [expression for item in iterable if condition] 
    
    - `expression`: The operation or transformation to perform on each element.
    - `item`: The variable representing each element of the iterable.
    - `iterable`: Any iterable (e.g., list, range, string) to loop over.
    - `if condition`: (Optional) A filtering condition; only elements satisfying this condition are included.
'''

# 1 . numbers from 1 to 10 

ls = [x for x in range(11)]
print(ls)

# 2 . even numbers from 1 to 10

ls = [x for x in range(11) if x%2 == 0]
print(ls)


# 3 . squaring numbers from 1 to 10

ls = [x ** 2 for x in range(11)]
print(ls)


