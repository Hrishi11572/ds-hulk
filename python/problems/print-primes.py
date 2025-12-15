# Print Primes from 1 to N 

import math
N = int(input())

def checkPrime(X : int)->bool: 
    if X == 0 or X == 1: 
        return False 

    for i in range(2, math.floor(math.sqrt(X)) + 1): 
        if X%i == 0: 
            return False 
    
    return True

for i in range(1, N+1):
    if checkPrime(i): 
        print(i, end=" ")