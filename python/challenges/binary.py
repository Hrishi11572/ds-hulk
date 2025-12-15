
'''
Description

Given a number NN. Print the result of doing the following operation on NN:

    Convert NN to its binary representation.
    Count number of ones in the above binary representation.
    Print the equivalent decimal number that its binary representation has only the number of ones that were counted above.

'''


t = int(input())

while t>0: 
    N = int(input())

    count = 0
    i = 0 

    while N > 0: 
        if N & 1: 
            count += 1 
        N >>= 1 

    print(pow(2, count)-1)
    t -= 1