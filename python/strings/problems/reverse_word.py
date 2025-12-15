'''
Given a string of words S. Print the string formed by reversing each word of the string. 
'''

S = input()
ls = S.split()

for word in ls: 
    word = list(reversed(word))
    word = "".join(word)
    print(word, end=" ")
