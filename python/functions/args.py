'''
Lesson on Variable length parameters in functions 

Using *args (Non-keyword Variable Arguments):

    Collects additional arguments into a tuple.

'''

def add_numbers(*args):
    print(f"Numbers: {args}")
    return sum(args)

print(add_numbers(1, 2, 3, 4, 5 , 6 , 7 , 8))  # Outputs: Numbers: (1, 2, 3, 4), Total: 10

'''
Explanation:

    *args allows you to pass any number of arguments to the function.
    Arguments are accessible as a tuple inside the function.
'''
