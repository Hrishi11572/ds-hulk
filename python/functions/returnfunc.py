'''
Functions can return complex data structures like lists, dictionaries, and even other functions.
'''

def multiplier(factor):
    def multiply_by(n):
        return n * factor 
    return multiply_by


times3 = multiplier(3)
print(times3(10))