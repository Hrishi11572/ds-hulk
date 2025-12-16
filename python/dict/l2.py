'''
 - Creating dictionaries in python 
'''

# 1. by defining key-value pairs 

my_dict = {
    "alice" : 21, 
    "bob dylan" : 19    
}

print(my_dict)



# 2. by using the dict() constructor 

student_marks = dict(Bob = 29, Alice=21, Alexandra = 35)
print(student_marks)


'''Accessing Elements in a Dictionary'''

# 1. 
student_marks = {"Alice": 85, "Bob": 90, "Charlie": 78}
print(student_marks["Alice"])
# Outputs: 85



# 2. using `get` method
student_marks = {"Alice": 85, "Bob": 90, "Charlie": 78}
print(student_marks.get("alicaa",0))
# Outputs: 0
