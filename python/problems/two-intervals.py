# Find the interval of Intersection 
t = int(input())

while t>0: 
    l1, r1, l2 , r2 = map(int, input().split())
    
    if (l1 > r2 or l2 > r1): 
        print("-1")
    else:
        print(max(l1, l2), min(r1 , r2))
    t-=1