'''
Combining Dictionaries - 

Using update() Method : The update() method adds key-value pairs from one dictionary to another, updating existing keys.

Python 3.9+ allows merging dictionaries using the | operator.
'''


dict1 = {"Alice": 85, "Bob": 90}
dict2 = {"Charlie": 78, "Bob": 95}
dict1.update(dict2)
print(dict1)
# Outputs: {'Alice': 85, 'Bob': 95, 'Charlie': 78}

dict1 = {"Alice": 85, "Bob": 90}
dict2 = {"Charlie": 78, "Bob": 95}
merged = dict1 | dict2
print(merged)
# Outputs: {'Alice': 85, 'Bob': 95, 'Charlie': 78}
