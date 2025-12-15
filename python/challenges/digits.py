T = int(input())

while T >0 : 
    ls = list(input().strip()) # safe to remove blank spaces
    ls.reverse()
    print(" ".join(ls))
    T-=1 
