# About Strings and manipulation in python 



# 1. Writing multiline strings 

str1 = '''
    Hello, I am Hrishikesh Tiwari.
'''

print(str1)


# 2. f-strings 

name = "Hrishikesh"
print(f"I am {name} Tiwari.")


# 3. Concatenation, and repetition 

firstName = "Hrishikesh"
lastName = "Tiwari"

# concatenation 
print(firstName + lastName)

# repetition 
print(firstName *3)


# indexing 

str1 = "HelloIamHrishikeshTiwariOfIITKGP"
print(str1[0], str1[6], str1[9])