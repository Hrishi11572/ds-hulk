'''
Some advanced string methods in python : 

- capitalize()
    Converts the first character of the string to uppercase and the rest to lowercase.

- title()
    Converts the first character of each word to uppercase.
    
- swapcase()
    Swaps the case of all characters in the string (uppercase becomes lowercase and vice versa).
    
- zfill(width)
    Pads the string with zeros on the left to ensure the string reaches the specified width.
    
- isalnum()
    Checks if all characters in the string are alphanumeric (letters or numbers).

- isalpha()
    Checks if all characters in the string are alphabetic.

- isdigit()
    Checks if all characters in the string are digits.
    
- islower()
    Checks if all characters in the string are lowercase.

- isupper()
    Checks if all characters in the string are uppercase.

- isspace()
    Checks if the string contains only whitespace characters.
'''


# 1. .capitalize()
text = "hello, python"
print(text.capitalize())


# 2. .title()
text = "python is a user friendly programming language, which was developed by guido von rossum."
print(text.title())


# 3. .swapcase()
text = "Python Is a Computer Lang"
print(text.swapcase())


# 4. .zfill()
text = "56"
print(text.zfill(5)) # prints : 00056

'''
ljust(width): Left-aligns the string.
rjust(width): Right-aligns the string.
center(width): Centers the string.
'''

text = "Python"

print(text.ljust(10, "*"))
print(text.rjust(10, "."))
print(text.center(10 , "="))


text = "none??"
print(text.isalnum()) # -- prints False because of the `??`
print(text.isalpha()) # -- prints False because ?? is not an alphabet 

text = "3455"
print(text.isdigit()) # -- returns True 


