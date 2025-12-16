''' On dictionary methods'''

# 1. keys() : Returns a view object containing all the keys in the dictionary.

student_marks = {
    "alice" : 19, 
    "charile" : 20, 
    "mizzi" : 15, 
    "dona" : 18
}

print(student_marks.keys())


# 2. values() Method : Returns a view object containing all the values in the dictionary.

print(student_marks.values())

# items() Method : Returns a view object containing key-value pairs as tuples.

print(student_marks.items())


''' 
fromkeys() Method
Creates a new dictionary with keys from an iterable and a default value.
'''

keys = ["alice", "bob", "mizzi"]
new_dict = dict.fromkeys(keys, 1)

print(new_dict) # {'alice': 1, 'bob': 1, 'mizzi': 1}