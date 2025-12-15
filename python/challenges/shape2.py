N = int(input())

def printInvTriangle(N: int)->None:
    for i in range(0, N): 
        for k in range(1 , N-i+1): 
            print(" ", end="")
            
        for j in range(0 , 2*i+1):
            print("*", end="", sep=" ") 
        print("\n",end="")
    return None 

printInvTriangle(N)
    