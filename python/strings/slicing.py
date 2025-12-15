'''
The most annoying topic is this one. 

Learn from the example given .... 
'''

text = "HIMALAYAS"

print(text[0:5]) # prints : HIMAL
print(text[0:5:2]) # prints : HML

print(text[-1::-1]) # prints whole string reversed
print(text[-5:]) # prints last 5 characters `LAYAS`
print(text[-5::-1]) # prints first five characters in reversed : LAMIH


'''
Strings in Python are immutable, meaning their content cannot be changed after creation. However, you can create a new string by concatenating or slicing existing strings.
'''


# Throws Error
# text = "Immutable"
# text[0] = "I"