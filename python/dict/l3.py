'''
Deletion in a dictionary 
'''

# 1. using `del` keyword
student_marks = {"Alice": 85, "Bob": 90, "Charlie": 78}
del student_marks["Charlie"]
print(student_marks)

# Outputs: {'Alice': 85, 'Bob': 90}

# 2. using `pop()` keyword
student_marks = {"Alice": 85, "Bob": 90, "Charlie": 78}
removed_value = student_marks.pop("Bob")
print(removed_value)      # Outputs: 90
print(student_marks)      # Outputs: {'Alice': 85, 'Charlie': 78}


# Outputs: {'Alice': 85, 'Bob': 90}


# 3. using `clear()` keyword 
student_marks = {"Alice": 85, "Bob": 90, "Charlie": 78}
student_marks.clear()
print(student_marks)
# Outputs: {}
