# print first N fibonacci numbers 

N = int(input())

ls = []

a = 0 
b = 1 
ls.append(a)
ls.append(b)

for i in range(1 , N-1): 
    c = a + b 
    ls.append(c)
    a = b 
    b = c 
    
if N >= 2 : 
    for n in ls: 
        print(n, end=" ") 
else : 
    print(0)