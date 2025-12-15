'''
Description

Given a number N. Print a face down right-angled triangle that has N rows.

Note:
Don't print any extra spaces after symbol "*".
Input Format

Only one line containing a number N.
Output Format

Print the face down right-angled triangle with N rows as described above.

    INPUT 
    4

    OUTPUT
    ****    
    ***
    **
    *
'''

N = int(input())

def printInvTriangle(N: int)->None:
    for i in range(1, N+1): 
        for j in range(1 , N-i+2):
            print("*", end="", ) 
        print("\n",end="")
    return None 

printInvTriangle(N)
    