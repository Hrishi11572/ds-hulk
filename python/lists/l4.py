# list operations & methods 

# 1. concatenation 

ls1 = ["apple", "banana", "mango"]
ls2 = ["orange"]

ls3 = ls1 + ls2 


ls4 = [1 , 2 , 3]
ls5 = ls2 + ls4

print(ls3)
print(ls5)

# 2. Repetition 

ls6 = ls2 * 5
print(ls6)

# 3. in/not in 

'''
    in: Checks if an element exists in a list.
    not in: Checks if an element does not exist in a list.
    Returns True or False.
'''

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # Outputs: True
print("grape" not in fruits)  # Outputs: True