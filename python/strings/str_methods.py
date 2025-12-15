'''
Covers essential string methods like : 

    len()
    lower(), upper()
    strip()
    split()
    join()
    find()
    index()
'''

# 1. len()
text = "Python Programming, is a user friendly lang."

print(len(text))

# 2. lower() & upper()
lstr = text.lower()
print(lstr)

ustr = text.upper()
print(ustr)

# 3. replace()

new_txt = text.replace("Python", "C++")
print(new_txt, text, sep = " | ")

# 4. split()
'''
The split() method splits a string into a list of substrings based on a delimiter (default is space).
'''

spl_str = text.split(" ")
print(spl_str)

# 5. join()
'''
The join() method combines elements of an iterable (e.g., a list) into a single string using the string as a delimiter.
'''

new_txt = " - ".join(spl_str)
print(new_txt)


'''
find() returns the index of the first occurrence of a substring or -1 if not found.

index() is similar but raises a ValueError if the substring is not found.
'''
# 6. find()

print(text.find("user"))

# 7. index()

print(text.index("user"))