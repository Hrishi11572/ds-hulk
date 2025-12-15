'''
Given a string S, Print the string from the beginning to the first "\" character without printing the "\".
'''

t = int(input())

while t > 0: 
    string = input()
    idx = string.find("\\")
    if idx != -1:
        print(string[:idx])
    else: 
        print(string)
    t = t - 1