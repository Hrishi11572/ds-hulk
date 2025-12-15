

'''
    String Methods : 
        1. len()
        2. //.lower(); //.upper()
        3. //.strip()
        4. //.replace()
        5. //.split()
        6. //.join()
'''

# 1. len()
globalstring = "The Quick Brown Fox , Fox jumps over the lazy little dog."

print(len(globalstring))

print(globalstring.lower())
print(globalstring.upper())


# 2. .strip()

text = "    Hello World    "
print(text.strip())

# 3. .replace()

print(globalstring.replace("Fox", "Wolf"))

# 4. .split()

print(globalstring.split())

# 4. .join()

ls = ["Bob", "the", "builder"]

print("".join(ls))